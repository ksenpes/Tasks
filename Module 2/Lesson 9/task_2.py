def convert_to_hex(R, G, B):
    return('#{:02x}{:02x}{:02x}'. format(R, G, B))

R, G, B = list(map(int, input('R G B: ').split(', ')))
HEX = convert_to_hex(R, G, B)
print('HEX: ', HEX.upper())