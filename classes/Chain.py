import hashlib
import string
import random
from .Block import Block
from .Wallet import Wallet
import sys
from datetime import datetime


class Chain:
    def __init__(self):
        self.blocks = []
        self.last_transaction_number = 0
        self. number = 0

    def generate_hash(self):

        letters = string.printable
        index = random.randint(1, 101)

        random_string = ''
        for i in range(index):
            random_string = random_string.join(random.choice(letters))

        new_hash = hashlib.sha256(random_string.encode()).hexdigest()

        if self.verify_hash(new_hash):
            if self.add_block(random_string, new_hash) is False:
                return "error."
            else:
                return " Block success"
        else:
            self.number=self.number +1
            print(self.number)
            self.generate_hash()


    def verify_hash(self, verify_hash):
        for n in self.blocks:
            if n.hash == verify_hash:
                return False

        return True

    def add_block(self, random_string, new_hash):
        if len(self.blocks) < 1:
            parent_hash = "00"
        else:
            parent_hash = self.blocks[len(self.blocks) - 1].hash

        block = Block(random_string, new_hash, parent_hash)
        if block is not False:
            block.save()
            self.blocks.append(block)
            return True
        else:
            return False

    def get_block(self, block_hash):
        for b in self.blocks:
            if b.hash == block_hash:
                return b

        return None
