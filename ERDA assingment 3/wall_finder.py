import numpy as np
from math import floor
def vision(guard, room,reso_matrix,angle_reso):
    # guard is a list with [x,y] position of the given guard
    # room is a numpy array [matrix] with the walls and where the guards can see
    # outputs the room with where the guard can see it
    # 0 no one can see that point
    # 1 is a wall
    # 2 is a point that guards can see
    # it will start with polar coordinates and check for each angle how far the guard is from a wall
    # angle_reso is the number of points for angle
    radius_reso = reso_matrix/15  #small increment for angle
    theta_list = np.linspace(0, 2 * np.pi, angle_reso) #list with angles
    r = 0

    angle_check = np.zeros(angle_reso)
    ymax,xmax = (room.shape[0]-1),(room.shape[1]-1)

    while 0 in angle_check:
        r += radius_reso
        index = 0
        for angle in theta_list:
            if angle_check[index] != 1:

                x_cord = (floor((r*np.cos(angle)/reso_matrix) + guard[1]))
                y_cord = (floor((r*np.sin(angle)/reso_matrix) + guard[0]))


                if x_cord>xmax or y_cord>ymax or x_cord<0 or y_cord<0:
                    angle_check[index] = 1
                    continue

                if room[y_cord][x_cord] == 1:
                    angle_check[index] = 1
                    continue

                if room[y_cord][x_cord] == 0:
                    room[y_cord][x_cord] = 2

            index+=1

    return room

