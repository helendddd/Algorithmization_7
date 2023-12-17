import heapq


def procedurehuffman(f):
    heap = []
    buffer_fs = set()

    for symbol, frequency in f.items():
        heapq.heappush(heap, (frequency, symbol))
    while len(heap) > 1:
        f1, i = heapq.heappop(heap)
        f2, j = heapq.heappop(heap)
        fs = f1 + f2
        ord_val = ord('a')
        fl = str(fs)
        while fl in buffer_fs:
            symb = chr(ord_val)
            fl = str(fs) + " " + symb
            ord_val += 1
        buffer_fs.add(fl)
        f[fl] = {f"{x}": f[x] for x in [i, j]}
        del f[i], f[j]
        heapq.heappush(heap, (fs, fl))
    return f


def huffman_codes(tree, codes, path=''):
    for i, (node, child) in enumerate(tree.items()):
        # Если child - это лист, добавляем его в код
        if isinstance(child, int):
            codes[node] = path[1:] + str(abs(i-1))
        else:
            # Если child - это словарь, продолжаем рекурсивно
            huffman_codes(child, codes, path + str(abs(i-1)))
    return codes


def huffman_encode(data, codes):
    encoded_data = ''.join(codes[char] for char in data)
    return encoded_data


def huffman_decode(encoded_data, codes):
    decoded_data = ''
    current_code = ''
    for bit in encoded_data:
        current_code += bit
        for char, code in codes.items():
            if code == current_code:
                decoded_data += char
                current_code = ''
                break
    return decoded_data


if __name__ == "__main__":
    input_string = "Hello Word!"
    frequency = {}

    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    for char, count in frequency.items():
        print(f"'{char}': {count} раз")

tree = procedurehuffman(frequency)
print(tree)
code = huffman_codes(tree, dict())
print("code", code)
encoded_data = huffman_encode(input_string, code)
decoded_data = huffman_decode(encoded_data, code)

print(f"Original Data: {input_string}")
print(f"Encoded Data: {encoded_data}")
print(f"Decoded Data: {decoded_data}")
