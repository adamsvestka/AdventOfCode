with open(__file__[:-4] + ".txt") as file:
    count = 0
    for line in file:
        inputs, outputs = line.split(" | ")
        inputs = inputs.split()
        outputs = outputs.split()
        for out in outputs:
            if len(out) in {2, 4, 3, 7}:
                count += 1
    print(count)
