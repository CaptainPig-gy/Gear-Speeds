import math
import matplotlib.pyplot as plt

# gear ratios from https://www.automobile-catalog.com/auta_details1.php#gsc.tab=0
# tire circumference is 1.99334 meters for a honda civic

RPM_X = [] # empty list for RPM values
starting_RPM = 1000 # data from manufacturer starts here

# fills list with values from 1000 - 6700
while starting_RPM <= 6700:
    RPM_X.append(starting_RPM)
    starting_RPM += 100

# formula for tire rpm and car speed #
# Engine rpm / transmission gear /axle gear(final drive) = tire rpm
# Tire circumference in meters x tire rpm = meters per minute
# Meters per minute x 0.03728283 = mph
    
# this list provides the gear ratios [0] is gear 1
gearRatios = [3.142, 1.869, 1.235, 0.948, 0.727]
finalDrive = 4.294
circumference = 1.99334
finalSpeeds = [] # values will be used to graph later
# tireRPM = 

# goes through each ratio and rpm to find final speed
for gears in gearRatios:
    # print(gears)
    speed = [] # temporary list for each ratio 
    for RPM in RPM_X:
        tireRPM = RPM / gears / finalDrive
        metersPerMinute = circumference * tireRPM

        # appends final speeds to list for this ratio
        speed.append(round(metersPerMinute * 0.03728283, 2))
    
    # appends the full list from above to the final list that stores all values
    finalSpeeds.append(speed)

newFile = "speed_data.txt" # creates new file to output all speeds for user

gearNumber = 1
with open(newFile, "w") as file: # writes data to file
    file.write("RPM Values Tested \n")
    file.write(str(RPM_X) + "\n\n")
    for lists in finalSpeeds:
        file.write(f"Speeds in MPH for Gear {gearNumber} \n")
        gearNumber += 1
        file.write(str(lists) + "\n\n")

gearNumber = 1
for mph in finalSpeeds: # graph is plotted
    plt.plot(RPM_X, mph, label = f"Gear {gearNumber}")
    gearNumber += 1
plt.grid(True)
plt.xlabel("RPM")
plt.ylabel("MPH")
plt.title("Maximum speed of the Gears")
plt.legend()
plt.show()