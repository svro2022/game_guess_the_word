from utils import load_words, change_word, write_history, read_history

#по правилам хорошего тона, принято обозначать файлы как переменные + в случае изменения не надо искать по всему коду
words_txt = 'words.txt'
history_txt = 'history.txt'

#Другой вариант ввода
#print("Введите ваше имя")
#user_name = input()

user_name = input('Введите ваше имя\n')
words = load_words(words_txt)  #создаем переменную - список из функции load_words
score = 0  # счетчик правильных ответов

for word in words:
    print(change_word(word))
    user_answer = input()

    if user_answer.lower().strip(' ') == word: #к нижнему регистру (в списке нижний) и удаляем пробелы
        print(f'Верно! Вы получаете 10 очков.')
        score += 10
    else:
        print(f'Неверно! Верный ответ – {word}.')


write_history(history_txt, user_name, score)
print(read_history(history_txt))
