line="-"

print("+","-","*","**","/","**","%", "program ko bnd krne ke liye (exit) liho")
print(line*50)


#--------------------------------------------------------------------

while True:

    choice=input("enter your operator given below .")

    print(line*50)

    if  choice in["+","-","*","**","/","//","%","program ko bnd krne ke liye (exit) liho"]:

     num1=int(input("enter your first number :"))

     num2=int(input("enter your second number : "))

     print(line*50)
#---------------------------------------------------------------------


    if choice == "+":

        print(num1+num2)

        print(line*50)

#---------------------------------------------------------------------

    elif choice == "-":

        print(num1-num2)

        print(line*50)
#---------------------------------------------------------------------

    elif choice == "*":
        print(num1*num2)

        print(line*50)

#---------------------------------------------------------------------

    elif choice == "**":

        print(num1**num2)

        print(line*50)
#---------------------------------------------------------------------

    elif choice == "/":

        if num2==0:

            print("error not divided by 0: ")

            print(line*50)

        else:

            print(num1/num2)

            print(line*50)
#---------------------------------------------------------------------

    elif choice == "//":

        if num2==0:
            print("error not divided by 0:")

            print(line*50)

        else:
            print(num1//num2)

            print(line*50)
#---------------------------------------------------------------------

    elif choice=="exit":

        print("thanks for using this project version 2: ")

        print(line*50)
        break
#---------------------------------------------------------------------

    elif choice=="%":
        print(num1%num2)

        print(line*50)

#---------------------------------------------------------------------
    else:
        print("please choose a valid operator. ")
        print(line*50)
     