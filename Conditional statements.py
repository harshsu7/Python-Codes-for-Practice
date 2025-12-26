upi_id = input("Enter UPI ID:")
bank_bal= float(input("Enter bank balance:"))
if upi_id=="sid@okhdfcbank" or upi_id=="sid@okicici" and bank_bal>=1000:
 print("Transaction Valid")
 pin= input( "Enter UPI pin:")
 if pin == "3452":
  print("Payment processed")
 else: 
    print("Invalid pin")
else:
  print("Transaction Invalid")