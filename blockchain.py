import hashlib
import json
from datetime import time


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(proof=100, previous_hash=1)

    def new_block(self, proof, previous_hash=None):
        # Creates new blocks and adds them to the chain

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = []
        self.chain.append(block)

        return block

    def new_transaction(self, sender, recipient, amount):
        # Appends a new transaction to the currently existing transactions
        self.current_transactions.append(
            {
                'sender': sender,
                'recipient': recipient,
                'amount': amount
            }
        )

        return self.last_block['index'] + 1

    def proof_of_work(self, last_proof):
        # Consensus algorithm

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    def register_node(self):
        pass

    def valid_chain(self):
        pass

    @staticmethod
    def valid_proof(last_proof, proof):
        # Validates the block

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:4] == '0000'

    @staticmethod
    def hash(block):
        # Hashes a block

        block_string = json.dumps(block, sort_keys=True).encode()
        
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # Returns the last block in the chain

        return self.chain[-1]
