from hashlib import sha256
import json, random
from time import time


class Block:
    def __init__(self,transactions, prev_hash, i, proof=0):
        self.index = i
        self.transactions = transactions
        self.timestamp = time()
        self.hash = None
        self.proof = proof
        self.nonce = 0
        self.prev_hash = prev_hash
    
    def hash_block(self):
        # self.prev_hash = prev_hash
        block = {'index': self.index, 'transactions': self.transactions, 'timestamp':self.timestamp, 'hash':self.hash, 'proof':self.proof, 'nonce':self.nonce, 'prev_hash': self.prev_hash }
        jsoned = json.dumps(block,sort_keys=True)
        hashed = sha256(jsoned.encode('utf-8')).hexdigest()
        self.hash = hashed
        return hashed

    def __repr__(self):
        block = {'index': self.index, 'transactions': self.transactions, 'timestamp':self.timestamp, 'hash':self.hash, 'proof':self.proof, 'nonce':self.nonce, 'prev_hash': self.prev_hash, }
        stringified_block = json.dumps(block, sort_keys=True)
        
        return stringified_block

class Transaction:
    def __init__(self,sender,receiver,amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
    
    def hash_transaction(self):
        transaction = {
            'sender': self.sender,
            'recipient': self.receiver,
            'amount': self.amount
        }
        jsoned = json.dumps(transaction,sort_keys=True)
        return sha256(jsoned.encode('utf-8')).hexdigest()
    
    def __repr__(self):
        transaction = {
            'sender': self.sender,
            'recipient': self.receiver,
            'amount': self.amount
        }
        return str(transaction)

# t = Transaction('amir','nadia',50)
# print(t)



class BlockChain:
    def __init__(self):
        self.chain = []
        self.transactions = []
    
    def add_block(self,exchanges,existing_block=None):

        xs = [] #xs stands for exchanges.  the array storing the stringified Transaction objects
        for x in exchanges:
            sender,receiver,amount = x
            t = Transaction(sender,receiver,amount)
            xs.append(str(t))

        self.transactions += xs

        if existing_block is None:
            if not len(self.chain):
                prev_hash,index,proof = 0,1,0
                genesis = Block(xs,prev_hash,index,proof)
                genesis.hash_block()
                self.chain.append(genesis)
            else: #there exists blocks on the chain
                prev_hash = self.chain[-1].hash
                print('prev_hash', prev_hash)
                last_proof = self.chain[-1].proof
                print('last_proof', last_proof)
                index = self.chain[-1].index + 1
                proof = self.proof_of_work(last_proof,5)
                print('proof: ',proof)
                new_block = Block(xs,prev_hash,index,proof)
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

    def proof_of_work(self, last_proof,difficulty=3):
        ''' - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof'''

        proof = 0
        zeros = ''

        for i in range(difficulty):
            zeros += '0'
        print('zeros', zeros)

        while self.hash_try(proof,last_proof)[:difficulty] != zeros:
            # print(f'attempt # {proof}', self.hash_try(proof,last_proof))
            proof += 1
        
        print('found solution:', self.hash_try(proof,last_proof))
        return proof

        # x = len(self.transactions)
        # y = 0

        # simple problem:  find a hash
        # while sha256(str(x*y).encode('utf-8')).hexdigest()[:5] != '00000':
        #     y += 1
        # hashed = sha256(str(x*y).encode('utf-8')).hexdigest()
        # print('found solution: ', y)
        # return hashed
         # while sha256(str(proof + last_proof).encode('utf-8')).hexdigest()[:3] != '000':
        #      proof += 1
       

    def hash_try(self,proof,last_proof):
        new_proof = str(proof) + str(last_proof)
        return sha256(new_proof.encode('utf-8')).hexdigest()

    def hash_blocks(self):
        for i,b in enumerate(self.chain):
            if i == 0:
                prev_hash = 0
                genesis = b
                genesis.hash_block(prev_hash)
            else:
                prev_hash = self.chain[i-1].hash
                b.hash_block(prev_hash)

    def set_difficulty(self,difficulty):
        zeros = ''
        for i in range(difficulty):
            zeros += '0'
        # zeros = zeros[1:]
        for i,b in enumerate(self.chain):
            b.hash = zeros + b.hash
            if i == 0:
                b.prev_hash = 0
                continue
            b.prev_hash = self.chain[i-1].hash
        return self.chain
        
        return zeros
    
    def check_difficulty(self,difficulty):
        genesis_hash = self.chain[0].hash
        for i,c in enumerate(genesis_hash):
            if c != '0':
                break
        return i >= difficulty

    
    def blockchain(self):
        for b in self.chain:
            print(b)
            print('\n')
        
    def __repr__(self):
        return str(self.chain)


bc = BlockChain()

an2 = ('amir','nancy',20)
jj10 = ('joe','jacob',10)
zz5 = ('zieger','zelda',5)
ma50 = ('muhammad','abdullah',50)
jl12 = ('jose','leanna',12)

bc.add_block([an2])
bc.add_block([jj10,zz5,ma50])

bc.blockchain()



# bc.blockchain()
# print('\n')
# bc.set_difficulty(7)
# bc.hash_blocks()
# bc.set_difficulty(5)
# bc.hash_blocks()
# bc.blockchain()

# x = bc.check_difficulty(3)
# print(x)
# bc.hash_blocks()


# bc.blockchain()









# hashed = sha256('test'.encode('utf-8')).hexdigest()
# x = bc.hash_difficulty(hashed,3)




    

