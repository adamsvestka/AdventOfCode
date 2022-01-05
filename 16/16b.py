with open(__file__[:-4] + ".txt") as file:
    data = file.read().strip()

    from types import FunctionType
    from math import prod

    l = 4 * len(data)
    data = int(data, 16)
    p = l - 1

    # print(format(data, f"0{l}b") + " - " + str(data))

    def get(c=1):
        global p
        mask = ((1 << c) - 1) << (p - c + 1)
        p -= c
        val = (data & mask) >> (p + 1)
        # print(
        #     " " * (l - p - c - 1)
        #     + format(val, f"0{c}b")
        #     + " " * (p + 1)
        #     + " - "
        #     + str(val)
        # )
        return val

    class Packet:
        version: int
        type: int
        number: int
        operands: list
        operation: FunctionType

        def print(self, n=0):
            print(f"{'    ' * n}Packet(version={self.version}, type={self.type}):")
            if hasattr(self, "number"):
                print(f"{'    ' * (n + 1)}number={self.number}")
            if hasattr(self, "operands"):
                for operand in self.operands:
                    operand.print(n + 1)

        def calculate(self):
            if hasattr(self, "number"):
                return self.number
            return self.operation([operand.calculate() for operand in self.operands])

    def parse_packet():
        packet = Packet()
        packet.version = get(3)
        packet.type = get(3)
        if packet.type == 4:
            packet.number = 0
            while True:
                i = get()
                packet.number = packet.number << 4 | get(4)
                if i == 0:
                    break
        else:
            packet.operands = []
            if get():
                packets = get(11)
                for _ in range(packets):
                    packet.operands.append(parse_packet())
            else:
                bits = get(15)
                b = p - bits
                while p > b:
                    packet.operands.append(parse_packet())
            if packet.type == 0:
                packet.operation = sum
            elif packet.type == 1:
                packet.operation = prod
            elif packet.type == 2:
                packet.operation = min
            elif packet.type == 3:
                packet.operation = max
            elif packet.type == 5:
                packet.operation = lambda x: 1 if x[0] > x[1] else 0
            elif packet.type == 6:
                packet.operation = lambda x: 1 if x[0] < x[1] else 0
            elif packet.type == 7:
                packet.operation = lambda x: 1 if x[0] == x[1] else 0
        return packet

    packet = parse_packet()

    # packet.print()

    print(packet.calculate())
