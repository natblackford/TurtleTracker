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

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#creating dictionaries to hold date and location data
date_dict = {}
location_dict = {}

#Pretend we read one line of data from the file
for lineString in line_list:
    #see if there is data
    if lineString[0] in  ("#","u"):
        continue #if no data, skip to next line
    #Split the string into a list of data items
    lineData = lineString.split()

    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    #Add date and location to respective dictionaries
    date_dict[record_id] = obs_date
    location_dict[record_id] = (obs_lat, obs_lon)

    #Print the location of sara
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

#testing functionality
firstkey = list(location_dict.keys())[0]
print(firstkey)
print(location_dict[firstkey])
print(date_dict[firstkey])
print(date_dict['24719'])