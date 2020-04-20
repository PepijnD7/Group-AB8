import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Measurements2014_05_22.txt", sep="\t", engine='python', header=4)
print(data.head())
print(data.shape)


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
# data[position of sensor][t] t is number of time step

#t = 32
#addings C and D data to plot

for t in range(79):
    x1_plot = []
    y1_plot = []

    x2_plot = []
    y2_plot = []

    for i in range(8):
        C = "C" + str(i)
        D = "D" + str(i)

        stressC = data[str(code_location[C])].iloc[t]
        stressD = data[str(code_location[D])].iloc[t]

        normal_stress = (stressC+stressD)/2
        x1_plot.append(actual_location[C])
        y1_plot.append(normal_stress)


    #adding A and B data to plot
    for i in range(3):
        A = "A"+str(i)
        B = "B" + str(i)

        stressA = data[str(code_location[A])].iloc[t]
        stressB = data[str(code_location[B])].iloc[t]

        normal_stress = (stressA+stressB)/2
        x2_plot.append(actual_location[A])
        y2_plot.append(normal_stress)

    plt.plot(x1_plot,y1_plot)
    plt.plot(x2_plot, y2_plot)
plt.show()