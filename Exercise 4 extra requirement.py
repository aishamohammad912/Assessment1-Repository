#List of countires and their capitals
countires=("France","Netherland","germany","Italy","Spain","United kingdom","Sweden","Norway","portugal")
capitals=("Paris","Amsterdam","Berlin","Rome","Madrid","London","Brussel","Stockholm","Oslo","Lisbon")

#loop through countries and capitals
for i in range (len(countires)):
    #Ask the user for capital of the country
    answer=input (f"what is the capital of {countires[i]}?").strip()

    #check if the answer is correct or not
    if answer.lower()==capitals[i].lower():
        print("Correct!\n")
    else:
        print(f"Wrong!The answer is {capitals[i]}.\n")



    