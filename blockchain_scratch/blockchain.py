from hashlib import sha256
import json, random
from time import time


class Block:
    def __init__(self,transactions, prev_hash, i):
        self.index = i
        self.timestamp = time()
        # self.hash = sha256('test'.encode('utf-8')).hexdigest()
        self.hash = None
        self.proof = None
        self.prev_hash = prev_hash
        self.transactions = transactions
    
    def hash_block(self):
        block = {'index': self.index, 'timestamp':self.timestamp, 'hash':self.hash, 'proof':self.proof, 'prev_hash': self.prev_hash, 'transactions': self.transactions}
        jsoned = json.dumps(block,sort_keys=True)
        hashed = sha256(jsoned.encode('utf-8')).hexdigest()
        self.hash = hashed
        return hashed

    def __repr__(self):
        block = {'index': self.index, 'timestamp':self.timestamp, 'hash':self.hash, 'proof':self.proof, 'prev_hash': self.prev_hash, 'transactions': self.transactions}
        stringified_block = json.dumps(block, sort_keys=True)
        
        return stringified_block


class BlockChain:
    def __init__(self):
        self.chain = []
        self.transactions = []
    
    def add_block(self,transactions=[],block=None):
        if block is None:
            if not len(self.chain):
                genesis = Block(transactions,0,1)
                genesis.hash_block()
                self.chain.append(genesis)
            else: #there exists blocks on the chain
                prev_hash = self.chain[-1].hash
                index = self.chain[-1].index + 1
                new_block = Block(transactions,prev_hash,index)
                new_block.hash_block()
                self.chain.append(new_block)
        else: #block has been passed in
            if not len(self.chain): #genesis block
                genesis = block
                genesis.prev_hash = 0
                genesis.hash_block()
                self.chain.append(genesis)
            else: #there are blocks in the block chain
                block.prev_hash = self.chain[-1].hash
                block.index = self.chain[-1].index + 1
                block.hash_block()
                self.chain.append(block)
        
    def __repr__(self):
        return str(self.chain)


bc = BlockChain()
bc.add_block()
bc.add_block()
bc.add_block()
bc.add_block()

for block in bc.chain:
    print(block)
    print('\n')








    

