import random
from ..util import get_direction


class FirstDiamondLogic(object):
    def __init__(self):
        self.goal_position = None
        self.previous_position = (None, None)
        #self.turn_direction = 1

    def next_move(self, board_bot, board):
        props = board_bot["properties"]

        base_distance = 1000

        current_position = board_bot["position"]

        # Analyze new state
        if props["diamonds"] == 5:
            # Move to base if we are full of diamonds
            base = props["base"]
            self.goal_position = base
        else:
            # Move towards first diamond on board
            for diamond in board.diamonds:
                diamond_distance = (abs(current_position["x"] - diamond.get('position')["x"])) + (abs(current_position["y"] - diamond.get('position')["y"]))
                total_distance = ((abs(diamond.get('position')["x"] - props["base"]["x"])) + (abs(diamond.get('position')["y"] - props["base"]["y"]))/(5/(props["diamonds"]+1))) + diamond_distance

                if (not (props["diamonds"] == 4 and diamond.get('properties')["points"] == 2)):
                    if(total_distance < base_distance):
                        base_distance = total_distance
                        self.goal_position = diamond.get('position')
                    elif (total_distance == base_distance and diamond.get('properties')["points"] == 2):
                        base_distance = total_distance
                        self.goal_position = diamond.get('position')

        if self.goal_position:
            cur_x = current_position["x"]
            cur_y = current_position["y"]
            delta_x, delta_y = get_direction(
                cur_x,
                cur_y,
                self.goal_position["x"],
                self.goal_position["y"],)

            #TODO: Fixa så man ej fastna om x, y = 0, 15
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
        
        return 0, 0


"""
"gameObjects":[{"id":49,"position":{"x":9,"y":13},"type":"TeleportGameObject","properties":{"pairId":"1"}},{"id":50,"position":{"x":8,"y":8},"type":"TeleportGameObject","properties":{"pairId":"1"}},{"id":621619,"position":{"x":7,"y":2},"type":"BotGameObject","properties":{"diamonds":0,"score":6,"name":"Doris","inventorySize":5,"millisecondsLeft":19875,"timeJoined":"2020-05-10T21:27:41.088Z","base":{"x":7,"y":3}}},{"id":621620,"position":{"x":7,"y":3},"type":"BaseGameObject","properties":{"name":"Doris"}},{"id":621621,"position":{"x":8,"y":0},"type":"BotGameObject","properties":{"diamonds":5,"score":85,"name":"Gabby","inventorySize":5,"millisecondsLeft":21116,"timeJoined":"2020-05-10T21:27:42.329Z","base":{"x":7,"y":9}}},{"id":621622,"position":{"x":7,"y":9},"type":"BaseGameObject","properties":{"name":"Gabby"}},{"id":622181,"position":{"x":7,"y":0},"type":"BotGameObject","properties":{"diamonds":4,"score":0,"name":"robot","inventorySize":5,"millisecondsLeft":51254,"timeJoined":"2020-05-10T21:28:12.467Z","base":{"x":3,"y":14}}},{"id":622182,"position":{"x":3,"y":14},"type":"BaseGameObject","properties":{"name":"robot"}},{"id":622343,"position":{"x":7,"y":1},"type":"DiamondButtonGameObject","properties":null},{"id":622344,"position":{"x":11,"y":1},"type":"DiamondGameObject","properties":{"points":2}},{"id":622345,"position":{"x":5,"y":12},"type":"DiamondGameObject","properties":{"points":2}},{"id":622346,"position":{"x":7,"y":10},"type":"DiamondGameObject","properties":{"points":2}},{"id":622347,"position":{"x":11,"y":0},"type":"DiamondGameObject","properties":{"points":2}},{"id":622348,"position":{"x":5,"y":10},"type":"DiamondGameObject","properties":{"points":1}},{"id":622349,"position":{"x":5,"y":9},"type":"DiamondGameObject","properties":{"points":1}},{"id":622350,"position":{"x":12,"y":6},"type":"DiamondGameObject","properties":{"points":1}},{"id":622351,"position":{"x":11,"y":8},"type":"DiamondGameObject","properties":{"points":1}},{"id":622352,"position":{"x":8,"y":10},"type":"DiamondGameObject","properties":{"points":1}},{"id":622353,"position":{"x":4,"y":13},"type":"DiamondGameObject","properties":{"points":1}},
{"id":622354,"position":{"x":2,"y":2},"type":"DiamondGameObject","properties":{"points":1}},
{"id":622355,"position":{"x":7,"y":7},
"""