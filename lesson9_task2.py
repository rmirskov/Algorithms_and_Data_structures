'''2. Закодируйте любую строку по алгоритму Хаффмана.'''

from collections import Counter

def encode_huffman(s):
    counter = Counter(s)
    ordered_counter = sorted(counter.items(), key=lambda x: x[1])
    alphabet = {let: '' for let, _ in ordered_counter}

    print('Процесс кодирования: ')
    while len(ordered_counter) != 1:
        print(ordered_counter)
        left = ordered_counter.pop(0)
        right = ordered_counter.pop(0)
        for let in left[0]:
            alphabet[let] = '0' + alphabet[let]
        for let in right[0]:
            alphabet[let] = '1' + alphabet[let]
        current_node = (left[0] + right[0], left[1] + right[1])
        i = 0
        while True:
            if (len(ordered_counter) == 0):
                ordered_counter.append(current_node)
                break
            elif (current_node[1] <= ordered_counter[i][1]):
                ordered_counter.insert(i, current_node)
                break
            elif (i == len(ordered_counter) - 1):
                ordered_counter.append(current_node)
                break
            i += 1
    print('Полученный алфавит: ', *alphabet.items(), sep='\n')
     
    return [alphabet[l] for l in s]

input_str = input('Введите строку для кодирования: ')
# input_str = 'beep boop beer!'
if len(set([l for l in input_str])) == 1:
    print('Кодировать нечего, так как вся строка состоит из одного символа.')
else:
    print(
        f'Результат кодирования по алгоритму Хаффмана для строки "{input_str}":\n',
        *encode_huffman(input_str), sep=' '
        )
