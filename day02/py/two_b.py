data = []
with open("input/input.txt") as f:
  data = [line.strip() for line in f.readlines() if line.strip()]

print(data)

class Pos: 
    x = 0
    y = 0
    aim = 0
  
    def __init__(self, x, y, aim):
        self.x = int(x)
        self.y = int(y)
        self.aim = int(aim)

    def __repr__(self):
        return f"Pos: ({self.x}, {self.y}, aim {self.aim})"

command = {
        "down": lambda pos, dist: Pos(pos.x, pos.y, pos.aim+dist),
        "up": lambda pos, dist: Pos(pos.x, pos.y, pos.aim-dist),
        "forward": lambda pos, dist: Pos(pos.x+dist, pos.y+(dist*pos.aim), pos.aim),
        }

pos = Pos(0, 0, 0)
print(pos)

for step in data:
    op, dist = step.split(" ")
    pos = command[op](pos, int(dist))
    print(pos)

print(pos.x * pos.y)
