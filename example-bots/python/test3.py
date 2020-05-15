import os
import time

while (True):
    os.system("pipenv run start --token 13df346a-5720-4963-8750-68b16cd5bd60 --board 1 --time-factor=1 --logic LowerLeft")
    time.sleep(1)