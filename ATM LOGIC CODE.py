# Data
name = [
    "Rohan Murthy", "Rohini Patil",
    "Kamlesh Jadhav", "Karishma Doke",
    "Karim Khan", "Karim Saif"
]

acc_no = [
    3444500001, 3444500002,
    3444500003, 3444500004,
    3444500005, 3444500006
]

acc_bal = [8000, 7680, 0, 0, 75000, 6900]

record = []

# Display
def display_accounts():
    for i in range(len(acc_no)):
        print(f"""
Account Number : {acc_no[i]}
Account Holder : {name[i]}
Balance        : {acc_bal[i]}
""")

    print("Zero balance accounts:", acc_bal.count(0))
    print("Total Cash:", sum(acc_bal))
    print("Max Balance:", max(acc_bal))
    print("Min Balance:", min(acc_bal))

# Transaction Logic
def transact():
    number = int(input("Enter Account Number: "))

    if number not in acc_no:
        print("Invalid account number!")
        return

    pos = acc_no.index(number)
    amount = int(input("Enter Amount: "))

    cash_opt = int(input("""
Select option:
1. Deposit
2. Withdraw
"""))

    if cash_opt == 1:
        acc_bal[pos] += amount
        print("Deposit successful")
    elif cash_opt == 2:
        if acc_bal[pos] >= amount:
            acc_bal[pos] -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
    else:
        print("Invalid option")

# Add Account
def add_account():
    number = acc_no[-1] + 1
    acc_name = input("Enter Name: ")

    name.append(acc_name)
    acc_no.append(number)
    acc_bal.append(500)

    print("Account added successfully")
    display_accounts()

# protect the data
def protect_data():
    record.clear()
    for i in range(len(name)):
        record.append((name[i], acc_no[i], acc_bal[i]))

    print("Protected Data:")
    print(tuple(record))

# Menu Logic
def bank():
    while True:
        select = int(input("""
Welcome To BOI
1. Display accounts
2. Add account
3. Transaction
4. Protect account details
5. Exit
Select option: """))

        if select == 1:
            display_accounts()
        elif select == 2:
            add_account()
        elif select == 3:
            transact()
        elif select == 4:
            protect_data()
        elif select == 5:
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid selection")

# ---------- Run ----------
bank()

