def calculat(Number1 , Opration , Number2):
    if (Opration == '+'):
      return Number1 + Number2
    elif (Opration == '-'):
        return Number1 - Number2
    elif (Opration == '*'):
        return Number1 * Number2
    elif (Opration == '/'):
        return Number1 / Number2
    elif (Opration == '^'):
        return Number1 ** Number2
    else :
        return "Your opration is false"

    
while True:
     Number1 = int(input("Please Enter Your First Number:"))
     Opration = input("Please Enter your Opration:")
     Number2 = int(input("Please Enter Your Second Number:"))
     print("Result :" ,calculat(Number1,Opration,Number2))

     if input("Do you wanna Continue?  (y/n)").lower() !='y':
       break
