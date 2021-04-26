import re

s = input()
print("YES" if re.fullmatch("^(dream|dreamer|erase|eraser)+$", s) else "NO")
