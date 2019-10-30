# skribbl.io-autodraw-script
A tool that automates drawing images on the game skribbl.io. It redraws an clipboard image to the https://skribbl.io/ canvas (or any drawable screen, for that matter).

## Requirements
This has been developed and tested in Python 3.6.4, on Windows 10.

## Installation
1. Clone this repository.
2. Install Python 3.6.4.
3. Install dependencies with `pip install -r requirements.txt`.

## Usage
1. Select an image you'd like to redraw. Right-click on it and select the "Copy Image" option.
2. Run this script with `python main.py`. If you have an image in your clipboard, the script will ask you to hover the cursor over the position that you wish to redraw the image. Once you pick a position, press `spacebar` to start redrawing the image. If you'd like to quit the program at this point you can simply tap `q`.

It is recommended that you don't run this script on large images, because it will take a long time to finish drawing.

## Example
The following gif illustrates how to use the script:

![](example.gif)
