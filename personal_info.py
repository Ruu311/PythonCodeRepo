print("==================================================")
print("              PERSONAL INFORMATION                ")
print("==================================================")

Name = "Rupam Kumari"
Age = 22
City = "Jamshedpur"
Hobby = "Playing Guitar"

#Get user input

Favorite_Food = input("Please enter your favorite Dish: ")
Favorite_Color = input("Please enter your favorite color: ")

#Validation Check if the User Input is Blank for Favorite Food

while Favorite_Food == "":
    print("Please enter a valid food!")
    Favorite_Food = input("Please enter your favorite Dish: ")
    

#Validation Check if the User Input is Blank for Favorite Color

while Favorite_Color == "":
    print("Please enter a valid Color!")
    Favorite_Color = input("Please enter your favorite Color: ")

# Calculate age in months
age_in_months = Age * 12

print("==================================================")
print("              PERSONAL INFORMATION                ")
print("==================================================")

print(f"Name: {Name}")
print(f"Age: {Age} years ({age_in_months} months old)")
print(f"City: {City}")
print(f"Hobby: {Hobby}")
print()
print(f"Favorite Food: {Favorite_Food}")
print(f"Favorite Color: {Favorite_Color}")

      
# Goodbye message
#----------------------------------------------------------
print("==================================================")
print("Thanks for using this program!")
#---------------------------------------------------------
