from os import walk
import uuid
import json

class Wallet:

    unic_id = int
    balance = 0 
    history = {} 

    def generate_unique_id(self):
        
        file_names = []
        for (dirpath, s, filenames) in walk("./content/wallets"):
            file_names.extend(filenames)
            break

        unic_id = uuid.uuid1()

        while(str(unic_id) + ".json" in file_names):
            unic_id = uuid.uuid1()
        
        self.unic_id = int(unic_id)

    def add_balance(self, amount: int):
        self.balance = self.balance + amount
    
    def sub_balance(self, amount):
        if amount > self.balance:
            print("The amount is higher than your balance !")
        else:
            self.balance = self.balance - amount 

    def send(self):
        pass

    def load(self, unic_id):

        filename = str(unic_id) + ".json"
        path_wallets_folder = "./content/wallets/"
        file_names = []

        for (dirpath, filenames, filenames) in walk(path_wallets_folder):
            file_names.extend(filenames)
            break

        if filename in file_names:
            with open(path_wallets_folder + filename, "r") as file:
                json_data = json.load(file)
                self.unic_id = json_data['id']
                self.balance = json_data['balance']
                self.history = json_data['history']
                return json_data
        else:
            print('The identification number was not found !')


    def save(self):
        file = "./content/wallets/{}.json".format(self.unic_id)
        jsonString = json.dumps({"id": self.unic_id,"balance": self.balance, "history": self.history})

        with open(file, "x") as file:
            file.write(jsonString)