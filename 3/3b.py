with open(__file__[:-4] + ".txt") as file:

    def rating(b: int):
        file.seek(0)
        numbers = [line.strip() for line in file]
        for i in range(len(numbers[0])):
            bits = sum(int(num[i]) for num in numbers)
            if bits >= len(numbers) / 2:
                numbers = list(filter(lambda num: num[i] == str(b), numbers))
            else:
                numbers = list(filter(lambda num: num[i] == str(1 - b), numbers))
            if len(numbers) == 1:
                return numbers[0]

    o2 = rating(1)
    co2 = rating(0)
    print(int(o2, 2) * int(co2, 2))
