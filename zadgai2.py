import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_code(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    root = heap[0]
    codes = {}
    def generate_codes(node, prefix=''):
        if node.char is not None:
            codes[node.char] = prefix
        else:
            generate_codes(node.left, prefix + '0')
            generate_codes(node.right, prefix + '1')

    generate_codes(root)
    return codes

# Жишээ
frequencies = {'A': 8, 'B': 3, 'C': 1, 'D': 1}
result = huffman_code(frequencies)
print(result)