import math

# You throw a dart that hits coordinates (x, y) on a dartboard.
# Create a program that gives you the score.
# See:
#   https://en.wikipedia.org/wiki/Darts#Dartboard
#   https://www.dimensions.com/element/dartboard

print("Enter the coordinates in mm from the center of the board.")
x = float(input("x? "))
y = float(input("y? "))

# Points of the sectors, clockwise from the top
# Example: the sector right from the center is POINTS[5] == 6.
POINTS = (20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5)

# COMPLETE...

distance = math.sqrt(x**2 + y**2)
angle = math.degrees(math.atan2(y, x))

if (distance > 170):
    print('OUT')
    exit(1)

print(f'Angle: {angle}')

angle += 180



if angle < 9:
    score = POINTS[5]
elif angle < 27:
    score = POINTS[4]
elif angle < 45:
    score = POINTS[3]
elif angle < 63:
    score = POINTS[2]
elif angle < 81:
    score = POINTS[1]
elif angle < 99:
    score = POINTS[0]
elif angle < 117:
    score = POINTS[19]
elif angle < 135:
    score = POINTS[18]
elif angle < 153:
    score = POINTS[17]
elif angle < 171:
    score = POINTS[16]
elif angle < 189:
    score = POINTS[15]
elif angle < 207:
    score = POINTS[14]
elif angle < 225:
    score = POINTS[13]
elif angle < 243:
    score = POINTS[12]
elif angle < 261:
    score = POINTS[11]
elif angle < 279:
    score = POINTS[10]
elif angle < 297:
    score = POINTS[9]
elif angle < 315:
    score = POINTS[8]
elif angle < 333:
    score = POINTS[7]
elif angle < 351:
    score = POINTS[6]
else:
    score = POINTS[5]

print(f'Score: {score}')
