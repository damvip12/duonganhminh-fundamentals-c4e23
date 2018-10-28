action = input("Welcome to our shop , what do you want ? (C , R , U , D) : ")
items = ["T-shirt" , " Sweater"]

while action =="R" or action == "C" or action == "U" or action == "D" :
    if action == "R" :
        print("Our items :", *items , sep=" , ")
        action=input("What else do you want to do? Last action was R.      ")
    if action == "C":
        new_item = input("Enter new item :")
        items.append(new_item)
        print("Our items :", *items , sep=" , ")
        action = input("What else do you want to do? Last action was C.      ")
    if action =="U":
        i = int(input("Update position ?"))
        if i>3 :
            print("The number must be smaller than 4. Try again.")
            break
        else :
            new_item_updated = input("New item ?")
            items[i-1] = new_item_updated
            print(*items, sep=" , ")
            action = input("What else do you want to do? Last action was U.       ")
    if action == "D":
        i = int(input("Delete position ?"))
        items.pop(i-1)
        print("Our items :", *items , sep=" , ")
        print("Thanks for choosing us.")
        break
    


    
    else :
        print("Wrong action.Try again")
        break
else :
    print("Wrong action.Try again")
   