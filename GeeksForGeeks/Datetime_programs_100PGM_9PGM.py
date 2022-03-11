#Date time Program
#1.Python program to get Current Time
#MEthod1
from datetime import datetime
  
# now() method is used to
# get object containing 
# current date & time.
now_method = datetime.now()
  
# strftime() method used to
# create a string representing
# the current time.
#MEthod2
currentTime = now_method.strftime("%H:%M:%S")
print("Current Time =", currentTime)

from datetime import datetime
  
# Time object containing 
# the current time.
time = datetime.now().time() 
  
print("Current Time =", time)


#2.Get Current Date and Time using Python

import datetime 
    
# using now() to get current time 
current_time = datetime.datetime.now() 
    
# Printing value of now. 
print ("Time now at greenwich meridian is : "
                                    , end = "") 
print (current_time) 

#MEthod2
import datetime 

current_time = datetime.datetime.now()
print ("The attributes of now() are : ") 
    
print ("Year : ", end = "") 
print (current_time.year) 
    
print ("Month : ", end = "") 
print (current_time.month) 
    
print ("Day : ", end = "") 
print (current_time.day) 
    
print ("Hour : ", end = "") 
print (current_time.hour) 
    
print ("Minute : ", end = "") 
print (current_time.minute) 
    
print ("Second : ", end = "") 
print (current_time.second) 
    
print ("Microsecond : ", end = "") 
print (current_time.microsecond) 


#3.Python | Find yesterday’s, today’s and tomorrow’s date

from datetime import datetime, timedelta

presentday = datetime.now() # or presentday = datetime.today()
yesterday = presentday - timedelta(1)
tomorrow = presentday + timedelta(1)
print("Yesterday = ", yesterday.strftime('%d-%m-%Y'))
print("Today = ", presentday.strftime('%d-%m-%Y'))
print("Tomorrow = ", tomorrow.strftime('%d-%m-%Y'))

#4.Python program to convert time from 12 hour to 24 hour format

def convert24(str1):
      
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
          
    # remove the AM    
    elif str1[-2:] == "AM":
        return str1[:-2]
      
    # Checking if last two elements of time
    # is PM and first two elements are 12   
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
          
    else:
          
        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]
  
# Driver Code        
print(convert24("08:05:45 PM"))

#5.Python program to find difference between current time and given time

def difference(h1, m1, h2, m2):
      
    # convert h1 : m1 into
    # minutes
    t1 = h1 * 60 + m1
      
    # convert h2 : m2 into
    # minutes 
    t2 = h2 * 60 + m2
      
    if (t1 == t2): 
        print("Both are same times")
        return 
    else:
          
        # calculating the difference
        diff = t2-t1
          
    # calculating hours from
    # difference
    h = (int(diff / 60)) % 24
      
    # calculating minutes from 
    # difference
    m = diff % 60
  
    print(h, ":", m)
  
# Driver's code
if __name__ == "__main__":
      
    difference(7, 20, 9, 45)
    difference(15, 23, 18, 54)
    difference(16, 20, 16, 20)

#6.Python Program to Create a Lap Timer

import time  
  
# Timer starts
starttime=time.time()
lasttime=starttime
lapnum=1
  
print("Press ENTER to count laps.\nPress CTRL+C to stop")
  
try:
     while True: 
          input() 
   
          laptime=round((time.time() - lasttime), 2)  

          totaltime=round((time.time() - starttime), 2)  
   
          print("Lap No. "+str(lapnum)) 
          print("Total Time: "+str(totaltime))
          print("Lap Time: "+str(laptime))
            
          print("*"*20)
  
          lasttime=time.time()
          lapnum+=1

except KeyboardInterrupt:
     print("Done")

#7.Convert date string to timestamp in Python

import time
import datetime
  
  
string = "20/01/2020"
print(time.mktime(datetime.datetime.strptime(string,
                                             "%d/%m/%Y").timetuple()))


#8.How to convert timestamp string to datetime object in Python?

from datetime import datetime
    
timestamp = 1545730073
dt_obj = datetime.fromtimestamp(1140825600)
  
print("date_time:",dt_obj)
print("type of dt:",type(dt_obj))

#9.Find number of times every day occurs in a Year

import datetime
import calendar
  
def day_occur_time(year):
     
    # stores days in a week
    days = [ "Monday", "Tuesday", "Wednesday", 
           "Thursday",  "Friday", "Saturday",
           "Sunday" ]
     
    # Initialize all counts as 52
    L = [52 for i in range(7)]
     
    # Find the index of the first day
    # of the year
    pos = -1
    day = datetime.datetime(year, month = 1, day = 1).strftime("%A")
    for i in range(7):
        if day == days[i]:
            pos = i
             
    # mark the occurrence to be 53 of 1st day
    # and 2nd day if the year is leap year
    if calendar.isleap(year):
        L[pos] += 1
        L[(pos+1)%7] += 1
         
    else:
        L[pos] += 1
         
     
    # Print the days
    for i in range(7):
        print(days[i], L[i])
      
  
# Driver Code
year = 2019
day_occur_time(year)

