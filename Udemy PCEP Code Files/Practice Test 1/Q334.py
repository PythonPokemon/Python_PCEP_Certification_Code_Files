"""
You are an intern for ABC electric cars company.
You must create a function that calculates the average velocity
of their vehicles on a 1320 foot (1/4 mile) track.
Consider the following code.


distance = ???(input('Enter the distance travelled in feet'))
distance_miles = distance/5280  # convert to miles
 
time = ???(input('Enter the time elapsed in seconds'))
time_hours = time/3600  # convert to hours
 
velocity = distance_miles/time_hours
print('The average Velocity : ', velocity, 'miles/hour')
--------------------------------------------------------
The output must be as precise as possible.
What would you insert instead of ??? and ???

Richtige Antwort
float
float
"""

# distance = float(input('Enter the distance travelled in feet'))
distance = float('437723.42')  # Just for convenience
distance_miles = distance/5280

# time = float(input('Enter the time elapsed in seconds'))
time = float('1723.9')  # Just for convenience
time_hours = time/3600  # convert to hours

velocity = distance_miles/time_hours
print('The average Velocity : ', velocity, 'miles/hour')
# The average Velocity : 173.1236071486956 miles/hour


