n = ["ManUtd", "ManCity", "Arsenal", "Chelsea","Liverpool"]

with open("teams.txt", "w") as file:
    for item in n:
        file.write("%s\n" % item)
    print("Done")

file = open("teams.txt", "r")
lines = file.readlines(1)
print(lines)
file.close()

# get readlines to print 1st and 4th line somehow
# first line complete