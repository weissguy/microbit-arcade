# MakeCode Arcade with Joystick:bit Controller

*In-class only*. For the YBM x MIT Workshop January 2026.

## Setup
1. Ensure Python $\geq$ 3.9 (https://www.python.org/) is installed.
2. Install Python dependencies. You can do this by following these steps:
    - Open a Command Prompt by clicking on the Windows search bar and typing `cmd`.
    - Type the command `py -m pip install pyserial` and hit Enter.
    - Type the command `py -m pip install pynput` and hit Enter.
3. Clone this Git repository. The easiest way to do this is:
    - Click on the green "Code" button, then "Download Zip".
    - Open File Explorer and navigate to your Downloads folder. Right click on "microbit-arcade-main.zip" and click "Extract".
    - You should now see the three files in this repository in the folder "microbit-arcade-main".

## Configuring the Microbit target

Your joystick:bit controller is powered by a microbit processor. We want the processor to communicate with your computer through a serial interface. In order to do this, we'll download some code onto the microbit.

1. Plug the Joystick:bit controller into your computer with USB.
2. Navigate to https://makecode.microbit.org and open a new project.
3. Click on the JavaScript tab of the project and delete any code already there. Now, copy the contents of `serialwriter.js`, and paste the code into the JavaScript tab of the MakeCode project.
4. Press "Download". You'll be prompted to plug in the controller, then pair the BBC Microbit object and connect. Press "Download", and the code will load on your microbit.
    - You'll know the code is downloaded if you see a smiley face on the LEDs :)
5. *Important*: Click "Disconnect" in the MakeCode editor (otherwise, this tab will interfere with the next step). Keep the controller plugged into the computer by USB.


## Mapping serial data to keyboard events

Now that we have data from the joystick, we need to connect it to the MakeCode Arcade simulator. The simulator accepts input from your computer keyboard (Space, Enter, Up, Down, Left, Right), so we'll map values from serial to simulated keyboard events using a Python script.

1. Open a Command Prompt by clicking on the Windows search bar and typing `cmd`.
2. Navigate to the "microbit-arcade-main" folder. Instructions for this will vary based on your file structure, but most likely: `cd Desktop/microbit-arcade-main`
3. Run the following command to start reading serial data: `py serialreader.py`
    - You'll know the command worked if you see "Reading serial..." printed to the terminal.

## Code & game!!

Open https://arcade.makecode.com/ and get started! Feel free to use the templates in this repository as a building block.

When you're done using the joystick, go to the Command Prompt and press "Ctrl+C" to stop the Python script.
