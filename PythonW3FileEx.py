def fileRead(fileName):
    txt = open(fileName)
    print(txt.read())

fileRead("test.txt")