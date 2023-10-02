#------------------------------------------------------------------------------------
# ARGOSTrackingTool.py
# Description: This tool reads in raw ARGOS tracking data and allows users 
#   to view coordinates for turtle location by inputting dates. It filters
#   out lower quality ARGOS points. 
#
# Author: Nat Blackford (nsb32@duke.edu)
# Date: 10/2/2023
#------------------------------------------------------------------------------------

#Parse Data
lineString = "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"
#print(lineString[0])

lineData = lineString.split(    )
#print(lineData[0])
#print(lineData)
#assigning variables to objects in the list

ob_id = lineData[0]
ob_date = lineData[2]
ob_lc= lineData[3]
ob_lat = lineData[5]
ob_lon = lineData[6]

#print(ob_lon)


