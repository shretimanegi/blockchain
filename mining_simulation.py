
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
    
    def mineBlock(self,difficulty):
        print(f"Mining Block {self.index} with difficulty {difficulty}")
        start_time=time.time()
        attempt=0
        prefix='0'*difficulty #target pattern the hash must start with
        while(not self.block_hash.startswith(prefix)):
            #increase the value of nonce to make the hash start with target pattern
            self.nonce+=1 
            self.block_hash=self.compute_hash()
            attempt+=1
        end_time=time.time()
        duration=end_time-start_time
        print(f"Block mined!")
        print(f"Hash: {self.block_hash}")
        print(f"Attempts: {attempt}")
        print(f"Time taken: {duration:.4f} seconds\n")

#Create Blockchain
chain=[]

#Genesis Block
chain.append(Block(0,"Genesis block","0"))

#Block 1
chain.append(Block(1,"Tanya Sharma",chain[0].block_hash))

#Block 2
chain.append(Block(1,"Vinay Kumar",chain[1].block_hash))

#CHALLENGE: To print how many nonce attempts were made to measure the time taken
chain[0].mineBlock(difficulty=2)
chain[1].mineBlock(difficulty=4)
chain[1].mineBlock(difficulty=5)









