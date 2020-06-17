import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from FEM_strain import FEM_DATA_PLOT
# Opens the data
data = pd.read_csv("Measurements2014_05_22.txt", sep="\t", engine='python', header=4)
print(data.head())

#fem data :list of lists witf fem[i][j] i being the loadstep with (xcord,axial,bending)
FEM =FEM_DATA_PLOT()
FEMaxzero = FEM[0][1]
FEMbendzero = FEM[0][2]
#yield strain by department of denfence USA
yyield = -8860

code_location = {"A0": 1.58908, "A1": 2.09349, "A2": 2.59791,
                 "B0": 3.77008, "B1": 3.26436, "B2": 2.75864,
                 "C0": 0.192102, "C1": 0.414263, "C2": 0.510969, "C3": 0.673016, "C4": 0.793244, "C5": 0.848131,
                 "C6": 0.984042, "C7": 1.25324,
                 "D0": 5.17115, "D1": 4.95288, "D2": 4.83656, "D3": 4.68756, "D4": 4.55425, "D5": 4.50327,
                 "D6": 4.33205, "D7": 4.07065}

# the name was arranged so An and Bn have the same actual location, the same holds for C and D
actual_location = {"A0": 1.05, "A1": 0.55, "A2": 0.05,
                   "B0": 1.05, "B1": 0.55, "B2": 0.05,
                   "C0": 0.07, "C1": 0.296, "C2": 0.378, "C3": 0.54, "C4": 0.645, "C5": 0.70, "C6": 0.759, "C7": 1.027,
                   "D0": 0.076, "D1": 0.297, "D2": 0.388, "D3": 0.540, "D4": 0.650, "D5": 0.711, "D6": 0.764,
                   "D7": 1.024}

# data entry of column must be string
stiffeners = [0.34, 0.582, 0.627, 0.74]


def actual_location_est(p1, p2):
    code1 = str(code_location[p1])
    code2 = str(code_location[p2])
    if p1[0] in ["A", "C"]:  # ascending
        n = int(data.loc[0, code1:code2].shape[0])

    else:  # descending
        n = int(data.loc[0, code2:code1].shape[0])

    if p1[0] in ["A", "B"]:  # ascending
        x0 = actual_location[p2]
        x1 = actual_location[p1]

    else:  # descending
        x0 = actual_location[p1]
        x1 = actual_location[p2]

    return np.linspace(x0, x1, n)


# load step number      1  2   3   4   5
load_steps_t = [1, 13, 28, 40, 55]


load_step_ext = [0,"0","10","20","30","39"]

