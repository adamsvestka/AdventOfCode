with open(__file__[:-4] + ".txt") as file:
    data = int(file.read().strip(), 16)

    from math import ceil

    p = 4 * ceil(data.bit_length() / 4) - 1

    def get(c=1):
        global p
        mask = ((1 << c) - 1) << (p - c + 1)
        p -= c
        val = data & mask
        return val >> (p + 1)

    class Packet:
        version: int
        type: int
        number: int
        operands: list

        def print(self, n=0):
            print(f"{'    ' * n}Packet(version={self.version}, type={self.type}):")
            if hasattr(self, "number"):
                print(f"{'    ' * (n + 1)}number={self.number}")
            if hasattr(self, "operands"):
                for operand in self.operands:
                    operand.print(n + 1)

    version = 0

    def parse_packet():
        global version
        packet = Packet()
        packet.version = get(3)
        version += packet.version
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
        return packet

    parse_packet()  # .print()

    print(version)
