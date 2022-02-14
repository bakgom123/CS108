"""CS 108 - Lab 4.1

This program lets the user input
1. current temperature (in degrees Fahrenheit), and 2. wind speed (in miles/h).
And use the National Weather Service formula to compute the wind-chill temperature
Finally, depending on the wind-chill temperature,
it tells the user how many layers of clothes should they put on or should they stay at home.

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

t = float(input('Temperature: '))
v = float(input('Wind speed: '))
wc_temp = 35.74 + 0.6215*t - 35.75*(v**0.16) + 0.4275*t*(v**0.16)

if v < 2 or t < -58 or t > 41:
    print('Invalid input')
else:
    print('Wind chill:',wc_temp)
    if wc_temp < -40:
        print('Stay home!')
    elif -40 <= wc_temp < -10:
        print('Four layers')
    elif -10 <= wc_temp < 20:
        print('Three layers')
    elif 20 <= wc_temp < 40 :
        print('Two layers')
    else:
        print('One layer')
    

    
    
    
    
    
    
    
    
    
    
    