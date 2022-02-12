import math
import random

# Count of points which should be calculated
# Increase the get a more precise result
# Too high values may crash the program
points = 1000000

# Count of points inside the unit circle
# If a random point is inside the unit circle,
# This count will be increased by 1
inside = 0

for i in range(points):
    # Coordinates of the Point P(x, y)
    # Both x and y will be between 0 and 1
    x = random.random()
    y = random.random()
    
    # Pythagorean theorem
    # Distance between the Point and the Origin
    # of the imaginary Cordinate System
    dist = math.sqrt(x * x + y * y)
    
    # If this distance is less or equal to 1 
    # (the radius of the unit circle), this means
    # the point is inside the unit circle
    if dist <= 1:
        # So increase the inside count
        inside += 1
        
# "inside / points" now gives the area of a quarter.
# Multiplying this quarter by 4, gives us the full 
# area of the unit circle - which is equal to Pi!
pi = (inside / points) * 4

# Log the final result!
print(pi)