import subprocess

import os
import time

while (True):
    os.system("pipenv run start --token 86e9bc53-5def-40c3-b6e5-832341c45d72 --board 1 --time-factor=1 --logic FirstDiamond")
    time.sleep(1)


#subprocess.run(["pipenv run start", "--token 86e9bc53-5def-40c3-b6e5-832341c45d72", "--board 3", "--time-factor=2", "--logic RandomDiamond"])

#list_files = subprocess.run(["ls", "-l"])
