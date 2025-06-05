import hashlib
import time
from datetime import datetime
#defining constants
MAX_STRING =256
DIFFICULTY=2

class block:
    def __init__(self, index, timestamp, data, prev_hash, nonce=0):
        self.index=index
        self.timestamp=timestamp
        self.data=data
        self.prev_hash= prev_hash
        self.nonce=nonce
        self.hash=self.calculate_hash()
        
    def calculate_hash(self):  #calculating hash using sha256 function
        block_string = f"{self.index}{self.timestamp}{self.prev_hash}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()
    def __str__(self):  #representing details of the block
        return (f" Block{self.index}[\n"
                f" Timestamp:{self.timestamp}\n"
                f" prev_hash: {self.prev_hash}\n"
                f" data: {self.data} \n"
                f" nonce: {self.nonce} \n"
                f" hash: {self.hash} \n]")
class block_chain:
    def __init__(self):
        self.chain=[self.create_genesis_block()]
        
    def create_genesis_block(self): #creating first block
        return block(
            index=0,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            data="this is the first one",
            prev_hash="0",
            nonce=0
        )
        
    def get_latest_block(self): #getting recent block
        return self.chain[-1]
        
    def add_new_block(self, data): #adding new block to chain
        new_block=block(
                index=self.get_latest_block().index+1,
                timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                data=data,
                prev_hash=self.get_latest_block().hash,
                )
        self.mine_block(new_block) #mine the block
        
        self.chain.append(new_block)#adding to chain
    
    def mine_block(self, block):
    #finding nonce until we get the hash of the block starting with difficulty*zeroes
    
        print(f" Mining the block {block.index}\n")
        start_time= time.time()
    
        while not block.hash.startswith("0"*DIFFICULTY):
            block.nonce+=1
            block.hash=block.calculate_hash()
        end_time= time.time()
        time_took= end_time - start_time
    
        print(f" time taken to create hash : {time_took:.4f} seconds\n ")
        print(f" final nonce value is : {block.nonce} and the hash : {block.hash}\n ")
   
    def is_valid(self):
        
        for i in range(1, len(self.chain)):
           
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
           
            if current_block.hash != current_block.calculate_hash():
                print(f" block{current_block.index} has been tampered with!")
               
                return False
               
            if current_block.prev_hash != previous_block.hash:
                print(f" block {current_block.index} has invalid previous_hash!")
                
                return False
                
            if not current_block.hash.startswith(DIFFICULTY*"0"):
                print(f" block{current_block.index} has invalid proof-of-work!")
                
                return False
               
        print("Blockchain is valid")
        return True
