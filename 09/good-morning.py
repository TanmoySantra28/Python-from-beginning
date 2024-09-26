#Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour.
import time
timestamp = time.strftime('%H:%M:%S') #get the current hour,min,sec
print("Current time = ",timestamp)
hour = int(time.strftime('%H'))
if(hour>=4 and hour<=10):
    print("Good Morning")
elif(hour>10 and hour<=14):
    print("Good Noon")
elif(hour>14 and hour<=17):
    print("Good Afternoon")
elif(hour>17 and hour<=19):
    print("Good Evening")
else:
    print("Good Night")