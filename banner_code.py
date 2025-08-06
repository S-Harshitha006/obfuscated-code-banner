import base64

part1 = [72, 65, 82, 83, 72, 73, 84, 72, 65, 32, 83]
part2 = "Q09NUFVURVIgU0NJRU5DRSBTVFVERU5U"

name = ''.join(chr(i) for i in part1)
role = base64.b64decode(part2).decode()

print(f"{name}, {role}")
