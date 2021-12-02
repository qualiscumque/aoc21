
data = []
with open("input/input.txt") as f:
  data = [int(line.strip()) for line in f.readlines() if line.strip()]

last = None
incs = 0
for line in data:
  if last:
      print(line, end=" ")
      if line > last: 
          print("increased <=")
          incs += 1
      elif line < last:
          print("decreased")
      else: 
          print("same")
  else:
    print("n/a no prev measure")
  last = line

print(f"incs {incs}")

