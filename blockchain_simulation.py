
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
        
    def display(self):
        #prints the block
        print(f"Block : {self.index}")
        print(f"Data : {self.data}")
        print(f"Hash : {self.block_hash}")
        print(f"Prev hash : {self.prev_hash}\n")


#Check the validity of a blockchain
def is_valid(chain):
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
            
    return True

#Create Blockchain

chain=[]

#Genesis Block
chain.append(Block(0,"Genesis block","0"))

#Block 1
chain.append(Block(1,"Tanya Sharma",chain[0].block_hash))

#Block 2
chain.append(Block(1,"Vinay Kumar",chain[1].block_hash))

#Display
print("Blockchain: ")
for block in chain:
    block.display()

#Validity
print("Blockchain validity : ", is_valid(chain))

#CHALLENGE: Changing the data of Block 1 and recalculting the hash
chain[1].data="Data has been tampered"
chain[1].hash=chain[0].compute_hash()

#After tampering
for block in chain:
    block.display()

#Check the validity
print("Blockchain validity : ", is_valid(chain))



