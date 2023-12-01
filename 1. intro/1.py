file = open('../shakespeare.txt')
lines = file.readlines()
###########################################
def valid(char):
    if ord('A') <= ord(char) <= ord('Z'):
        return True
    if ord('a') <= ord(char) <= ord('z'):
        return True
    if ord('0') <= ord(char) <= ord('9'):
        return True
    if ord(' ') == ord(char):
        return True
    return False
###########################################
#lines = list(map(lambda x: x.strip(), lines))
lines = [ x.strip() for x in lines ]
lines = [ x.replace("\t", " ") for x in lines ]
lines = [ x.replace("  ", " ") for x in lines ]
for i in range(len(lines)):
    lines[i] = list(filter(valid, lines[i]))
    lines[i] = "".join(lines[i])
titles = lines[9:53]        #put titles in variable
lines = lines[54:]          #remove titles
###########################################
for i in range(len(titles)):
    start = lines.index(titles[i])
    if i < len(titles) - 1:
        end = lines.index(titles[i+1])
        chap1 = lines[start:end]
    else:
        chap1 = lines[start:]
    file2 = open(f"../BOOKS/{i+1}. {titles[i]}.txt", "w")
    for x in chap1:
        file2.write(x+"\n")
    file2.close()

file.close()