password = "python123"
user_password = input("Enter the password : ")
while user_password != password:
    print("wrong password")
    user_password = input("Enter the password: ")
    print("acces granted")
    
secret = 7
guess = int(input("Enter the guess : "))
while guess != secret:
    print("wrong guess")
    guess = int(input("Enter the guess : "))
    print("congratulations , you've guessed it")