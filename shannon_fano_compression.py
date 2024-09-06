from collections import Counter

def compress_data(data):
    processed = []
    compressor = []
    total_length = len(data)

    for char, count in Counter(data).items():
        var = count / total_length
        comp = {'original': char, 'count': count, 'code': '', 'probability': var}
        compressor.append(comp)

    sorted_compressor = sorted(compressor, key=lambda x: x['probability'], reverse=True)
    split = splitter([i['probability'] for i in sorted_compressor], 0)
    encoder(sorted_compressor, split)

    compressed_text = "".join(i['code'] for i in sorted_compressor)
    with open("compressed_text.txt", "w") as output_file:
        output_file.write(compressed_text)

    with open("dict.txt", "w", encoding="utf-8") as dict_file:
        for i in sorted_compressor:
            dict_file.write(f"The sybmol is - {i['original']} :: Code - {i['code']}\n")

    return compressed_text


def splitter(probability, pointer):
    diff = sum(probability[:pointer + 1]) - sum(probability[pointer + 1:])
    if diff < 0:
        point = splitter(probability, pointer + 1)
        diff_1 = sum(probability[:point]) - sum(probability[point:])
        diff_2 = sum(probability[:point + 1]) - sum(probability[point + 1:])
        return point - 1 if abs(diff_1) < abs(diff_2) else point
    else:
        return pointer


def encoder(compressor, split):
    if split > 0:
        part_1 = compressor[:split + 1]
        for i in part_1:
            i['code'] += '0'
        if len(part_1) > 1:
            encoder(part_1, splitter([i['probability'] for i in part_1], 0))
        part_2 = compressor[split + 1:]
        for i in part_2:
            i['code'] += '1'
        if len(part_2) > 1:
            encoder(part_2, splitter([i['probability'] for i in part_2], 0))
    elif split == 0:
        part_1 = compressor[:split + 1]
        for i in part_1:
            i['code'] += '0'
        part_2 = compressor[split + 1:]
        for i in part_2:
            i['code'] += '1'

if __name__ == '__main__':
    choice = int(input("Enter 1 to enter text manually, or 2 to download from a file: "))
    if choice == 1:
        text = input("Enter the text to compress: ")
    elif choice == 2:
        file_path = input("Specify the path to the file to download the text: ")
        try:
            with open(file_path, 'r') as file:
                text = file.read()
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            print('Developed by Dimiqhz')
            exit()
    else:
        print("The wrong option is selected.")
        print('Developed by Dimiqhz')
        exit()

    print(f"The source text: {text}")
    compress_data(text)
    print("The data is saved to a file compressed_text.txt")
    print("The dictionary is saved to a file dict.txt")
    print('Developed by Dimiqhz')
