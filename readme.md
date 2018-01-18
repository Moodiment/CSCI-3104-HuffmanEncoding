## Huffman Encode
This is a apart of a homework Assignment for algorithms.  The objective of this assignment was to output the raw 'bits' required to encode a specific string fed into the python script.

### Minor Technical Explaination:
This implementation uses a minheap to initialize all nodes that will be used for the Huffman encoding. It continually deletes the two least-frequent nodes in the minheap, sums those nodes, and adds it back into the minheap to build the huffman encoding. 
