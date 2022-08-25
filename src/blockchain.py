from block import Block
import datetime
from SmartContract import SmartContract

num_blocks_to_add = 10

block_chain = [Block.create_genesis_block()]

print("The genesis block has been created.")
print("Hash: %s" % block_chain[0].hash)

SC = SmartContract()

for i in range(1, num_blocks_to_add):
    data = SC.run()
    print(data.token1)
    block_chain.append(Block(block_chain[i-1].hash,
                             data,
                             datetime.datetime.now()))
    print("Block #%d created." % i)
    print("Hash: %s" % block_chain[-1].hash)
