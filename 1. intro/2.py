import os
########################################################
filesNames = os.listdir("../BOOKS")
filesNames = sorted(
    filesNames, 
    key=lambda x: int(x.split(".")[0])
)
#remove this line
filesNames = filesNames[41:42]
########################################################
files = [ open(f"../BOOKS/{x}", "r") for x in filesNames ]
datas = [ x.readlines() for x in files ]
########################################################
def preproc(book):
    book = [ x.strip() for x in book ]
    book = [ x.lower() for x in book ]
    return book
########################################################
datas = list(map(preproc, datas))
for fileName, data in zip(filesNames, datas):
    print(fileName, len(data))
    data = " ".join(data).strip().split(" ")
    freq = dict([(x, data.count(x)) for x in data])
    for k, v in freq.items():
        print(k, v)
########################################################