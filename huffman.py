class Node:
    def __init__(self,value=None,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
        self.position = ''
    
    def is_leaf(self):
        return self.left == self.right == None
            

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
        root = Node(('*',nodes[0].value[1]+nodes[1].value[1]),nodes[0],nodes[1])
        left = nodes.pop(0)
        left.position = '0'
        right = nodes.pop(0)
        right.position = '1'
        thing = (left.value[0]+right.value[0],'*')
        root = Node(thing,left,right)
        nodes.append(root)
    return root

def compress(text):
    frequencies = {}
    values = []
    print 'input: %d bits.' % (len(text) * 8)
	
	# get frequencies and characters
    for character in text:
        if character not in frequencies:
            frequencies[character] = 0
        frequencies[character] += 1
    for key in frequencies:
        values.append((frequencies[key],key))
    # create tree
    root = create_huffman_tree(values)
    
	# created tree, now to encode
    codes = {}
    code = ''
    # post-order traversal
    parent_stack = []
    current = root 
    while len(parent_stack) > 0 or current != None:
        if current != None:
            parent_stack.append(current)
            if current.left != None:
                code += '0'
            current = current.left
        else:
            current = parent_stack.pop()
            code = code[:-1]
            
            # visit
            if current != None and current.is_leaf():
                codes[current.value[1]] = code
            
            if current.right != None:
                code += '1'
            current = current.right
        print code
    
    # store huffman tree into code
    for c in codes:
        print c,codes[c]
    
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
    
    input_text = "test"
    compress(input_text)
