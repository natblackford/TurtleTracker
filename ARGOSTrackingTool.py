#------------------------------------------------------------------------------------

# ARGOSTrackingTool.py
# Description: This tool reads in raw ARGOS tracking data and allows users 
#   to view coordinates for turtle location by inputting dates. It filters
#   out lower quality ARGOS points. 
#
# Author: Nat Blackford (nsb32@duke.edu)
# Date: 10/2/2023
#------------------------------------------------------------------------------------

#Create a variable pointing to the data file
file_name = './data/raw/sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read the file as single lines
lineString = file_object.readline()

#Iterate through lines
while lineString:
    #see if there is data
    if lineString[0] in  ("#","u"):
        lineString = file_object.readline()
        continue #if no data, skip to next line
    
    #Split the string into a list of data items
    lineData = lineString.split()

    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    #Print the location of sara
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

    #skip to next line
    lineString = file_object.readline()

# Close the file
file_object.close()