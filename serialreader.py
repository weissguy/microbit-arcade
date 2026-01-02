import time
import threading
import serial
from pynput.keyboard import Controller, Key


# ---- Config ----
PORT = "COM3"
BAUD = 115200

CENTER = 512
THRESH = 150

READ_CHUNK = 64
IDLE_SLEEP_S = 0.005

# Safety: if we never see a newline, don't let the buffer grow forever.
MAX_BUFFER_BYTES = 8192
# Safety: ignore absurdly long single lines
MAX_LINE_BYTES = 1024

kb = Controller()


class SerialLineReader:
    """
    Buffered line reader similar to MakeCode's approach:
    - read bytes in chunks
    - accumulate into a buffer
    - split into lines by '\n'
    - keep partial line in buffer
    - handle CRLF and decoding errors safely
    """

    def __init__(self, ser: serial.Serial):
        self.ser = ser
        self.buf = bytearray()

    def poll_lines(self):
        """
        Non-blocking-ish: reads what it can, returns a list of decoded lines.
        """
        data = self.ser.read(READ_CHUNK)
        if not data:
            return []

        self.buf.extend(data)

        # Prevent runaway buffer growth if device spams without '\n'
        if len(self.buf) > MAX_BUFFER_BYTES:
            # Keep the last part (most likely to contain a newline soon)
            self.buf = self.buf[-MAX_BUFFER_BYTES:]

        lines = []

        while True:
            nl = self.buf.find(b"\n")
            if nl == -1:
                break

            raw_line = bytes(self.buf[:nl])  # up to but not including '\n'
            del self.buf[: nl + 1]           # remove line + '\n' from buffer

            # Handle CRLF: remove trailing '\r'
            if raw_line.endswith(b"\r"):
                raw_line = raw_line[:-1]

            # Ignore absurdly long lines (likely corruption / wrong baud)
            if len(raw_line) > MAX_LINE_BYTES:
                continue

            # Decode robustly
            line = raw_line.decode("utf-8", errors="ignore").strip()
            if line:
                lines.append(line)

        return lines


class ControllerApp:
    def __init__(self):
        self.stop_event = threading.Event()
        self.enabled = True

        try:
            self.ser = serial.Serial(PORT, BAUD, timeout=0.05)
        except serial.serialutil.SerialException:
            raise Exception('Could not open serial port. Is controller connected by USB?')

        self.reader = SerialLineReader(self.ser)

    def handle_line(self, line: str):

        parts = line.split(",")
        if len(parts) != 6:
            return
        try:
            x, y, a, b, c, d = map(int, parts)
        except ValueError:
            return

        # Horizontal
        if x < CENTER - THRESH:
            kb.press(Key.right)
            kb.release(Key.left)
        elif x > CENTER + THRESH:
            kb.press(Key.left)
            kb.release(Key.right)
        else:
            kb.release(Key.left)
            kb.release(Key.right)

        # Vertical
        if y < CENTER - THRESH:
            kb.press(Key.down)
            kb.release(Key.up)
        elif y > CENTER + THRESH:
            kb.press(Key.up)
            kb.release(Key.down)
        else:
            kb.release(Key.up)
            kb.release(Key.down)

        # Buttons (assuming active-low)
        if c == 0:
            kb.press(Key.space)
        else:
            kb.release(Key.space)

        if d == 0:
            kb.press(Key.enter)
        else:
            kb.release(Key.enter)

    def run(self):
        try:
            print('Reading serial...')
            while not self.stop_event.is_set():
                enabled = self.enabled

                if not enabled:
                    time.sleep(0.05)
                    continue

                lines = self.reader.poll_lines()
                if not lines:
                    time.sleep(IDLE_SLEEP_S)
                    continue

                for line in lines:
                    self.handle_line(line)

        finally:
            # cleanup
            print('Terminating.')
            try:
                self.ser.close()
            except Exception:
                pass


def main():
    app = ControllerApp()

    try:
        app.run()
    except KeyboardInterrupt:
        pass
    finally:
        app.stop_event.set()


if __name__ == "__main__":
    main()
