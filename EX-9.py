a=int(input("enter the maths mark:"))
b=int(input("enter the physics mark:"))
c=int(input("enter the chemistry mark:"))
d=int(input("enter the computer science mark:"))
tot=(a+b+c+d)
avg=(tot/4)
print("total=",tot)
print("aggregate=",avg)
if(avg>75):
    print("Grade= Distinction")
elif(75>avg and avg>=60):
    print("Grade= First Division")
elif(60>avg and avg>=50):
    print("Grade= Second Division")
elif(50>avg and avg>=40):
    print("Grade= Third Division")
else:
    print("Grade= Fail")
    
     
    
