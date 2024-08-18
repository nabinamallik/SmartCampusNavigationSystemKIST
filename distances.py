import math

# Define a function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

# Dictionary of points with their coordinates
coordinates = {
    'a':    (501, 285), #main gate
    'b':    (506, 262), #ATM
    'c':    (525, 306), #Temple
    'd':    (505, 308), #Security Chamber
    'cp1':  (488, 283), #Check Point 1
    'e':    (495, 361), #Parking Slot
    'cp2':  (398, 283), #check Point 2
    'cp3':  (392, 191), #check point 2.1
    'f':    (433, 187), #Mechanical Building
    'cp4':  (350, 287), #check point 3
    'cp5':  (318, 287), #check point 4
    'g':    (320, 220), #Cricket Ground
    'cp6':  (240, 288), #check point 5
    'cp7':  (240, 224), #check point 6
    'h':    (263, 223), #stage
    'i':    (240, 120), #Library / workshop
    'cp8':  (163, 295), #check point 7
    'cp9':  (164, 327), #Check point 8
    'j':    (138, 327), #CSE Building
    'cp10': (166, 398), #check point 9
    'cp11': (118, 394), #check point 10
    'k':    ( 99, 495), #2nd/3rd yr Hostel
    'l':    ( 48, 469), #1st yr Hotel
    'cp12': (171, 484), #check point 11
    'm':    (156, 505), #Principa Office
    'n':    (268, 487), #Electrical Building
    'cp13': (275, 545), #check point 12
    'o':    (188, 552), #Girls Hostel
    'cp14': (345, 482), #Check point 13
    'p':    (343, 437), #FootBall Ground
    'cp15': (410, 481), #Check Point 14
    'q':    (402, 389), #Civil Building
    'r':    (441, 385), #IMBA/MBA Building
    'cp16': (467, 476), #check point 15
    's':    (478, 516), #Maintenance
    't':    (439, 504), #VallyBall Ground
    'cp17': (415, 536), #check point 16
    'u':    (472, 546), #cafeteria
    'v':    (499, 551), #GYM
    'w':    (442, 568), #Kho-kho Ground
    'x':    (485, 576), #Basketball Ground
    'cp18': (417, 590), #check point 17
    'cp19': (419, 651), #check point 18
    'y':    (460, 662), #Jr Canteen
    'z':    (437, 691) #Sr Canteen
}

# Calculate distances between all pairs of coordinates
distances = {}
keys = list(coordinates.keys())

for i in range(len(keys)):
    for j in range(i + 1, len(keys)):
        point1 = keys[i]
        point2 = keys[j]
        distance = euclidean_distance(coordinates[point1], coordinates[point2])
        distances[(point1, point2)] = distance

# Output the calculated distances
print(distances)