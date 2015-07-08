class Node:
    def __init__(self,value=None,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
        self.position = ''

def inorder(node):
    if node == None:
        return 
    inorder(node.left)
    print node.value
    inorder(node.right)

def create_huffman_tree(values):
    root = None
    nodes = []
    for value in values:
        nodes.append(Node(value))
    while len(nodes) > 1:
        nodes = sorted(nodes,key=lambda node: node.value[0])
        root = Node((nodes[0].value[0]+nodes[1].value[0],'*'),nodes[0],nodes[1])
        left = nodes[0]
        left.position = '0'
        right = nodes[1]
        right.position = '1'
        del nodes[0]
        del nodes[0]
        thing = (left.value[0]+right.value[0],'*')
        root = Node(thing,left,right)
        nodes.append(root)
    return root

def compress(text):
    frequencies = {}
    values = []
    
    for character in text:
        if character not in frequencies:
            frequencies[character] = 0
        frequencies[character] += 1
    for key in frequencies:
        values.append((key,frequencies[key]))
    
    root = create_huffman_tree(values)
    

def decompress(text):
    pass 

if __name__ == '__main__':
    values = [
        (5,'1'),
        (7,'2'),
        (10,'3'),
        (15,'4'),
        (20,'5'),
        (45,'6')
    ]
    
    input_text = "hello. my name is Bao."
    compress(input_text)
