#Creating a dictionary 
month_days={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
#january,februray,march,april,may,june,july,august,september,october,november,december

#Asking user for month numbers
month_number=int(input("Enter the month number:"))

#Checking if the number is valid and print the corresponding number of days
if 1<=month_number<=12:
    print(f"The month{month_number}has {month_days[month_number]}days.")
else:
    print("Invalid number!.Enter a number between 1 and 12.")
