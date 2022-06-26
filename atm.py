meteAccount= {
    "name": "Metehan Cakır",
    "accountNumber": "12345678",
    "balance" : 3000,
    "additional account": 2000
}

ipekAccount= {
    "name": "Ipek Cakır",
    "accountNumber": "123456789",
    "balance" : 2000,
    "additional account": 1000
}


def withdrawal(account, amount):
    print(f"Hello {account['name']}")
    
    if account["balance"]>=amount:
        print("You can take your money")
        account["balance"]=account["balance"]-amount
    else:
        if account["balance"]+account["additional account"]>= amount:
            a=input("Your balance is not enough to withdraw this money. Do you want to use the money in your additional account? Yes/No:")
            if a=="Yes" or a=="yes" :
                print("You can take your money")
                account["additional account"]= account["additional account"]-(amount-account["balance"])
                account["balance"]=0
            elif a=="No" or a=="no" :
                print("The wtihdraw canceled.")
            else:
                print("The wtihdraw canceled.")
        else:
            print("Your balance is not enough to withdraw this money. The wtihdraw canceled.")

def balanceInquiry(account):
    print(f" The balance of your account with number {account['accountNumber']}: {account['balance']} and the balance of your additional account :{account['additional account']}")

withdrawal(meteAccount,3500)
balanceInquiry(meteAccount)               