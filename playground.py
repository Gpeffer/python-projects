import sys

ourArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\nLength of argv: " + str(len(ourArray)))
print()

ourArray[0] = 32

for i in range(len(ourArray)):
    ourArray[i] = 2 ** ourArray[i]

for i range(len(ourArray)):
    print(str(i) + "\t" + str(ourArray[i]))

print()

print("Sum: " + str(sum(ourArray)))
