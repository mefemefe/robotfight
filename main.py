def fight(robot_1, robot_2, tactics):
    tact1 = 0
    tact2 = 0
    fst = None
    sec = None
    if robot_1["speed"] >= robot_2["speed"]:
        fst = robot_1
        sec = robot_2
    else:
        fst = robot_2
        sec = robot_1
    while tact1 < len(fst["tactics"]) and tact2 < len(sec["tactics"]):
        sec["health"] -= tactics[fst["tactics"][tact1]]
        tact1 += 1
        if sec["health"] < 1:
            return fst["name"] + " has won the fight."
            # fst win

        fst["health"] -= tactics[sec["tactics"][tact2]]
        tact2 += 1
        if fst["health"] < 1:
            return sec["name"] + " has won the fight."
            # sec win

    if tact1 < len(fst["tactics"]):
        while tact1 < len(fst["tactics"]):
            sec["health"] -= tactics[fst["tactics"][tact1]]
            tact1 += 1
            if sec["health"] < 1:
                return fst["name"] + " has won the fight."
                # fst win

    elif tact2 < len(sec["tactics"]):
        while tact2 < len(sec["tactics"]):
            fst["health"] -= tactics[sec["tactics"][tact2]]
            tact2 += 1
            if fst["health"] < 1:
                return sec["name"] + " has won the fight."
                # sec win
    else:
        if fst["health"] == sec["health"]:
            return "The fight was a draw."
            # DRAW
        elif fst["health"] > sec["health"]:
            return fst["name"] + " has won the fight."
            # fst win
        else:
            return sec["name"] + " has won the fight."
            # sec win

'''
CAN CHANGE VALUES, 
NUMBER AND TYPE OF TACTICS A ROBOT HAS,
AND ADD NEW TACTICS.
DON'T CHANGE THE NAMES OF THE VALUES ("health" needs to remain as "health")
'''

robot_1 = {
  "name": "Rocky",
  "health": 100,
  "speed": 20,
  "tactics": ["punch", "punch", "laser", "missile"]
 }
robot_2 = {
   "name": "Missile Bob",
   "health": 100,
   "speed": 21,
   "tactics": ["missile", "missile", "missile", "missile"]
 }
tactics = {
   "punch": 20,
   "laser": 30,
   "missile": 35
 }

print(fight(robot_1,robot_2,tactics))