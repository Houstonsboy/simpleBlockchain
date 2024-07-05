import hashlib

class KadmusCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash=previous_block_hash
        self.transaction_list=transaction_list
        
        self.block_data="-".join(transaction_list)+ "-"+previous_block_hash
        self.block_hash=hashlib.sha256(self.block_data.encode()).hexdigest() 
        # encoding is because hashing is done bytes not strings
      
t1="Gift sends 0.6 KC to Gift"       
t2="Mike sends 3.6 KC to Brian"        
t3="Brenda sends 8 KC to Linet"        
t4="Linet sends 6 KC to Gift"      
t5="James sends 3 KC to Chris"        
t6="Abel sends 3 KC to Drake"       

initial_block=KadmusCoinBlock("Initial Hash",([t1,t2]))  
print(initial_block.block_data)
print(initial_block.block_hash) 

second_block=KadmusCoinBlock(initial_block.block_hash,([t3,t4]))
print(second_block.block_hash) 
third_block=KadmusCoinBlock(second_block.block_hash,([t5,t6]))
print(third_block.block_hash)  