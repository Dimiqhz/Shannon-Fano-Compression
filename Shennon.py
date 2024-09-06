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

    # Сохраняем результат сжатия в файл
    compressed_text = "".join(i['code'] for i in sorted_compressor)
    with open("compressed_text.txt", "w") as output_file:
        output_file.write(compressed_text)

    # Сохраняем словарь в файл
    with open("dict.txt", "w", encoding="utf-8") as dict_file:
        for i in sorted_compressor:
            dict_file.write(f"Символ - {i['original']} :: Код - {i['code']}\n")

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


# Основная функция
if __name__ == '__main__':
    choice = int(input("Введите 1, чтобы ввести текст вручную, или 2, чтобы загрузить из файла: "))
    if choice == 1:
        text = input("Введите текст для сжатия: ")
    elif choice == 2:
        file_path = input("Укажите путь к файлу для загрузки текста: ")
        try:
            with open(file_path, 'r') as file:
                text = file.read()
        except FileNotFoundError:
            print(f"Файл '{file_path}' не найден.")
            exit()
    else:
        print("Выбрана неверная опция.")
        exit()

    print(f"Исходный текст: {text}")
    compress_data(text)
    print("Данные сохранены в файл compressed_text.txt")
    print("Словарь сохранен в файл dict.txt")
