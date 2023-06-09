import random

'''Считывает текстовый файл и делает список new_lines'''
def load_words(filename):
    new_lines = []
    with open(filename, 'r', encoding='utf-8') as f:  #кодировка utf-8
        for line in f.readlines():
            new_lines.append(line.strip("\n"))  #избавляемся от \n в конце каждого слова в списке

    return new_lines

'''Создает список word, в котором перемешиваются все элементы'''
def change_word(word):
    word = list(word)
    random.shuffle(word)
    #print(word)   hptnyo при вызове change_word(words[0])
    #print(''.join(word)) ['h', 'p', 't', 'n', 'y', 'o']  при вызове change_word(words[0])
    return ''.join(word)

'''Записывает статистику в history'''
def write_history(filename, user_name, score):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f'{user_name} {score} \n')

'''Вывод статистики'''
def read_history(filename):
    max = 0 #максимальное количество очков за игру
    count = 0 #сколько сыграно игр

    with open(filename, 'r', encoding='utf-8') as f:  #кодировка utf-8
        for line in f.readlines():
            count += 1
            score = int(line.split(' ')[1])  #в файле статистики разбивает строку-результат по пробелам
            if score > max:
                max = score

    return f'Всего игр сыграно: {count}\n ' \
           f'Максимальный рекорд: {max}'
