import os
import time

while (True):
    os.system("pipenv run start --token 1ace84fa-f3c3-42f2-8a65-94837266f45e --board 1 --time-factor=1 --logic LowerRight")
    time.sleep(1)