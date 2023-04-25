# take in inp.txt and replace all "xyz" with the val below

val = "LUADDY"

with open("inp.txt", "r") as f:
    lines = f.readlines()

with open("out.txt", "w") as f:
    for line in lines:
        f.write(line.replace("xyz", val))

