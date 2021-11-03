import sys

sys.argv[0]
sys.argv[1]
sys.argv[2]

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if (a == b) and (b == c):
    print('equal')
else:
    print('not equal')
