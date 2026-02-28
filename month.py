User_input=int(input("Enter a number between 1 and 12: "))
months=["january","february","March","April","May","June","July","August","september","October","November","December"]

if 1<=User_input<=12:
    print("Month:",months[User_input-1])
else:
    print("input is invalid")
