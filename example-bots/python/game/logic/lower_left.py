import random
from ..util import get_direction, position_equals

#terminal 5
# test3.py
class LowerLeft(object):
    def __init__(self):
        self.goal_position = None
        self.previous_position = (None, None)

    def next_move(self, board_bot, board):
        props = board_bot["properties"]
        current_position = board_bot["position"]

        middle = {"x" : 7, "y" : 7}
        chill = {"x" : 3, "y" : 11}


        #print (type(board))

        base_distance = 1000

        for thingy in board.gameObjects:
            if (thingy["type"]=="BotGameObject"):
                if thingy["properties"]["name"]=="robot":
                    robot = thingy
                else:
                    robot = None
            if (thingy["type"]=="DiamondButtonGameObject"):
                #print (robot["properties"]["diamonds"])
                # Reset finns i rätt ruta
                if thingy.get("position")["x"] <= middle["x"] and thingy.get("position")["y"] >= middle["y"]:
                    self.goal_position = thingy.get("position")
                    if(robot):
                        for diamond in board.diamonds:
                            diamond_distance = (abs(robot["position"]["x"] - diamond.get('position')["x"])) + (abs(robot["position"]["y"] - diamond.get('position')["y"]))
                            total_distance = (abs(diamond.get('position')["x"] - robot["properties"]["base"]["x"])) + (abs(diamond.get('position')["y"] - robot["properties"]["base"]["x"])) + diamond_distance
                            if(diamond_distance < base_distance):
                                base_distance = total_distance
                                if base_distance > 3:
                                    if self.goal_position["x"] != 0:
                                        self.goal_position["x"] -= 1
                                    else:
                                        self.goal_position["x"] += 1

                #Reset finns i fel ruta
                else:
                    self.goal_position = chill






        if self.goal_position:
            # Calculate move according to goal position
            cur_x = current_position["x"]
            cur_y = current_position["y"]
            delta_x, delta_y = get_direction(
                current_position["x"],
                current_position["y"],
                self.goal_position["x"],
                self.goal_position["y"],
            )
            ("HOPPAS VI ÄR HÄR LUL")
            if (delta_x == 0 and delta_y == 0 ):
                delta_y += 1
            if (cur_x, cur_y) == self.previous_position:
                # We did not manage to move, lets take a turn to hopefully get out stuck position
                if delta_x != 0:
                    if self.goal_position["y"] > cur_y or cur_y == 0:
                        delta_y = 1
                    else:
                        delta_y = -1
                    delta_x = 0
                elif delta_y != 0:
                    if self.goal_position["x"] > cur_x or cur_x == 0:
                        delta_x = 1
                    else:
                        delta_x = -1
                    delta_y = 0
            self.previous_position = (cur_x, cur_y)
            return delta_x, delta_y
        print ("BORDE EJ VARA HÄR")
        return 0, 0



"""
{"id":794523,"position":{"x":5,"y":1},"type":"DiamondButtonGameObject","properties":null}
,{"id":793402,"position":{"x":8,"y":11},"type":"BotGameObject","properties":{"diamonds":2,"score":37,"name":"robot","inventorySize":5,"millisecondsLeft":5563,"timeJoined":"2020-05-10T23:34:10.331Z","base":{"x":4,"y":10}}}
"""
