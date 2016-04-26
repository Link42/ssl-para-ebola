# ssl-para-ebola
Its bascially a fancy software ruler for SSL

Bult in python3, this repo is bascially batteries not included. I'll explain what you can do to get it working will by no means hold your hand.

Big disclaimer, I haven't managed to match SSL's settings exactly. If someone wants to figure it out and send me a pull request go for it. See below in settings for best settings to use.

![alt text](http://i.imgur.com/mMfz3XO.png "Screenshot")

## Dependencies
This is built on basic python3, tested on 3.4 I have used PyQt4 for the window so youll need that as well as python3.


## Resolution
The resolution for the program is currently just hardcoded to my 1440p monitor, youll have to change this if yours is different. The line to change here is the one with the `setGeometry()` fuction.


## Settings
The two vertical sliders Gravity and Air Resistance need to be tuned before you will get any form of accuracy out of the ruler.
Best settings I have found are `Gravity: 256` and `Air Resistance: 32` This is not 100% accurate but good enough to land almost anything, bascially the longer the line the lower the accuracy.


## Usage
In case it isnt straight forward you use your clicky thing to line up the reticule with your tank, then find your shot with the sliders down below. They translate directly in the games power and angle figures. I'm too lazy to make the angle slider match SSL when you're shoiting left. So you will have to do `180 - Angle slider` to find the same number SSL will display.
