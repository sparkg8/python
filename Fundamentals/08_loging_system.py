"""
Loging system. Prompt the user to enter username: 'admin' and password: 'pass123'
If it is correct then print, login successful, if not, print loging failed
"""

user_name = input("Enter your user name: ")
pass_word = input("Enter password: ")

if user_name == 'admin' and pass_word == 'pass123':
    print("Loging successful...\n")
else:
    print("Information is not correct.\n") 