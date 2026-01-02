# MakeCode Arcade with Joystick:bit Controller

For the YBM x MIT Workshop January 2026

## Configuring the Microbit target

The controller is going to write button/joystick to serial. To do this, we'll need to download some code onto the microbit processor.

1. Plug the Joystick:bit controller into your computer with USB
2. Navigate to https://makecode.microbit.org and open a new project
3. Copy `serialwriter.js` into the JavaScript tab of the project
4. Download the code to your controller
    - You'll know the code is downloaded if you see a smiley face on the LEDs :)
5. *Important*: Click "Disconnect" in the MakeCode editor (otherwise this tab will interfere with the next step)


## Mapping serial data to keyboard events

Now that we have live serial data, we need to connect it to the MakeCode Arcade simulator. The simulator accepts keyboard input (Space, Enter, A/W/S/D), so we'll map values from serial to keyboard events using a Python script.

1. Ensure Python $\geq$ 3.9 (https://www.python.org/) and Git (https://git-scm.com/) are installed
2. Clone this repository
3. Open a Command Prompt and navigate to the directory "microbit-arcade" (or your local parent folder)
4. Run the following command to start reading serial data: `py serialreader.py`

5. *Important*: When you're done using the controller, make sure to press "Ctrl+C" to stop the Python script


## Code & game!!

Open https://arcade.makecode.com/ and get started! Feel free to use the templates in this repository as a building block.
