import math
from collections import defaultdict


class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


def calculate_pair_frequencies(text):
    frequencies = defaultdict(int)
    for i in range(len(text) - 1):
        pair = text[i:i + 2]
        frequencies[pair] += 1

    # Добавить символы, которые встречаются только один раз
    for char in text:
        if char not in frequencies:
            frequencies[char] = 1

    return frequencies


def build_huffman_tree(frequencies):
    nodes = []
    for char, freq in frequencies.items():
        node = HuffmanNode(char, freq)
        nodes.append(node)

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)

        merged_node = HuffmanNode(None, left.freq + right.freq)
        merged_node.left = left
        merged_node.right = right

        nodes.append(merged_node)

    return nodes[0]


def build_huffman_codes(tree):
    codes = {}

    def traverse(node, code=""):
        if isinstance(node, HuffmanNode):
            if node.char:
                codes[node.char] = code
            else:
                traverse(node.left, code + "0")
                traverse(node.right, code + "1")

    traverse(tree)
    return codes


def calculate_bits(text, codes):
    encoded_text = "".join(codes.get(char, "") for char in text)  # Добавлено обращение к `.get()` для проверки наличия символа в словаре
    num_bits = len(encoded_text)
    return encoded_text, num_bits


def calculate_shannon_entropy(frequencies):
    total_freq = sum(frequencies.values())
    entropy = 0
    for freq in frequencies.values():
        prob = freq / total_freq
        entropy += prob * math.log2(1 / prob)
    return entropy

def lzw_compress(text):
    codes = {chr(i): i for i in range(256)}
    current_code = 256
    encoded_text = []
    buffer = ""
    for char in text:
        new_buffer = buffer + char
        if new_buffer in codes:
            buffer = new_buffer
        else:
            encoded_text.append(codes[buffer])
            codes[new_buffer] = current_code
            current_code += 1
            buffer = char
    encoded_text.append(codes[buffer])
    return encoded_text

def calculate_lzw_bits(text):
    encoded_text = lzw_compress(text)
    max_code = max(encoded_text)
    num_bits = math.ceil(math.log2(max_code + 1))
    num_bits *= len(encoded_text)
    return num_bits


def encode_text(input_file, output_file):
    with open(input_file, "r") as file:
        text = file.read()

    frequencies = calculate_pair_frequencies(text)
    tree = build_huffman_tree(frequencies)
    codes = build_huffman_codes(tree)
    encoded_text, num_bits = calculate_bits(text, codes)
    shannon_entropy = calculate_shannon_entropy(frequencies)
    with open(output_file, "w") as file:
        file.write(encoded_text)

    lzw_bits = calculate_lzw_bits(text)
    print("Количество информации (Шеннон):", shannon_entropy)
    print("Количество битов (LZW):", lzw_bits)
    print("Количество битов (Хаффман):", num_bits)

encode_text("in.txt", "out.txt")




