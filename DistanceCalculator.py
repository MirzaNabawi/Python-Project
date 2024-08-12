import math
def distance (x , y):
    return math.sqrt(abs(x)**2 + abs(y)**2)
x =float (input("Enter the X Coordinate: "))
y =float (input("Enter the Y Coordinate: "))

print ("The Distance is:", distance(x, y))
