pi = 3.142
radius = 4
area = pi * (radius**2)
print(area)

pi = 22/7
print("The new branch of the code with a new value of pi", pi)
area1 = pi * (radius**2)
print("The new value of area becomes ", area1)
diff = area1 - area
print("The difference of value is ", diff)
uncer = (diff / area1)*100
print("Percentage uncertainity is ", uncer, "which is negligible")
