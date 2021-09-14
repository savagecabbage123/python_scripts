shop_name = input("What will your shop name be? \n")
if len(shop_name) > 20:
    print("this name is over the 20 character limit")
    print("try again")
    shop_name = input("What will your shop name be? \n")
print("\n" + shop_name)