num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num,"x",i,"=",num*i)
    
for i in range(10,0,-1):
    print(i)
print("Blast off")
num = int(input("Enter a number : "))
total = 0
for i in range (1,num+1):
    total = total + i
    print("sum = ",total)