import os
import time

while (True):
    os.system("pipenv run start --token 1b13fd3a-495b-46ee-b763-7b92fff864c4 --board 1 --time-factor=1 --logic UpperLeft")
    time.sleep(1)