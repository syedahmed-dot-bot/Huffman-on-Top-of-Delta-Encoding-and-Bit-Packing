from collections import Counter
import heapq

def get_frequencies(chunks):
    return Counter(chunks) 

class Node:
    def __init__(self, element, freq):
        self.element = element
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
    
def build_huffman_tree(frequencies):
    heap = [Node(element, freq) for element, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, current_node = '', code_map = {}):
    if node is None:
        return
    
    if node.element is not None:
        code_map[node.element] = current_node

    generate_codes(node.left, current_node + '0', code_map)
    generate_codes(node.right, current_node + '1', code_map)    

    return code_map

def encode_list(chunks, code_map):
    return ''.join(code_map[element] for element in chunks)