from hashlib import sha256
import json, random
from time import time


class Block:
    def __init__(self,transactions, prev_hash, i):
        self.index = i
        self.transactions = transactions
        self.timestamp = time()
        self.hash = None
        self.proof = None
        self.nonce = 0
        self.prev_hash = prev_hash
    
    def hash_block(self):
        block = {'index': self.index, 'transactions': self.transactions, 'timestamp':self.timestamp, 'hash':self.hash, 'proof':self.proof, 'nonce':self.nonce, 'prev_hash': self.prev_hash, }
        jsoned = json.dumps(block,sort_keys=True)
        hashed = sha256(jsoned.encode('utf-8')).hexdigest()
        self.hash = hashed
        return hashed

    def __repr__(self):
        block = {'index': self.index, 'transactions': self.transactions, 'timestamp':self.timestamp, 'hash':self.hash, 'proof':self.proof, 'nonce':self.nonce, 'prev_hash': self.prev_hash, }
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

    def hash_blocks(self):
        for i,b in enumerate(self.chain):
            if i == 0:
                b.prev_hash = 0
                continue
            b.prev_hash = self.chain[i-1].hash
        return self.chain

    def set_difficulty(self,difficulty):
        zeros = ''
        for i in range(difficulty):
            zeros += '0'
        # zeros = zeros[1:]
        for b in self.chain:
            b.hash = zeros + b.hash
        return zeros
    
    def blockchain(self):
        for b in self.chain:
            print(b)
            print('\n')
        
    def __repr__(self):
        return str(self.chain)


bc = BlockChain()
bc.add_block()
bc.add_block()
bc.add_block()
bc.add_block()
bc.add_block()

# bc.blockchain()
print('\n')
bc.set_difficulty(3)
bc.hash_blocks()

bc.blockchain()








# hashed = sha256('test'.encode('utf-8')).hexdigest()
# x = bc.hash_difficulty(hashed,3)




    

