from typing import *
from dataclasses import dataclass

@dataclass
class NodeTree:
    left: Union['NodeTree', str] 
    right: Union['NodeTree', str] 

    def children(self):
        return self.left, self.right

def huffman_code_tree(node: Union[NodeTree, str], binString: str = '') -> Dict[str, str]:
    if isinstance(node, str):
        return {node: binString}
    l, r = node.children()
    d = {}
    d.update(huffman_code_tree(l, binString + '0'))
    d.update(huffman_code_tree(r, binString + '1'))
    return d

string = input('Enter string to be compressed: ')

freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key = lambda x: x[1], reverse = True)

nodes = freq

while len(nodes) > 1:
    key1, c1 = nodes[-1]
    key2, c2 = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key = lambda x: x[1], reverse = True)

huffmanCode = huffman_code_tree(nodes[0][0])

encodedStr = ''
for i in string:
    encodedStr += huffmanCode[i]

for (char, frequency) in freq:
    print(f'{char} | {huffmanCode[char]}')
print(f'Original string encoded: {encodedStr}')
