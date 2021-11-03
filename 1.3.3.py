import sys

sys.argv[1]
sys.argv[2]

a = float(sys.argv[1])
b = float(sys.argv[2])

if (a >= 0.0) and (a <= 1.0):
    if (b >= 0.0) and (a <= 1.0):
        print(str('True'))
else:
    print(str('False'))
