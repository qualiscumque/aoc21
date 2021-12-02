
data = []
with open("input/input.txt") as f:
  data = [int(line.strip()) for line in f.readlines() if line.strip()]

last = None
incs = 0
for idx, line in enumerate(data):
  if idx-2 >= 0:
    entry = data[idx] + data[idx-1] + data[idx-2] 
    if last:
      print(entry, end=" ")
      if entry > last: 
        print("increased <=")
        incs += 1
      elif line < last:
        print("decreased")
      else: 
        print("same")
    else:
      print("n/a no prev measure")
    last = entry

print(f"incs {incs}")

