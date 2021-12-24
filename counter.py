from collections import defaultdict

text = 'Do gaming instead of drugs'
chars = defaultdict(int)

for char in text:
    chars[char] += 1

print(chars['a'])
print(chars['g'])
print(chars['i'])
print(chars['d'])
print(chars['r'])
print(chars['u'])
print(chars['w'])