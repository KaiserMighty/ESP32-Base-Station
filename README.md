# ESP32 Base Station
This "base station" is a moduler program meant to run in the background of a windows computer, and act as the interface for various ESP32 based embedded system projects.

## Overview
The listener captures UDP messages over the `17388` port. The message is formatted into two parts, seperated by a colon. The first part is the "handler" identifier, and the second part includes any arguments.

The listener determines if the message has a colon or not; if it doesn't, then it assumes there are no arguments. It will then match the first part to the command map and call the appropariate handler function from the `handlers` directory.

## Handlers
Handlers are meant to be module python files that can easily be extended. Each handler is a python script, and a handler may contain as many functions as required:
* [doorbell.py](https://github.com/KaiserMighty/ESP32-Doorbell)
  * ring_bell: Play a ding audio cue
* [spotify.py](https://github.com/KaiserMighty/ESP32-SpotifyController)
  * controller_main: Input handler that calls the other functions
  * play_pause: Play or pause the current track
  * next_track: Skip the current track
  * previous_track: Play the previous track
  * loop_track: Set the loop mode to track
  * volume_up: Turn up the volume by 4
  * volume_down: Turn down the volume by 4

## Usage
1. Run `builder.bat` on Windows to create an `.exe` in the `dist` directory.  
2. Create a Basic Task in Task Scheduler with the following settings:
```
Trigger: When the computer starts
Action: Start a program
Program/script: dist\esp32_base_station.exe
```
Where `Program/script` points to the `exe` in the `dist` folder.  
* To run it in the background without restarting, simply run the `exe` file in dist once.  
* The listener can be turned off or restarted by ending the process using the Task Manager.

## Environment Variables
To abstract sensitive information, there is an `.env` file inside the `handlers` directory; here is the structure of that file:  
```
SPOTIPY_CLIENT_ID=
SPOTIPY_CLIENT_SECRET=
SPOTIPY_REDIRECT_URI=
SPOTIFY_DEVICE_ID=
```