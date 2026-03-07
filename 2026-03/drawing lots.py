# Two teams compete against each other, with three players on each side. Team A consists of three players: a, b, and c; Team B consists of three players: x, y, and z. The match list is decided by drawing lots.Player a does not play against x, and player c does not play against x or z.
No_1 = ['a', 'b', 'c']
No_2 = ['x', 'y', 'z']

for a_opponent in No_2:
    for b_opponent in No_2:
        if b_opponent == a_opponent:
            continue
        for c_opponent in No_2:
            if c_opponent == a_opponent or c_opponent == b_opponent:
                continue
            if a_opponent != 'x' and c_opponent not in ['x', 'z']:
                print("drawing lots：")
                print(f"a vs {a_opponent}")
                print(f"b vs {b_opponent}")
                print(f"c vs {c_opponent}")
