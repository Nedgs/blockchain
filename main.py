from classes.wallet import Wallet

if __name__ == "__main__":
    
    Wallet = Wallet() 

    Wallet.generate_unique_id()
    Wallet.add_balance(4500)

    Wallet.save()