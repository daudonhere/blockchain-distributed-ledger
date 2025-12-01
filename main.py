import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "genesis block", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), data, previous_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            prev = self.chain[i - 1]
            curr = self.chain[i]

            if curr.hash != curr.calculate_hash():
                return False

            if curr.previous_hash != prev.hash:
                return False

        return True


bc = Blockchain()
bc.add_block("transaction 1: A -> B")
bc.add_block("transaction 2: B -> C")
bc.add_block("transaction 3: C -> D")

print("valid before modification:", bc.is_chain_valid())

bc.chain[1].data = "fake transaction: X -> Y"
print("valid after modification:", bc.is_chain_valid())
