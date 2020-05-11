Simple bot
==========

How to install
--------------

```bash
pip install pipenv
pipenv sync
```


Register bot
------------

First you need to register one or more bots if not already done. This can be done using the following command:

`pipenv run start --name <name> --email <email> --logic <logic>`

The application will print out a token if the registration was successful. Don't loose this token, it is your password to be able to play using this bot!


------ ONLINE
'botToken': '86e9bc53-5def-40c3-b6e5-832341c45d72'
------ ONLINE

pipenv run start --token 86e9bc53-5def-40c3-b6e5-832341c45d72 --board 2 --time-factor=1 --logic RandomDiamond
(Detta är vad jag körde med senast)

pipenv run start --name testiboyyy --email sandbergsimon42@gmail.com --board 4 --time-factor=5 --logic RandomDiamond
(för att lägga till ny robot)


----locally
###'botToken': 'fd9fecbe-547c-46d0-bdcd-f8645481f082' 
--------locally

Run a game session
------------------

When you have a token you can start a new game session (or continue an existing one) using the following command:

`pipenv run start --token <token> --logic <logic>`

The bot will play using the logic controller provided until game over. You can then run the bot again without having to register a new one.

Register multiple bots and play them all at once if you like!


Different logic controllers
---------------------------

Bots can play using different controllers (AI). There are two logic controllers implemented in this repository, namely:

* `game/logic/first_diamond.py`
* `game/logic/random.py`

All controllers implement a method called `next_move` that is called to calculate the next move given a board state.

You can use any of these two implementations as a start for your own implementation.
