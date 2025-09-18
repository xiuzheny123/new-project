def register():
    
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    with open("users.txt","r") as file:
        for line in file:
            stored_user,_ =line.strip().split(",")
            if stored_user ==username:
                print("Username already exists. Try another one")
                return 
        with open("users.txt","a") as file:
            file.write(f"{username},{password}\n")
        print("Registration successful! please login now")
        return
register()
    
            
