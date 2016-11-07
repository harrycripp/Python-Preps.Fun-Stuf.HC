#Write a program that asks you for your password.
#It then asks you to re-enter your password.
#If they are the same the message ‘access granted’ is displayed.
#If the passwords are not the same the message ‘access denied’ is displayed. 

password1 = input("Please enter your password:")
password2 = input("Please enter your passord again:")
if password1 == password2:
    print("Access Granted")
else:
    print("Access Denied")
