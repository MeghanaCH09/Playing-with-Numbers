def findlcm(a,b):
    lcm=max(a,b)

    while lcm%a!=0 or lcm%b!=0:
        lcm+=1
    
    return lcm

largenum=int(input("Enter the large number: "))
smallnum=int(input("Enter the small number: "))

print(f"The LCM of {largenum} and {smallnum} is {findlcm(largenum, smallnum)}")