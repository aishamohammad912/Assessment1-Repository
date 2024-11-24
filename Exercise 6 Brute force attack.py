#The correct password
correct_password="12345"

#Use of while loop tp repeatedly ask password from user
while True:
    user_input=input("Enter the password:")
    if user_input==correct_password:
     print("Access granted!")
    break# Exist the loop if answer is correct
else:
     print("Wrong password . Try again!.")