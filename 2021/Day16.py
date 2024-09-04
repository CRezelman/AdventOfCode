"""Day 16"""

def hex_to_bin(hex_string):
    """Convert hexadecimal string to binary string."""
    return ''.join(f"{int(char, 16):04b}" for char in hex_string)


def parse_literal(binary, index):
    """Parse a literal value packet."""
    literal_value = ''
    while True:
        group = binary[index:index+5]
        literal_value += group[1:]
        index += 5
        if group[0] == '0':  # Last group in the literal value
            break
    return int(literal_value, 2), index


def parse_packet(binary, index=0):
    """Parse a packet and return the sum of version numbers, the value of the packet, and the new index."""
    version = int(binary[index:index+3], 2)
    type_id = int(binary[index+3:index+6], 2)
    index += 6

    if type_id == 4:  # Literal value
        value, index = parse_literal(binary, index)
    else:  # Operator
        length_type_id = int(binary[index], 2)
        index += 1
        values = []
        if length_type_id == 0:
            total_length = int(binary[index:index+15], 2)
            index += 15
            end_index = index + total_length
            while index < end_index:
                sub_version, sub_value, index = parse_packet(binary, index)
                version += sub_version
                values.append(sub_value)
        else:
            num_sub_packets = int(binary[index:index+11], 2)
            index += 11
            for _ in range(num_sub_packets):
                sub_version, sub_value, index = parse_packet(binary, index)
                version += sub_version
                values.append(sub_value)

        if type_id == 0: 
            value = sum(values)
        elif type_id == 1: 
            value = 1
            for v in values:
                value *= v
        elif type_id == 2:
            value = min(values)
        elif type_id == 3:
            value = max(values)
        elif type_id == 5:
            value = 1 if values[0] > values[1] else 0
        elif type_id == 6:
            value = 1 if values[0] < values[1] else 0
        elif type_id == 7:
            value = 1 if values[0] == values[1] else 0

    return version, value, index


def day16():
    """Day 16"""
    part1 = 0
    part2 = 0

    hex_input = open('2021/inputs/day16.txt', 'r').read()

    binary = hex_to_bin(hex_input)
    part1, part2, _ = parse_packet(binary)


    return part1, part2


print(day16())
