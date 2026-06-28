marks = int(input("Enter a number : "))
if marks>=90:
    print("Grade A")
elif marks>75:
    print("Grade B")
elif marks>50:
    print("Grade C")
elif marks>0:
    print("Grade D")
else:
    print("Didn't attempt")
    
train = int(input("How many hours did you train ? : "))
if train>=2:
    print("well done you trained",train,"hours")
else :
    print("do well again tomorrow ")
    
