with open("input.csv", "r") as infile, open("output.csv", "w") as outfile:
    for line in infile:
        print(line.strip())
        outfile.write(line)