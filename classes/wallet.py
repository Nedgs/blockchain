import uuid
import os
import json


class Wallet:
    def __init__(self, unic_id=None):
        if unic_id is None:
            self.unic_id = self.generate_unic_id ()
            self.balance = 100
            self.history = []
            self.save()
        else:
            self.unic_id = unic_id
            self.load()

    def generate_unic_id(self):
        wallet_uuid = str(uuid.uuid4())

        if os.path.exists(f"./content/wallets/{wallet_uuid}.json"):
            return self.generate_unic_id()

        return wallet_uuid

    def add_balance(self, transaction):
        self.balance = self.balance + transaction["amount"]
        self.send(transaction)

    def sub_balance(self, transaction):
        self.balance -= transaction["amount"]
        self.send(transaction)

    def send(self, transaction):
        self.history.append({

            'amount': transaction["amount"],
            'emitter': transaction["emitter"],
            'receiver': transaction["receiver"],
            'date': transaction["date"],
            'transaction': transaction["number"]
        })
        self.save()

    def save(self):
        data = {
            'unic_id ': self.unic_id,
            'balance': self.balance,
            'history': []
        }

        for h in self.history:
            data['history'].append(h)

        with open(f"./content/wallets/{self.unic_id }.json", "w") as file:
            json.dump(data, file)

    def load(self):
        if os.path.exists(f"./content/wallets/{self.unic_id }.json"):
            with open(f"./content/wallets/{self.unic_id }.json") as file:
                data = json.load(file)
                self.unic_id  = data["unic_id "]
                self.balance = data["balance"]
                self.history = data["history"]

            return True
        else:
            return False