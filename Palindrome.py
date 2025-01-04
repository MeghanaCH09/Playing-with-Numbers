number = int(input("Enter a number:"))
orgnum=number
revnum=0

while number>0:
    digit=number%10
    revnum=revnum*10+digit
    number//=10

if orgnum==revnum:
    print(f"{orgnum} is a Palindrome number")
else:
    print(f"{orgnum} is not a Palindrome number")