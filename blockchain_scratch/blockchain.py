from hashlib import sha256
import json
import random
from time import time
from uuid import uuid4
from textwrap import dedent
# from urllib import urlparse

from flask import Flask,jsonify,request
from flask_cors import CORS

# import names
# t = Transaction('amir','nadia',50)
# print(t)

class BlockChain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.nodes = set()
    
    def register_node(self,address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def consensus_chain(self, chain,difficulty):
        prev_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(prev_block)
            print(block)
            print('\n-------------\n')

            if block['prev_hash'] != self.hash(prev_block):
                return False

            zeros = ''
            for i in range(difficulty):
                zeros += '0'
            
            #check proof of work is valid:
            proof = block['proof']
            prev_proof = prev_block['proof']
            hashed_proof = self.hash_proofs(proof,prev_proof)
            if hashed_proof[:difficulty] != zeros:  #the proof should always end up passing the work test, that value is what succeeded the first time.
                return False
            
            prev_block = block
            current_index += 1
        return True

    def new_transaction(self,sender,receiver,amount):
        # t = Transaction(sender,receiver,amount)
        # self.transactions.append(str(t))
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        }

        self.transactions.append(transaction)
        if len(self.chain):
            return self.last_block['index'] + 1 #return the index of the next block to add this particular transaction to after the new block is mined.
        else: return 2

    def new_block(self, proof, prev_hash=0):

        # if not len(self.chain):
        #     last_proof = 0
        # else:
        #     last_proof = self.chain[-1]['proof']
    
        # proof = self.proof_of_work(last_proof,4) #whoever gets the proof of work, then their block will be created with all the transactions pending in the blockchain. then the transactions will be cleared out again

        print('proof', proof)

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.transactions,
            'proof': proof,
            'prev_hash': prev_hash if not len(self.chain) else self.hash(self.chain[-1])
            # 'prev_hash': prev_hash or self.hash(self.chain[-1])
        }

        self.transactions = []
        # self.new_transaction('0','miner',1)
        # if len(block['transactions']):
        self.chain.append(block)
        return block

    def proof_of_work(self, last_proof,difficulty=3):
        ''' - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof'''

        proof = 0
        zeros = ''

        for i in range(difficulty):
            zeros += '0'
        print('zeros', zeros)

        while self.hash_proofs(proof,last_proof)[:difficulty] != zeros:
            # print(f'attempt # {proof}', self.hash_try(proof,last_proof))
            proof += 1
        
        print('found solution:', self.hash_proofs(proof,last_proof))
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

    def hash_proofs(self,proof,last_proof):
        new_proof = str(proof) + str(last_proof)
        return sha256(new_proof.encode('utf-8')).hexdigest()
    
    def hash_all(self):
        hashes = []
        for b in self.chain:
            hb = self.hash(b)
            hashes.append(hb)
        return hashes
    
    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True)
        hashed_block = sha256(block_string.encode('utf-8')).hexdigest()
        return hashed_block
    
    @property
    def last_block(self):
        return self.chain[-1] if len(self.chain) else None

    def blockchain(self):
        for b in self.chain:
            print(b)
            print('\n')
        return self.chain
        
    def __repr__(self):
        return str(self.chain)

app = Flask(__name__)
CORS(app)


node_identifier = str(uuid4()).replace('-', '')

# bc = BlockChain()
# bc.new_block()
# last_proof = bc.last_block['proof']
# proof = bc.proof_of_work(last_proof)
# prev_hash = bc.hash(bc.last_block)
# bc.new_block(proof,prev_hash)

# bc.new_transaction('amir','nancy',20)

# bc.blockchain()

bc = BlockChain()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/mine', methods=['GET'])
def mine():
    # return "We'll mine a new Block"
    '''
    1.Calculate the Proof of Work
    2.Reward the miner (us) by adding a transaction granting us 1 coin
    3.Forge the new Block by adding it to the chain
    '''
    #where to get the last_proof from?
    if not bc.last_block:
        last_proof = 0
    else: last_proof = bc.last_block['proof']
    proof = bc.proof_of_work(last_proof,5)  #2nd argument is the difficulty setting of the proof of work
    prev_hash = bc.hash(bc.last_block)
    bc.new_transaction('0',node_identifier,1)

    new_block = bc.new_block(proof,prev_hash)

    response = {
        'message': 'New Block Forged',
        'index': new_block['index'],
        'transactions': new_block['transactions'],
        'proof': new_block['proof'],
        'prev_hash': new_block['prev_hash']
    }

    return jsonify(response), 200





@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    print(values)

    required = ['sender', 'receiver', 'amount']
    if not all(t in values for t in required):
        return 'Missing Values', 400

    index = bc.new_transaction(values['sender'],values['receiver'],values['amount'])
    response = {'message': f"Transaction will be added to Block {index}"}
    return jsonify(response), 201

    # return "We'll add a new transaction"

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': bc.chain,
        'length': len(bc.chain)
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)








# bc.new_transaction('amir','nancy',20)
# genesis = bc.new_block()
# b1 = bc.new_block()
# b2 = bc.new_block()
# b3 = bc.new_block()
# b4 = bc.new_block()
# b5 = bc.new_block()
# bc.new_transaction('adam','sally',5)
# b6 = bc.new_block()
# b7 = bc.new_block()
# b8 = bc.new_block()


# hashes = bc.hash_all()

# bc.blockchain()

