# Rules for timing:
# Rice => 30
# Eba => 45
# Bread => 15
# Yam => 30
# Plantain => 25

# Algorithm for simple ordering system:
# - Let FM be the list of items on the menu 
# - Print “Welcome to MK’s Cuisine, Have a look at our tasty delicacies”
# - Display items in FM 
# - Prompt user to input their order from the menu
# - Assign user’s input to the variable called order
# - Search through FM  for order   
# - For i in FM : 
# -     if order == (FM[i]):
# -        print “Order taken. Please hold on          for ….minutes while your food is being prepared “
# -     else:
# -        Print “Sorry, that is currently not on our menu. Please place another order” 


# timing_rules = [30, 45, 15, 30, 25]
# timing

FM = ["eba, afang and chicken",
"eba, afang and beef",
"eba, afang and chevon",
"eba, afang and pork",
"eba, afang and fish",
"eba, egusi and chicken",
"eba, egusi and beef",
"eba, egusi and chevon",
"eba, egusi and pork",
"eba, egusi and fish",
"eba, white soup and chicken",
"eba, white soup and beef",
"eba, white soup and chevon",
"eba, white soup and pork",
"eba, white soup and fish",
"rice, stew and chicken",
"rice, stew and beef",
"rice, stew and chevon",
"rice, stew and pork",
"rice, stew and fish",
"rice, beans and chicken",
"rice, beans and beef",
"rice, beans and chevon",
"rice, beans and pork",
"rice, beans and fish",
"rice, pepper soup and chicken",
"rice, pepper soup and beef",
"rice, pepper soup and chevon",
"rice, pepper soup and pork",
"rice, pepper soup and fish",
"fufu, afang and chicken",
"fufu, afang and beef",
"fufu, afang and chevon",
"fufu, afang and pork",
"fufu, afang and fish",
"fufu, egusi and chicken",
"fufu, egusi and beef",
"fufu, egusi and chevon",
"fufu, egusi and pork",
"fufu, egusi and fish",
"fufu, white soup and chicken",
"fufu, white soup and beef",
"fufu, white soup and chevon",
"fufu, white soup and pork",
"fufu, white soup and fish",
"yam, egg and chicken",
"yam, egg and beef",
"yam, egg and chevon",
"yam, egg and pork",
"yam, egg and fish",
"yam, stew and chicken",
"yam, stew and beef",
"yam, stew and chevon",
"yam, stew and pork",
"yam, stew and fish",
"yam, beans and chicken",
"yam, beans and beef",
"yam, beans and chevon",
"yam, beans and pork",
"yam, beans and fish",
"yam, pepper soup and chicken",
"yam, pepper soup and beef",
"yam, pepper soup and chevon",
"yam, pepper soup and pork",
"yam, pepper soup and fish",
"bread, egg and chicken",
"bread, egg and beef",
"bread, egg and chevon",
"bread, egg and pork",
"bread, egg and fish",
"bread, stew and chicken",
"bread, stew and beef",
"bread, stew and chevon",
"bread, stew and pork",
"bread, stew and fish",
"bread, beans and chicken",
"bread, beans and beef",
"bread, beans and chevon",
"bread, beans and pork",
"bread, beans and fish",
"bread, pepper soup and chicken",
"bread, pepper soup and beef",
"bread, pepper soup and chevon",
"bread, pepper soup and pork",
"bread, pepper soup and fish",
"plantain, egg and chicken",
"plantain, egg and beef",
"plantain, egg and chevon",
"plantain, egg and pork",
"plantain, egg and fish",
"plantain, stew and chicken",
"plantain, stew and beef",
"plantain, stew and chevon",
"plantain, stew and pork",
"plantain, stew and fish",
"plantain, beans and chicken",
"plantain, beans and beef",
"plantain, beans and chevon",
"plantain, beans and pork",
"plantain, beans and fish",
"plantain, pepper soup and chicken",
"plantain, pepper soup and beef",
"plantain, pepper soup and chevon",
"plantain, pepper soup and pork",
"plantain, pepper soup and fish]"]

timing_rule = {"rice":30, "eba":45, "bread":15, "yam":30, "plantain": 25}
print("Welcome to MK's Cuisine, Have a look at our tasty delicacies")
for i in range(1,len(FM)+1):
    print(str(i)+": "+FM[i-1])
print("Enter your selected option between 1 - "+str(len(FM)))
customers_choice = int(input())
if customers_choice <= len(FM) or customers_choice >= 1:
    print("Your order "+FM[customers_choice-1]+" has been taken. Press N/n/no to cancel order or any key to proceed")
    confirmation = input()
    if confirmation == "N" or confirmation == "n" or confirmation == "No" or confirmation == "no" or confirmation == "NO":
        print("Order cancelled")
    else:
        print("Please hold on for ….minutes while your food is being prepared")
else:
    print("Sorry, that is currently not on our menu oooo. Please place another order")
