a = int(input("nilai a :"))
b = int(input("nilai b :"))
c = int(input("nilai c :"))
D = (b**2)-(4*a*c)
x1 = (-b+D**(1/2))/2*a
x2 = (-b-D**(1/2))/2*a
if D < 0:
    print("Fungsi tersebut tidak memiliki akar riil")
elif D > 0:
    print("Akar akar dari persamaan tersebut adalah",x2,"dan",x1)
else:
    print("Fungsi teersebut memiliki angka kembar yaitu",x1)