# an2 = ('amir','nancy',20)
# jj10 = ('joe','jacob',10)
# zz5 = ('zieger','zelda',5)
# ma50 = ('muhammad','abdullah',50)
# jl12 = ('jose','leanna',12)

# first_names = ["Adam", "Alex", "Aaron", "Ben", "Carl", "Dan", "David", "Edward", "Fred", "Frank", "George", "Hal", "Hank", "Ike", "John", "Jack", "Joe", "Larry", "Monte", "Matthew", "Mark", "Nathan", "Otto", "Paul", "Peter", "Roger", "Roger", "Steve", "Thomas", "Tim", "Ty", "Victor", "Walter"]

# class Block:
#     def __init__(self,transactions, prev_hash, i, proof=0):
#         self.index = i
#         self.transactions = transactions
#         self.timestamp = time()
#         self.hash = None
#         self.proof = proof
#         self.prev_hash = prev_hash
    
#     def hash_block(self):
#         # self.prev_hash = prev_hash
#         block = {'index': self.index, 'transactions': self.transactions, 'timestamp':self.timestamp, 'hash':self.hash, 'proof':self.proof,'prev_hash': self.prev_hash}
#         jsoned = json.dumps(block,sort_keys=True)
#         hashed = sha256(jsoned.encode('utf-8')).hexdigest()
#         self.hash = hashed
#         return hashed

#     def __repr__(self):
#         block = {'index': self.index, 'transactions': self.transactions, 'timestamp':self.timestamp, 'hash':self.hash, 'proof':self.proof,'prev_hash': self.prev_hash}
#         stringified_block = json.dumps(block, sort_keys=True)
        
#         return stringified_block

# class Transaction:
#     def __init__(self,sender,receiver,amount):
#         self.sender = sender
#         self.receiver = receiver
#         self.amount = amount
    
#     def hash_transaction(self):
#         transaction = {
#             'sender': self.sender,
#             'recipient': self.receiver,
#             'amount': self.amount
#         }
#         jsoned = json.dumps(transaction,sort_keys=True)
#         return sha256(jsoned.encode('utf-8')).hexdigest()
    
#     def __repr__(self):
#         transaction = {
#             'sender': self.sender,
#             'recipient': self.receiver,
#             'amount': self.amount
#         }
#         return str(transaction)


# def transaction_generator(quantity):
#     transactions = []
#     for i in range(quantity):
#         # n1 = names.get_first_name(gender="male")
#         # n2 = names.get_first_name(gender="female")
#         n1 = random.choice(first_names)
#         n2 = random.choice(first_names)
#         amount = random.randint(1,100)
#         transactions.append((n1,n2,amount))
#     return transactions

# transactions = transaction_generator(15)

# bc.add_block([an2])
# bc.add_block([jj10,zz5,ma50])
# for i in range(10):
#     a = bc.add_block([random.choice(transactions)])
#     print(type(a),a)

# chain = bc.blockchain()
# print(len(chain))




    # def add_block(self,exchanges):
    #     xs = [] #xs stands for exchanges.  the array storing the stringified Transaction objects
    #     for x in exchanges:
    #         sender,receiver,amount = x
    #         t = Transaction(sender,receiver,amount)
    #         xs.append(str(t))

    #     self.transactions += xs

    #     # if existing_block is None:
    #     if len(self.chain) == 0:
    #         prev_hash,index,proof = 0,1,0
    #         genesis = Block(xs,prev_hash,index,proof)
    #         genesis.hash_block()
    #         self.chain.append(genesis)
    #         return genesis.__dict__
    #     else: #there exists blocks on the chain
    #         prev_hash = self.chain[-1].hash
    #         print('prev_hash', prev_hash)
    #         last_proof = self.chain[-1].proof
    #         print('last_proof', last_proof)
    #         index = self.chain[-1].index + 1
    #         proof = self.proof_of_work(last_proof,4)
    #         print('proof: ',proof)
    #         new_block = Block(xs,prev_hash,index,proof)
    #         new_block.hash_block()
    #         self.chain.append(new_block)
    #         return new_block.__dict__

        # else: #block has been passed in
        #     if not len(self.chain): #genesis block
        #         genesis = existing_block
        #         genesis.prev_hash = 0
        #         genesis.hash_block()
        #         self.chain.append(genesis)
        #         return genesis.__dict__()
        #     else: #there are blocks in the block chain
        #         existing_block.prev_hash = self.chain[-1].hash
        #         existing_block.index = self.chain[-1].index + 1
        #         existing_block.hash_block()
        #         self.chain.append(existing_block)
        #         return existing_block

       
    
    

    # def hash_blocks(self):
    #     for i,b in enumerate(self.chain):
    #         if i == 0:
    #             prev_hash = 0
    #             genesis = b
    #             genesis.hash_block(prev_hash)
    #         else:
    #             prev_hash = self.chain[i-1].hash
    #             b.hash_block(prev_hash)

    # def set_difficulty(self,difficulty):
    #     zeros = ''
    #     for i in range(difficulty):
    #         zeros += '0'
    #     # zeros = zeros[1:]
    #     for i,b in enumerate(self.chain):
    #         b.hash = zeros + b.hash
    #         if i == 0:
    #             b.prev_hash = 0
    #             continue
    #         b.prev_hash = self.chain[i-1].hash
    #     return self.chain
        
    #     return zeros
    
    # def check_difficulty(self,difficulty):
    #     genesis_hash = self.chain[0].hash
    #     for i,c in enumerate(genesis_hash):
    #         if c != '0':
    #             break
    #     return i >= difficulty

    
    




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




    

