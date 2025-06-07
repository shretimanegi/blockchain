import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        prefix = '0' * difficulty
        while not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()

    def display(self):
        print(f"Block {self.index}")
        print(f"  Data: {self.data}")
        print(f"  Hash: {self.hash}")
        print(f"  Prev: {self.previous_hash}\n")

def is_chain_valid(chain, difficulty):
    for i in range(1, len(chain)):
        current = chain[i]
        previous = chain[i - 1]

        if current.hash != current.calculate_hash():
            print(f"Block {current.index} has invalid hash!")
            return False

        if current.previous_hash != previous.hash:
            print(f"Block {current.index} has invalid previous hash!")
            return False

        if not current.hash.startswith('0' * difficulty):
            print(f"Block {current.index} is not properly mined!")
            return False

    return True

# Create blockchain
difficulty = 2
chain = []

# Genesis Block
chain.append(Block(0, "Genesis Block", "0"))
chain[0].mine_block(difficulty)

# Block 1
chain.append(Block(1, "Block 1 Data", chain[0].hash))
chain[1].mine_block(difficulty)

# Block 2
chain.append(Block(2, "Block 2 Data", chain[1].hash))
chain[2].mine_block(difficulty)

print(" Initial Blockchain:")
for block in chain:
    block.display()

print(" Blockchain Valid?", is_chain_valid(chain, difficulty))

# Tampering with Block 1
print("\n Tampering Block 1 data...")
chain[1].data = "Tampered Data"
chain[1].hash = chain[1].calculate_hash()  # only recompute its own hash

print("\n After Tampering:")
for block in chain:
    block.display()

print(" Blockchain Valid?", is_chain_valid(chain, difficulty))
