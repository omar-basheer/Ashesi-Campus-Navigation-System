import cv2
import matplotlib.pyplot as plt
import numpy as np
image1 = cv2.imread('AerialView.jpg')

image = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
# px = image[651:700,140:160, 1] = 0
# image[651:700,140:160, 2] = 0
#
# print(px)
a = np.array([[(50, 635),(116, 666),(220, 605)]])
b = np.array([[(220, 605),(278,490)]])

SportsCentreToServiceCentre = np.array([[(458,151),(416,196),(470,240),(435,278)]])
ServiceCentreToSportsCentre = np.array([[(435,278),(470,240),(416,196),(458,151)]])

ServiceCentretoEngineeringWorkshop = np.array([[(435,278),(388,334)]])
EngineeringWorkShopToServiceCentre = np.array([[(388,334),(435,278)]])

EngineeringWorkShopToHealthCenter = np.array([[(388,334),(355,378)]])
HealthCenterToEngineeringWorkShop = np.array([[(355,378),(388,334)]])

HealthCentertoFablab = np.array([[(355,378),(318,420)]])
FablabtoHealthCenter = np.array([[(318,420),(355,378)]])


FablabtoGreenGate = np.array([[(318,420),(222,606)]])
GreenGatetoFabLab = np.array([[(222,606),(318,420)]])

GreenGatetoKingEngineering = np.array([[(222,606),(278,652),(308,663)]])
KingEngineeringtoGreenGate = np.array([[(308,663),(278,652),(222,606)]])

GreenGatetoWarrenLibrary = np.array([[(222,606),(278,652),(270,689)]])
WarrenLibrarytoGreenGate = np.array([[(270,689),(278,652),(222,606)]])


KingEngineeringtoNutorHall = np.array([[(308,663),(390,708)]])
NutorHalltoKingEngineering = np.array([[(390,708),(308,663)]])


NutorHaltoTheHive = np.array([[(390,708),(426,720),(477,724)]])
TheHivetoNutorHall = np.array([[(477,724),(426,720),(390,708)]])


WarrenLibraryToAptHall = np.array([[(270,689),(283,706)]])
AptHallWarrenLibraryto = np.array([[(283,706),(270,689)]])

WarrenLibraryToRadichelHall = np.array([[(270,689),(218,727),(243,745)]])
RadichelHalltoWarrenLibrary = np.array([[(243,745),(218,727),(270,689)]])

RadichelHallToJackSonHall = np.array([[(245,745),(269,755),(276,741)]])
JackSonHalltoRadichelHall = np.array([[(276,741),(269,755),(245,745)]])

JacksonHallToFoundersPlaza = np.array([[(276,741),(256,783)]])
FoundersPlazatoJacksonHall = np.array([[(256,783),(276,741)]])

RadichelHallToFoundersPlaza = np.array([[(243,745),(270,752),(256,783)]])
FoundersPlazatoRadichelHall = np.array([[(256,783),(270,752),(243,745)]])

CollinsCourtyardToAptHall = np.array([[(261,680),(286,698)]])
AptHalltoCollinsCourtyard = np.array([[(286,698),(261,680)]])

CollinsCourtyardtoDatabankFoundationHall = np.array([[(261,680),(284,701),(316,715),(302,733),(322,746)]])
CollinsCourtyardtoDatabankFoundationHall = np.array([[(322,746),(302,733),(316,715),(284,701),(261,680)]])

CollinsCourtyardtoAshesiBookShop = np.array([[(261,680),(284,701),(325,713),(326,708),(347,715)]])
AshesiBookShoptoCollinsCourtyard = np.array([[(347,715),(326,708),(325,713),(284,701),(261,680)]])

UniversityCheckpointtoMunchies = np.array([[(54,633),(127,670),(145,694),(182,794),(200,828),(221,855),(264,887),(301,908),(362,920),(421,942),(426,954),(386,971)]])
MunchiestoUniversityCheckpoint = np.array([[(386,971),(426,954),(421,942),(362,920),(301,908),(264,887),(221,855),(200,828),(182,794),(145,694),(127,670),(54,633)]])

UniversityCheckpointtoFoundersPlaza = np.array([[(54,633),(127,670),(145,694),(180,774),(257,813)]])
FoundersPlazatoUniversityCheckpoint = np.array([[(257,813),(180,774),(145,694),(127,670),(54,633)]])

TharcherAboreteumToGreenGate = np.array([[(154,647),(175,633),(222,606)]])
GreenGatetoTharcherAboretum = np.array([[(222,606),(175,633),(154,647)]])

UniversityCheckpointToTharcherAboreteum = np.array([[(54,633),(115,661),(130,660),(175,633)]])
TharcherAboreteumtoUniversityCheckpoint = np.array([[(175,633),(130,660),(115,661),(54,633)]])

list = [JacksonHallToFoundersPlaza]
#list = [FoundersPlazatoRadichelHall,RadichelHalltoWarrenLibrary,WarrenLibrarytoGreenGate,GreenGatetoFabLab,FablabtoHealthCenter,HealthCenterToEngineeringWorkShop,EngineeringWorkShopToServiceCentre,ServiceCentreToSportsCentre]
#list = [SportsCentreToServiceCentre,ServiceCentretoEnginerringWorkshop,EngineeringWorkShopToHealthCenter,HealthCentertoFablab,
        #FablabtoGreenGate, GreenGatetoWarrenLibrary,WarrenLibraryToRadichelHall,RadichelHallToFoundersPlaza]
array = list[0]
for i in range (len(list)-1):
    print("Array befor: ", array)
    array = np.append(array,list[i+1],axis=1)
    print("Array after: ",array)

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
# cv2.imshow("s:",image)
#
# plt.imshow(image)
# plt.show()
cv2.imshow("Map", image1)
cv2.waitKey(1000000)
cv2.destroyAllWindows()