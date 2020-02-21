import math

inf = open("4_directions.txt", "r")
outf = open("4_distance.txt", "w")

location = [0, 0]
while True:
    s = inf.readline()
    if s == "":
        break

    token, dist = s.split()
    dist = int(dist)
    if token == "UP":
        location[1] += dist
    elif token == "DOWN":
        location[1] -= dist
    elif token == "LEFT":
        location[0] -= dist
    elif token == "RIGHT":
        location[0] += dist
distance = math.sqrt(location[0] ** 2 + location[1] ** 2)
outf.write(str(round(distance)))

inf.close()
outf.close()