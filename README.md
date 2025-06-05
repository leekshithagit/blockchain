# Blockchain Implementation:

this is a simple implementation of blockchain using python with proof of work consensus

## Features:

- Block is created with the details: index, timestamp, data, nonce, cryptographic hash, previous block's hash
- Proof-of-work mining with adjustable difficulty, to make the process of hashing a bit slower
- Validating chain with tamper detection
- Mining performance metrics

## How it works:

### Core components:
1.**Block Class**
  - Stores transaction 'data' 
  - calculates 'hash' using sha256
  - links the block to 'previous_hash'
  - represents all the details of the block
2.**Block_chain Class:
 - creates array to maintain the 'chain' of valid blocks
 - initialises the 'genesis block'
 - adds 'new block' to chain
 - provides 'proof-of-work' for block('mine_block()')
 - validates the chain integrity('is_valid()')

# Proof-of-work mining:

- until hash of the block starts with 'DIFFICULTY * "0" ', nonce keeps on increasing by 1
- as nonce is included in process of calculating hash, hash gets updated every time
- this makes the process of calculating hash slower

# Usage :

    """Initialize blockchain"""
    bc = Blockchain()

    """"Add blocks (automatically mines)"""
    bc.add_block("Alice pays Charlie 3 NC")

    """Print __str__ output
    print(bc.chain[-1])

    """Validate chain"""
    print(bc.is_valid())
    """Returns True if chain is untampered"""

    bc.add_block("Striver pays Alice 5.2 NC")

    print(bc.chain[-1])

    print(bc.is_valid())

#Example output:
    Mining the block 1
    time taken to create hash : 0.0347 seconds
    final nonce value is : 354 and the hash : 00a4f8....

    Block 1 [
    Timestamp: ...
    Data: ...
    ]

    True

    Mining the block 2
    time taken to create hash : 0.0274 seconds
    final nonce value is : 128 and the hash : 00c7d3....

    Block 2 [
    Timestamp: ...
    Data: ...
    ]

    False

#Customisation : 

DIFFICULTY can be changed from "2" to "3" or something
