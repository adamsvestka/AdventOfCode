with open(__file__[:-4] + ".txt") as file:
    count = 0
    for line in file:
        inputs, outputs = line.split(" | ")
        inputs = [*map(set, inputs.split())]
        digits = [None] * 10

        def find(pred):
            found = [x for x in inputs if pred(x)][0]
            inputs.remove(found)
            return found

        digits[1] = find(lambda x: len(x) == 2)
        digits[4] = find(lambda x: len(x) == 4)
        digits[7] = find(lambda x: len(x) == 3)
        digits[8] = find(lambda x: len(x) == 7)
        digits[9] = find(lambda x: digits[4] | digits[7] <= x)
        digits[5] = find(lambda x: len(x) == 5 and digits[9] - digits[1] <= x)
        digits[6] = find(lambda x: digits[5] <= x)
        digits[0] = find(lambda x: len(x) == 6)
        digits[3] = find(lambda x: digits[1] <= x)
        digits[2] = find(lambda x: x)
        number = 0
        for out in outputs.split():
            out = set(out)
            number *= 10
            number += next(i for i, s in enumerate(digits) if s == out)
        count += number
    print(count)
