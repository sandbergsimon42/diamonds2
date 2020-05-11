import os
import time

while (True):
    os.system("pipenv run start --token 65eab4f9-9a39-4c3f-b57d-77d71753dffc --board 4 --time-factor=1 --logic RandomDiamond")
    time.sleep(1)