import math
import matplotlib.pyplot as plt
import json
from scipy.optimize import fmin_cg
import numpy as np


def pol2cart(rho, phi):
    x = rho * math.cos(phi)
    y = rho * math.sin(phi)
    return [x, y]


def extract_corners(data, threshold):
    """Extract corners in data using its gradient
    Args:
        data (list): data to find corners
        threshold (float): threshold for corner detection. Point is considered
            as corner when gradient is above this value
    Returns:
        [list, np.gradient]: list with found corners and gradient projection 
    """
    f = np.array(data)
    grad = np.gradient(f)
    corners_iter = []
    for i in range(len(data)):
        if grad[i] > threshold or grad[i] < -threshold:
            corners_iter.append(i)
    return corners_iter, grad


def corners_to_cartesian(corners_iter, data):
    x = np.arange(0, len(data))
    angle = (np.pi / len(data)) * x
    corners = np.zeros(shape=[len(corners_iter), 2])
    for i in range(len(corners_iter)):
        corners[i, :] = pol2cart(rho=data[corners_iter[i]], phi=angle[corners_iter[i]])
    return corners


def euclidean_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def calc_rotation(x, y, theta):
    xp = math.cos(math.radians(theta)) * 0.1 + x
    yp = math.sin(math.radians(theta)) * 0.1 + y
    return xp, yp


def f(z, *args):
    x,y=z
    x1, y1, x2, y2, d1, d2 = args
    return ((((x1-x)**2)+((y1-y)**2)-d1**2)**2)+((((x2-x)**2)+((y2-y)**2)-d2**2)**2)


def plot_as_cartesian_with_corners_and_pose(data, corners, poi):
    pac = plt.figure()
    ax1 = pac.add_axes([0.1, 0.1, 0.8, 0.8])
    plt.plot(data[:, 0], data[:, 1], '.')
    plt.plot(corners[:, 0], corners[:, 1], 'ro')
    tmpx = []
    tmpy = []
    for i in range(len(poi)):
        tmpx.append(poi[i][0])
        tmpy.append(poi[i][1])
    plt.plot(tmpx, tmpy, 'yo')
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")


def showPlots():
    plt.show()



if __name__=="__main__":

    data = json.load(open('data/fwd.json'))

    pose_x = []
    pose_y = []

    for i in range(len(data)):

        snapshot = data[i]
        scan = snapshot["scan"]
        d2 = snapshot["d2"]
        d1 = snapshot["d1"]

        # corners extraction
        corners_iter, _ = extract_corners(data=scan, threshold=0.06)
        corners_grad = corners_to_cartesian(corners_iter=corners_iter, data=scan)
        
        poi_corenrs = [] # point of interest corenrs
        poi_corenrs.append([corners_grad[-4, 0], corners_grad[-4, 1]])
        poi_corenrs.append([corners_grad[-5, 0], corners_grad[-5, 1]])
        d2_CD = scan[corners_iter[-4]]
        d1_CD = scan[corners_iter[-5]]
        d0_CD = euclidean_dist(poi_corenrs[0], poi_corenrs[1])

        # bilateration procedure
        z0 = [1, 1]
        args = (0, 0, d0_CD, 0, d1_CD, d2_CD)
        res = fmin_cg(f, z0, args=args, disp=False)
        if (res[0] < 0):
            res[0] = -res[0]
        if (res[1] < 0):
            res[1] = -res[1]
        pose_x.append(res[0])
        pose_y.append(res[1])
        print("Iter: {},  x: {}  y: {}".format(i, res[0], res[1]))

        if i==0:
            x = np.arange(0, len(scan))
            phi = (np.pi / len(scan)) * x
            data_cart = np.zeros(shape=[len(scan), 2])
            for j in range(len(scan)):
                data_cart[j, :] = pol2cart(scan[j], phi[j])
            plot_as_cartesian_with_corners_and_pose(data=data_cart, corners=corners_grad, poi=poi_corenrs)


    # adjust coordinate system
    for i in range(0, len(pose_x)):
        pose_x[i] -= pose_x[-1]
        pose_y[i] -= pose_y[-1]
    
    # plot pose
    plt.plot(pose_x, pose_y, '--go')
    plt.legend(['scan','corners', 'poi', 'pose'])
    plt.show()