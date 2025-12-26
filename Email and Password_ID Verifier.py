import re
import string


while True:
    FirstName = input('Enter your First Name: ')
    if FirstName.isalpha() and FirstName.istitle():
        print("Entered firstname is:", FirstName)
        break
    else:
        print("Invalid First Name")


while True:
    LastName = input('Enter your Last Name: ')
    if LastName.isalpha() and LastName.istitle():
        print("Entered lastname is:", LastName)
        break
    else:
        print("Invalid Last Name")


while True:
    Contact = input('Enter your Contact Number: ')
    if Contact.isdigit() and len(Contact) == 10:
        print("Entered Contact Number is:", Contact)
        break
    else:
        print("Invalid Contact Number! Must be 10 digits.")


while True:
    email = input('Enter email (xyz@anywhere.com): ')
    if re.match(r'^[\w\.-]+@[a-zA-Z0-9\.-]+\.[a-zA-Z]{2,}$', email):
        print("Entered email is:", email)
        break
    else:
        print("Invalid email format!")


while True:
    userName = input('Enter UserName: ')
    if userName.isidentifier():
        print("Entered userName is:", userName)
        break
    else:
        print("Invalid Username! No spaces, must start with a letter or _")


pattern = re.compile(r'^@[\w]+_\d+$')

while True:
    password = input('Enter password: ')
    if pattern.match(password):
        print("Entered password is:", password)
        break
    else:
        print("""
Invalid password format!
Rules:
- Must start with @
- Must contain _
- Must end with digits
Example: @Pass_word123
""")


lastMail = f"""
User {FirstName} {LastName},
Your email {email} has been successfully registered!
"""
print(lastMail)
