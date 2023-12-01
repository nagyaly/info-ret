data = open("../shakespeare.txt", "r")
lines = data.readlines()
lines = list(map(lambda x: x.strip().replace("    ", ""), lines))
names = lines[:45]
lines = lines[45:]
for line in names:
    start_index = lines.index(line)
    print(line, start_index)