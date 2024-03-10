# Next, design a program that creates a Car object then calls the accelerate method five times. 
# After each call to the accelerate method, get the current speed of the car and display it. 
# Then call the brake method five times. After each call to the brake method, get the current speed of the car and display it.

import CarClass as c
mycar = c.Car('hongqi','china')

mycar.accelerate()
speed_now = mycar.get_speed()
print(f'now speed is {speed_now}.')

mycar.accelerate()
speed_now = mycar.get_speed()
print(f'now speed is {speed_now}.')

mycar.accelerate()
speed_now = mycar.get_speed()
print(f'now speed is {speed_now}.')

mycar.accelerate()
speed_now = mycar.get_speed()
print(f'now speed is {speed_now}.')

mycar.accelerate()
speed_now = mycar.get_speed()
print(f'now speed is {speed_now}.')

mycar.brake()
speed_now = mycar.get_speed()
print(f'now speed is {speed_now}.')

mycar.brake()
speed_now = mycar.get_speed()
print(f'now speed is {speed_now}.')

mycar.brake()
speed_now = mycar.get_speed()
print(f'now speed is {speed_now}.')

mycar.brake()
speed_now = mycar.get_speed()
print(f'now speed is {speed_now}.')

mycar.brake()
speed_now = mycar.get_speed()
print(f'now speed is {speed_now}.')

# for i in range(5):
#     mycar.accelerate()
#     speed_now = mycar.get_speed()
#     print(f'now speed is {speed_now}.')
# for i in range(5):
#     mycar.brake()
#     speed_now = mycar.get_speed()
#     print(f'now speed is {speed_now}.')
