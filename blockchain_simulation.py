import hashlib
import time

class Block:
#the class block defines the structure of each blocks

    def __init__(self,index,data,prev_hash):
        self.index=index
        self.timestamp=time.time()
        self.nonce=0
        self.data=data
        self.prev_hash=prev_hash
        self.block_hash=self.compute_hash()
    
    #This calculates the hash of the block
    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.prev_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest() #Merkle root
    
    def mine(self,difficulty):
        prefix='0'*difficulty #target pattern the hash must start with
        while(not self.block_hash.startswith(prefix)):
            #increase the value of nonce to make the hash start with target pattern
            self.nonce+=1 
            self.block_hash=self.compute_hash()
    
    def display(self):
        #prints the block
        print(f"Block : {self.index}")
        print(f"Data : {self.data}")
        print(f"Hash : {self.block_hash}")
        print(f"Prev hash : {self.prev_hash}\n")


#Check the validity of a blockchain
def is_valid(chain,difficulty):
    for i in range(1,len(chain)): # 0-block(Genisis) block has nothing to compare with
        
        current=chain[i] #current block
        prev=chain[i-1]  #previous block

        #current.block_hash -> what was saved when the block was mined
        #current.compute_hash -> recomputates the hash value
        if current.block_hash!=current.compute_hash():
            print(f"Block {current.index} has invalid hash")
            return False  #Someone alterned the content of the block
        
        #Each block should point to the hash of the block before it
        if current.prev_hash!=prev.block_hash:
            print(f"Block {current.index} has invalid prev hash")
            return False  #Chain is broken
        
        #To check if PoW was implemented correctly
        if not current.block_hash.startswith('0'*difficulty):
            print(f"Block {current.index} wasn't correctly mined")
            return False  #Either not mined or tampered
    
    return True

#Create Blockchain
difficulty=3
chain=[]

#Genesis Block
chain.append(Block(0,"Genesis block","0"))
chain[0].mine(difficulty)

#Block 1
chain.append(Block(1,"Tanya Sharma",chain[0].block_hash))
chain[1].mine(difficulty)

#Block 2
chain.append(Block(1,"Vinay Kumar",chain[1].block_hash))
chain[2].mine(difficulty)

#Display
print("Blockchain: ")
for block in chain:
    block.display()

#Validity
print("Blockchain validity : ", is_valid(chain,difficulty))

#CHALLENGE: Changing the data of Block 1 and recalculting the hash
chain[0].data="Data has been tampered"
chain[0].hash=chain[0].compute_hash()

#After tampering
for block in chain:
    block.display()

#Check the validity
print("Blockchain validity : ", is_valid(chain,difficulty))


