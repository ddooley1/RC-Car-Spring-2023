# RC-Car-Spring-2023
			
On startup, the scripts needed to run the RC car should automatically open up. 
If for some reason you dont want the scripts operating on startup, modify the "/etc/rc.local"
file, or I guess you could just delete the script. 

The RC car can be controlled via PS3 controller (specifically the Mad Giga one in the lab, but others should work fine)
Uses the left & right triggers to accelerate the left & right sides of the wheels, and uses the left & right bumpers to reverse.

All of the code needed for the RC car to actually run is on the RCcar.py file on the desktop.

If for whatever reason you need to kill the program, the select button kills the motors.

Controls can be modified by editing the "miniCar.lyt" file in QJoyPad, just make sure you change the python code accordingly!
