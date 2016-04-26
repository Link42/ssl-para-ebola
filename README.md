# SSL Paraebola
*(Its a pun)*  
Basically a dumb software ruler for Shell Shock Live.

Bult in python3, this repo is very much so *batteries not included*. I'll explain what you can do to get it working will by no means hold your hand.

Also remeber you are a horrible person if you use this tool. Just putting that out there.  
\-Harbinger of Tanks

Big disclaimer, I haven't managed to match SSL's settings exactly. If someone wants to figure it out and let me know go for it. The information below explains how to tune the knobs for close to perfect acuracy.

![alt text](http://i.imgur.com/mMfz3XO.png "Screenshot")

&nbsp;

## Dependencies
This is built on basic python3, tested on 3.4 I have used PyQt4 for the window so youll need that as well as python3.

&nbsp;

## Resolution
The resolution for the program is currently just hardcoded to my 1440p monitor, youll have to change this if yours is different. The line to change here is the one with the `setGeometry()` fuction.

&nbsp;

## Settings
The two vertical sliders Gravity and Air Resistance need to be tuned before you will get any form of accuracy out of the ruler.
Best settings I have found are `Gravity: 256` and `Air Resistance: 32` This is not 100% accurate but good enough to land almost anything, bascially the longer the line the lower the accuracy.

Once you have gravity and air resistance set, they can and should bascially just be left alone. Incresing air resistance to like 40-50 when your shot is getting past ~75 power can give you a little better results. Why? I dont know.

&nbsp;

## Usage
In case it isnt straight forward you use your clicky thing to line up the reticule with your tank, then find your shot with the sliders down below. They translate directly in the games power and angle figures. I'm too lazy to make the angle slider match SSL when you're shoiting left. So you will have to do `180 - Angle slider` to find the same number SSL will display.

&nbsp;
&nbsp;

### Use and Abuse
Use it, rek some people I dont care. Feel your soul slowly drain as you ruin the game for everyone. You dirty, dirty cheater...  
If you're interested in contributing or perhaps know why my shitty software doesn't match shell shock exactly let me know. :)

For bonus points make it deal with wind, I don't play with wind myself. But don't think it will be very hard to compensate for it.
