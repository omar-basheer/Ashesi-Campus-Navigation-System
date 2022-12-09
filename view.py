import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread('AerialView.jpg')

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# px = image[651:700,140:160, 1] = 0
# image[651:700,140:160, 2] = 0
#
# print(px)
a = np.array([[(50, 635),(116, 666),(220, 605)]])
b = np.array([[(220, 605),(278,490)]])

SportsCentreToServiceCentre = np.array([[(458,151),(416,196),(470,240),(435,278)]])
ServiceCentretoEnginerringWorkshop = np.array([[(435,278),(388,334)]])
EngineeringWorkShopToHealthCenter = np.array([[(388,334),(348,378)]])
HealthCentertoFablab = np.array([[(351,378),(318,420)]])
FablabtoGreenGate = np.array([[(318,420),(222,606)]])
GreenGatetoKingEngineering = np.array([[(222,606),(278,652)]])
GreenGatetoWarrenLibrary = np.array([[(222,606),(278,652),(276,680)]])
list = [SportsCentreToServiceCentre,ServiceCentretoEnginerringWorkshop,EngineeringWorkShopToHealthCenter,
        HealthCentertoFablab,FablabtoGreenGate,GreenGatetoWarrenLibrary]

for i in range (len(list)-1):
    array = list[0]
    array = np.append(array,list[i+1],axis=1)
    print("Array: ",array)

# start_point = (50, 635)
# # End coordinate, here (450, 450). It represents the bottom right corner of the image according to resolution
# end_point = (116, 666)
# # White color in BGR
# color = (0, 0, 255)
# # Line thickness of 9 px
# thickness = 5
# # Using cv2.line() method to draw a diagonal green line with thickness of 9 px
# image = cv2.line(image, start_point, end_point, color, thickness)
#
# start_point2 = (116, 666)
# # End coordinate, here (450, 450). It represents the bottom right corner of the image according to resolution
# end_point2 = (212, 612)
#
# image = image = cv2.line(image, start_point2, end_point2, color, thickness)
#cv2.drawContours(image, [a], 0, (255,255,255), 2)
cv2.polylines(image,
              array,
              isClosed = False,
              color = (0,0,230),
              thickness = 3)
#cv2.imshow("s:",image)

plt.imshow(image)
plt.show()
# cv2.imshow("Map", image)
# cv2.waitKey(1000000)
# cv2.destroyAllWindows()