x = int(input("enter any number: "))
match x:
    case 0:
        print("The value of x is zero.")
    case 4:
        print("The value of x is four.")
y = int(input("Enter your score: "))
match y:
    case 7:
        print("your score is 7.")
# agr koi bhi number ho (use humne variable 'num' bol diya) aur woh 90 nahi hai
    case num if num != 90:
        print(num, "90 ke equal nahi hai!")
           
        