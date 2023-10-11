from cmath import sqrt


print("finding the distance between points")
xa=int(input("Xa= "))
ya=int(input("Ya= "))
xb=int(input("Xb= "))
yb=int(input("Yb= "))
AB=sqrt((xb-xa)**2+(yb-ya)**2)
print("First point A({0},{1}) and B({2},{3}), distanse AB={4}".format(xa,ya,xb,yb,f"{AB:.3f}"))