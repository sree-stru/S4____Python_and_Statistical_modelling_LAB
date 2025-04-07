import math

radius = int(input("Enter the radius of cylinder\n"))
height = int(input("Enter the height of culinder\n"))

def surface_area(r,h) :
    sa = 2 * math.pi * r ( r + h )
    print("Surface Area = ",sa)
def volume( r,h) :
    vol = math.pi * r * r * h
    print("Volume = ",vol)

surface_area(radius , height)
volume(radius , height)
