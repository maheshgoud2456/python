 #calculator 
a=float(input("enter no :"))
operator = input("enter + or - / or * or %")
b =float(input("enter no :"))
if (operator=="+"):
    ans = a+b
elif(operator=="-"):
    ans = a-b
elif(operator=="*"):
    ans = a*b
elif(operator=="%"):
    ans = a%b
else:
    ans = "invaild"
print(ans)
 



    


    


