#string list of names
names=["Jake","Zac","Ian","Ron","sam","Dave"]
search="sam"

# Asking user to input they want to search
search_term=input("Enter the name you want to seach for :")

# check if the name asked exist in the list
if search_term in names:
    print(f"Yes,{search_term}is in the list!")
else:
    print(f"NO,{search_term}is not in the list !")
