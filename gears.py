import math
import matplotlib.pyplot as plt

# gear ratios from https://www.automobile-catalog.com/auta_details1.php#gsc.tab=0
# tire circumference is 1.99334 meters for a honda civic

RPM_X = [] # new empty list
starting_RPM = 1000 # data from manufacturer starts here

while starting_RPM <= 6700:
    RPM_X.append(starting_RPM)
    starting_RPM += 100

# formula for tire rpm and car speed
# Engine rpm / transmission gear /axle gear(final drive) = tire rpm
# Tire circumference in meters x tire rpm = meters per minute
# Meters per minute x 0.03728283 = mph
    
# this list provides the gear ratios [0] is gear 1
gearRatios = [3.142, 1.869, 1.235, 0.948, 0.727]
finalDrive = 4.294
circumference = 1.99334
finalSpeeds = []
# tireRPM = 

for gears in gearRatios:
    # print(gears)
    speed = []
    for RPM in RPM_X:
        tireRPM = RPM / gears / finalDrive
        metersPerMinute = circumference * tireRPM
        speed.append(round(metersPerMinute * 0.03728283, 2))
    finalSpeeds.append(speed)

newFile = "speed_data.txt"

gearNumber = 1
with open(newFile, "w") as file:
    file.write("RPM Values Tested \n")
    file.write(str(RPM_X) + "\n\n")
    for lists in finalSpeeds:
        file.write(f"Speeds in MPH for Gear {gearNumber} \n")
        gearNumber += 1
        file.write(str(lists) + "\n\n")

gearNumber = 1
for mph in finalSpeeds:
    plt.plot(RPM_X, mph, label = f"Gear {gearNumber}")
    gearNumber += 1
plt.grid(True)
plt.xlabel("RPM")
plt.ylabel("MPH")
plt.legend()
plt.show()