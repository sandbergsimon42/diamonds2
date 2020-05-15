import os
import time

while (True):
    os.system("pipenv run start --token fa6a7f92-934c-489f-9953-d84c81529963 --board 1 --time-factor=1 --logic UpperRight")
    time.sleep(1)