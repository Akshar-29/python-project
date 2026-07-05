print("Welcome to the Interactive Personal Data Collector!\n")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav_num = int(input("Please enter your favourite number: "))

print("\nThank you! Here is the information we collected:\n")
print("Name: ",name," (Type:",type(name),", Memory Address: ",id(name),")",sep = "")
print("Age: ",age," (Type:",type(age),", Memory Address: ",id(age),")",sep = "")
print("Height: ",height," (Type:",type(height),", Memory Address: ",id(height),")",sep = "")
print("Favourite Number: ",fav_num," (Type:",type(fav_num),", Memory Address: ",id(fav_num),")",sep = "")

birth_year = 2026 - age
print("Your birth year is approximately: ",birth_year," (based on your)", age,")\n",sep = "")

rounded_height = int(height)
print("Your rounded height is:",rounded_height,"\n")

print("Thank you for using the Personal Data Collector. Goodbye!")
