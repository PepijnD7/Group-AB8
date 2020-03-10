Experimental strain data:

Measurements2014_05_22.txt contains the strain in the axial direction of the optical fiber. The data is ordered as described in the header of the file.

The fiber runs on the outside and inside of the leading edge at two different span locations. The calibration between the fiber location and the real 
location is given in the contourX_calibration.txt files. In ContourFigures these contours are shown on the leading edge.


FEM strain data:
shell_loadstepX_disp.out and shell_loadstepX_str.out contain the displacement and strain data from the finite element model for load step X, respectively. 
The displacement data contains a counter number, the node number, the x,y,z coordinates, and displacements in x,y,z direction of the nodes of the FEM. 
The strain data contains the node number and the x,y,z,xy,yz,xz engineering strain data of the nodes of the FEM in a global reference frame. 
This data needs to be modified such that it can be compared to the strain measured with the optical fiber.


Image data:
The Images folder contains pictures of the leading edge at different actuator displacements. It starts at 0mm and runs up to 39.2mm in steps of 2.5 mm. 
Picture G20 is again the initial condition.
The FEM load steps correspond with the pictures and strain measurements as follows:
loadstep 1 => picture 20 => strain measurement 1
loadstep 2 => picture 5 => strain measurement 13
loadstep 3 => picture 9 => strain measurement 28
loadstep 4 => picture 14 => strain measurement 40
loadstep 5 => picture 19 => strain measurement 55


Force-displacement data:
The displacement and force data in time is given in terms of the voltage of the power source and the voltage of the current sensor. 
To determine the displacement in cm, the voltage from the power source needs to be divided by 2. 
To determine the actuation force, the relation between the current sensor voltage and current needs to be 
determined using the calibration data in CurrentSensorCalibration3.txt and CurentVoltageReading3.txt and consequently the datasheet of the 
Linak LA23 24V B actuator can be used to find the actuation force.

The femForceDisplacement.txt file contains the force displacement points that were obtained using FEM.
Additional data:
The ModelData folder contains data on the stiffener locations and the target airfoil shape.
