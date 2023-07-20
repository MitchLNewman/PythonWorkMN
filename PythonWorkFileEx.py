n = ["ManUtd", "ManCity", "Arsenal", "Chelsea","Liverpool"]

with open("teams.txt", "w") as file:
    for item in n:
        file.write("%s\n" % item)
    print("Done")