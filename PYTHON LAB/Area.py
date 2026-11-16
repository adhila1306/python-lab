from graphics.rectfn import*
from graphics.cirfn import*
from graphics.Dgraphics.sphfn import*
from graphics.Dgraphics.cubfn import*
l=int(input("enter length:"))
b=int(input("enter bredth:"))
print("rectangle area=",RectArea(l,b))
print("rectangle perimeter=",RectPerimeter(l,b))

r=int(input("enter radiuds of circle:"))
print("circle area=",CirArea(r))
print("circle perimeter=",CirPerimeter(r))

r=int(input("enter radius of sphere:"))
print("sphere area=",SpArea(r))
print("sphere volume=",SpPerimeter(r))

l=int(input("enter cuboid length:"))
b=int(input("enter cuboid bredth:"))
h=int(input("enter cuboid height:"))
print("cuboid area=",CubArea(l,b,h))
print("cuboid perimeter=",CubPerimeter(l,b,h))
