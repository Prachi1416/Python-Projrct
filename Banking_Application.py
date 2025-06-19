balance = 0

def check_balance():
    print('Total Balance in your Account is: ',balance)

def deposit_cash(d_amt):
    global balance
    balance = balance + d_amt
    print(d_amt,'Rs. deposited')

def withdraw_cash(w_amt):
    global balance
    if balance < 500:
        print('Insufficient Balance atleast 500 Rs mandatory in your account')
    elif w_amt <= balance:
        balance = balance - w_amt
        print(w_amt,'Rs. Withdraw')
    else:
        print('Insufficent Funds....')

while True:
    ch = int(input('\nENTER CHOICE:'\
                    '\n1. Deposit Cash' \
                    '\n2. Withdraw Cash' \
                    '\n3. Check balance' \
                    '\n4. Exit '))
    if ch == 1:
        print('---> 1. DEPOSIT CASH')
        d_amt = int(input('Enter Amount to Deposit: '))
        deposit_cash(d_amt)

    elif ch == 2:
        print('---> 2. WITHDRAW CASH')
        w_amt = int(input('Enter Amount to Withdraw: '))
        withdraw_cash(w_amt)

    elif ch == 3:
        print('---> 3. CHECK BALANCE')
        check_balance()

    elif ch == 4:
        print('---> 4. Exit')
        break

    else:
        print('---> iNVALID CHOICE')

