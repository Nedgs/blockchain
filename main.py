from classes.Wallet import Wallet
from classes.Chain import Chain
import sys


def main():


    wallet1 = Wallet()
    print( wallet1.unic_id, wallet1.balance)
    chain = Chain()
    result = chain.generate_hash()
    print(result)








if __name__ == "__main__":
    sys.setrecursionlimit(999999999)

    main()