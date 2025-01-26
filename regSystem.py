import os
import difflib
if not os.path.exists("user_info.txt"):
    with open("user_info.txt", "w") as file:
        pass

print("Hello! Welcome to this simple Registration System \n")
while True:
    print("Please select an option below:")
    print("1. Create account\n2. Login\n3. Delete Account\n4. Exit")

    userInp = input("--> ")
    if userInp == "1":
        username = input("Username: ")
        while True:
            passwd = input("New password: ")
            confirm = input("Confirmation password: ")
            if passwd == confirm:
                print("\nUser created successfully.\n")
                break
            else:
                print("Both password did not mach. Try again")
                continue
        with open("user_info.txt", "a") as file:
            file.write(username)
            file.write("\n")
            file.write(passwd)
            file.write("\n")

    elif userInp == "2":
        username = input("Username: ")
        passwd = input("Password: ")
        

    elif userInp == "3":
        username = input("Username: ")
        passwd = input("Password: ")
        while True:
            inp = input("Are you sure you want to delete your account (y/n): ")
            inp.strip().lower()
            if inp == "y" or inp == "yes":
                with open("user_info.txt", "r") as file:
                    items = file.readlines()
                    li = list(items)
                li.remove(f"{username}\n")
                li.remove(f"{passwd}\n")
                with open("user_info.txt", "w") as file:
                    file.write("".join(li))
                print("User deleted successfully")
                break
            else:
                print("Your account was not deleted.")
                break
    elif userInp == "4":
        break
    else:
        print("Invalid Input!")

a = 2
b = 2
print(a == b)
