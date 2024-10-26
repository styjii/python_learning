world = "Python"

i = len(world) - 1
while i >= 0 :
    print(world[i])
    i -= 1

# correction
for letter in reversed(world) :
    print(letter)