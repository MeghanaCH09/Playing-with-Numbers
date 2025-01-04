largenum=int(input("Enter the large number: "))
smallnum=int(input("Enter the small number: "))

while (smallnum):
    number=smallnum
    smallnum=largenum%smallnum
    largenum=number

print(f"The HCF is {largenum}")