count = 1
for t in load_steps_t:

    FEMx = np.array(FEM[count-1][0])*1000
    FEMaxial = FEM[count-1][1]
    FEMbending = FEM[count-1][2]

    A_plot = []
    Ay_plot = []

    B_plot = []
    By_plot = []

    C_plot = []
    Cy_plot = []

    D_plot = []
    Dy_plot = []

    # getting the data for this time step from the table
    # First for C and D
    for i in range(7):
        Ca = "C" + str(i)
        Cb = "C" + str(i + 1)

        Da = "D" + str(i)
        Db = "D" + str(i + 1)

        strainC = data.loc[t, str(code_location[Ca]):str(code_location[Cb])]
        strainD = data.loc[t, str(code_location[Db]):str(code_location[Da])]

        xC = actual_location_est(Ca, Cb)
        xD = actual_location_est(Da, Db)

        C_plot.extend(xC[:-1])
        Cy_plot.extend(strainC[:-1])

        D_plot.extend(xD[:-1])
        Dy_plot.extend((strainD[::-1])[:-1])

    # Now adding A and B data to plot
    for i in range(1, -1, -1):  # has to run backwards because A and B are in the reverse order
        Aa = "A" + str(i)
        Ab = "A" + str(i + 1)

        Ba = "B" + str(i)
        Bb = "B" + str(i + 1)

        strainA = data.loc[t, str(code_location[Aa]):str(code_location[Ab])]
        strainB = data.loc[t, str(code_location[Bb]):str(code_location[Ba])]

        xA = actual_location_est(Aa, Ab)
        xB = actual_location_est(Ba, Bb)

        A_plot.extend(xA[:-1])
        Ay_plot.extend((strainA[::-1])[:-1])

        B_plot.extend(xB[:-1])
        By_plot.extend(strainB[:-1])

    # intervals where the fibers are attached
    interval1 = np.linspace(0.08, 0.303, 300)
    interval2 = np.linspace(0.381, 0.551, 200)
    interval3 = np.linspace(0.648, 0.709, 200)
    interval4 = np.linspace(0.761, 1.02, 300)

    # Make cubic splines and plot the graphs

    xnew = np.linspace(0.08, 1.02, 7000)  # interval for general strains

    Ainter = interpolate.interp1d(np.array(A_plot), np.array(Ay_plot), kind="cubic")
    Binter = interpolate.interp1d(np.array(B_plot), np.array(By_plot), kind="cubic")
    Cinter = interpolate.interp1d(np.array(C_plot), np.array(Cy_plot), kind="cubic")
    Dinter = interpolate.interp1d(np.array(D_plot), np.array(Dy_plot), kind="cubic")

    # General Strain
    plt.plot(xnew*1000, Ainter(xnew), label='A')
    plt.plot(xnew*1000, Binter(xnew), label=' B')
    plt.plot(xnew*1000, np.negative(Cinter(xnew)), label='$C_{-1}$')
    plt.plot(xnew*1000, np.negative(Dinter(xnew)), label=' $D_{-1}$')
    plt.plot(np.array(stiffeners)*1000, [0, 0, 0, 0], "o", label='Stiffeners')
    plt.plot(xnew*1000, (np.ones(xnew.shape)* yyield),'--', label = "Yield strain")

    plt.xlabel("Arc length [mm]")
    plt.ylabel("Microstrain [-]")
    #plt.title("Strain measurement "+ load_step_ext[count] + "mm extension ")
    plt.grid()
    plt.ylim(-16000, 6000)
    plt.xlim(0, 1100)
    plt.xticks(np.arange(0, 1200, 100))
    plt.yticks(np.arange(-16000, 8000, 2000))

    plt.legend()
    plt.show()

    # Average of span locations due to In and out
    strainIn1 = (Cinter(interval1) + Dinter(interval1))/2
    strainOut1 = (Ainter(interval1) + Binter(interval1))/2

    strainIn2 = (Cinter(interval2) + Dinter(interval2)) / 2
    strainOut2 = (Ainter(interval2) + Binter(interval2)) / 2

    strainIn3 = (Cinter(interval3) + Dinter(interval3)) / 2
    strainOut3 = (Ainter(interval3) + Binter(interval3)) / 2

    strainIn4 = (Cinter(interval4) + Dinter(interval4)) / 2
    strainOut4 = (Ainter(interval4) + Binter(interval4)) / 2

    # Axial strain
    axial_strain1 = (strainIn1 + strainOut1) / 2
    axial_strain2 = (strainIn2 + strainOut2) / 2
    axial_strain3 = (strainIn3 + strainOut3) / 2
    axial_strain4 = (strainIn4 + strainOut4) / 2

    col = "0.35"
    plt.plot(interval1*1000, axial_strain1, color =col, label = "Experiment")
    plt.plot(interval2*1000, axial_strain2, color =col)
    plt.plot(interval3*1000, axial_strain3, color =col)
    plt.plot(interval4*1000, axial_strain4, color =col)
    plt.plot(FEMx, (np.array(FEMaxial)-np.array(FEMaxzero)), "--", color = col, label = "FEM")
    plt.plot(np.array(stiffeners)*1000, [0, 0, 0, 0], "o", label='Stiffeners')

    plt.xlabel("Arc length [mm]")
    plt.ylabel("Microstrain [-]")
    #plt.title("Axial strain "+ load_step_ext[count] + "mm extension ")
    plt.grid()
    plt.ylim(-3200, 2800)
    plt.xlim(0, 1100)
    plt.xticks(np.arange(0, 1200, 100))
    plt.yticks(np.arange(-3200, 3200, 400))
    plt.legend()
    plt.show()
    # Bending strain
    bending_strain1 = (-strainIn1 + strainOut1) / 2
    bending_strain2 = (-strainIn2 + strainOut2) / 2
    bending_strain3 = (-strainIn3 + strainOut3) / 2
    bending_strain4 = (-strainIn4 + strainOut4) / 2

    plt.plot(interval1*1000, bending_strain1, color =col, label = "Experiment")
    plt.plot(interval2*1000, bending_strain2, color =col)
    plt.plot(interval3*1000, bending_strain3, color =col)
    plt.plot(interval4*1000, bending_strain4, color =col)
    plt.plot(FEMx, (np.array(FEMbending)-np.array(FEMbendzero)), "--", color=col, label = "FEM")
    plt.plot(np.array(stiffeners)*1000, [0, 0, 0, 0], "o", label='Stiffeners')

    plt.xlabel("Arc length [mm]")
    plt.ylabel("Microstrain [-]")
    #plt.title("Bending strain "+ load_step_ext[count] + "mm extension ")
    plt.grid()
    plt.ylim(-5000, 5000)
    plt.xlim(0, 1100)
    plt.xticks(np.arange(0, 1200, 100))
    plt.yticks(np.arange(-5000, 5500, 1000))
    plt.legend()
    plt.show()

    count += 1
