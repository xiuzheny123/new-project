def main():
    user_choice = input("Select:\n\t1 register \n\t2 login\n")
    if user_choice == "1":
        register()
    elif user_choice == "2":
        login()


def register():
    while True:
        username = input("Enter new username: ")
        

        with open("users.txt","r") as file:
            taken = False
            for line in file:
                stored_user,_ =line.strip().split(",")
                if stored_user ==username:
                    print("Username already exists. Try another one")
                    taken = True
        if taken:
            continue
        password = input("Enter new password: ")

        with open("users.txt","a") as file:
            file.write(f"{username},{password}\n")
        print("Registration successful! please login now")
        break
def login():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        with open("users.txt","r") as file:
            for line in file:
                stored_user,stored_pass =line.strip().split(",")
                if stored_user==username and stored_pass==stored_pass:
                    print("Login successful! Welcome,", username)
                    return
        print("Invalid username or password")
        








if __name__=="__main__":
    main()

    
            
