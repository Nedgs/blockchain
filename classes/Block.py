import json
import os
import shutil
import hashlib
from os import walk


class Block:
    def __init__(self, base_hash, hash, parent_hash):
        self.base_hash = base_hash
        self.hash = hash
        self.parent_hash = parent_hash
        self.transactions = []
        if self.check_hash() is False:
            return False



    def check_hash(self):

        hash = hashlib.sha256(self.base_hash.encode()).hexdigest()

        if self.hash == hash:
            return True
        return False

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        return self.save()

    def get_transaction(self, number):
        for t in self.transactions:
            if t["number"] == number:
                return t
        return None

    def get_weight(self):
        filename = './content/blocs/{}.json'.format(self.hash)
        file_stats = os.stat(filename)
        print(file_stats.st_size)

    def save(self):
        file_name = "./content/blocs/{}.json".format(self.hash)
        jsonString = json.dumps({"id_block":self.hash,"parent_block":self.parent_hash,"transactions":self.transactions})

        with open(file_name, "x") as file:
            file.write(jsonString)

    def load(self, id_block):

        filename = str(id_block) + ".json"
        path_blocs_folder = "./content/blocs/"
        file_names = []

        for (dirpath, filenames, filenames) in walk(path_blocs_folder):
            file_names.extend(filenames)
            break

        if filename in file_names:
            with open(path_blocs_folder + filename, "r") as file:
                json_data = json.load(file)
                self.hash = json_data['id_block']
                self.parent_hash = json_data['parent_hash']
                self.transactions = json_data['transactions']
                return json_data
        else:
            print('ERROR : The block was not found !')