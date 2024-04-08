users = {'a': 'a', 'user2': 'password2', 'user3': 'password3'}

username = input("Enter your username: ")
password = input("Enter your password: ")

if username in users and users[username] == password:
    print("Login successful!")
    loged_user = username
else:
    exit("Invalid username or password. Please try again.")