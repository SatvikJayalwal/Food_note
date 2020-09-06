import os; os.system("cls")

f=open("Food_note.txt","w")

food=input("Enter your breakfast : ")
f.write("Breakfast :   ")
f.write(food.capitalize())
f.write("\n")
print("Succesfully added to file\n")

food=input("Enter your lunch : ")
food.upper()
f.write("Lunch     :   ")
f.write(food.capitalize())
f.write("\n")
print("Succesfully added to file\n")

food=input("Enter your dinner : ")
food.upper()
f.write("Dinner    :   ")
f.write(food.capitalize())
f.write("\n")
print("Succesfully added to file")