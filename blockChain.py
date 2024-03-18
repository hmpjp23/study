import hashlib
import time


class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):  # 스페셜 메서드. 생성자
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.transactions}{self.timestamp}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2

    def create_genesis_block(self):
        return Block(0, "Genesis Block", time.time(), "0")

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True


# 블록체인 생성 및 블록 추가
blockchain = Blockchain()
blockchain.add_block(Block(1, "First transaction",
                     time.time(), blockchain.chain[-1].hash))
blockchain.add_block(Block(2, "Second transaction",
                     time.time(), blockchain.chain[-1].hash))

# 블록체인 검증
print("Blockchain is valid?", blockchain.is_valid())
