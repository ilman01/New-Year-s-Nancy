from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import time
import pygame
from datetime import datetime
import calendar
from mutagen.mp3 import MP3

# Target time
year = 2023
month = 12
day = 31
hour = 11
minute = 15
second = 0

timeZoneCompensation = 25200 # Difference between GMT and your timezone (in seconds)

# Path to MP3 File
MP3File = "The Fanciest Midnight.mp3"
audioLength = 88.8
#audioLength = MP3(MP3File).info.length



targetTimeEpoch = calendar.timegm(datetime(year, month, day, hour, minute, second).timetuple()) - timeZoneCompensation
currentTimeEpoch = time.time()

print("Script Start Time Epoch: " + str(currentTimeEpoch))
print("Target Time Epoch: " + str(targetTimeEpoch))
print("Target Time: " + datetime(year, month, day, hour, minute, second).strftime('%Y-%m-%d %H:%M:%S'))
print("Waiting until: " + str(audioLength))


print("Waiting for time...")

pygame.mixer.init()
pygame.mixer.music.load(MP3File)

while targetTimeEpoch - audioLength >= currentTimeEpoch:
    currentTimeEpoch = time.time()

    print("Current Clock: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "      " +"Time until target time: " + str(targetTimeEpoch - currentTimeEpoch), end="\r")


print("\nTime met! Playing audio.")

time.sleep(0.5)

currentTimeEpoch = time.time()
timeUntilTarget = targetTimeEpoch - currentTimeEpoch

print("Playing audio from: " + str(audioLength - timeUntilTarget))
pygame.mixer.music.play(start=audioLength - timeUntilTarget)


while True:
    print("Current Clock: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "     " + "Time: " + str(pygame.mixer.music.get_pos()/1000), end="\r" )

    if str(pygame.mixer.music.get_pos()/1000) == "-0.001":
        break

input("\nHappy New Year!")