import random
from ..util import get_direction, position_equals


class RandomDiamondLogic(object):
    def __init__(self):
        self.goal_position = None

    def next_move(self, board_bot, board):
        props = board_bot["properties"]
        current_position = board_bot["position"]

        print (type(board))

        for thingy in board.gameObjects:
            if (thingy["type"]=="DiamondButtonGameObject"):
                self.goal_position = thingy.get("position")
        

        for thingy1 in board.gameObjects:
            if (thingy1["type"]=="BotGameObject"):
                if thingy1["properties"]["name"]=="robot":
                    #print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n WOOOOOOOOOOO \n\n\n\n\n\n\n\n\n")

                    if thingy1["properties"]["diamonds"] != 5:
                        print ("Ej 5 diamanter")
                        if self.goal_position["x"] != 0:
                            self.goal_position["x"] -= 1
                        else:
                            self.goal_position["x"] += 1







        if self.goal_position:
            # Calculate move according to goal position
            delta_x, delta_y = get_direction(
                current_position["x"],
                current_position["y"],
                self.goal_position["x"],
                self.goal_position["y"],
            )
            ("HOPPAS VI ÄR HÄR LUL")
            if (delta_x == 0 and delta_y == 0 ):
                delta_y += 1
            return delta_x, delta_y
        print ("BORDE EJ VARA HÄR")
        return 0, 0



"""
{"id":794523,"position":{"x":5,"y":1},"type":"DiamondButtonGameObject","properties":null}
,{"id":793402,"position":{"x":8,"y":11},"type":"BotGameObject","properties":{"diamonds":2,"score":37,"name":"robot","inventorySize":5,"millisecondsLeft":5563,"timeJoined":"2020-05-10T23:34:10.331Z","base":{"x":4,"y":10}}}
"""
