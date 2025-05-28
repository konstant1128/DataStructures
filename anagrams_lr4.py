#импортируем Counter для подсчета символов в слове
from collections import Counter
#импортируем time для замера времени поиска анграмм
import time

#функция загрузки словаря
def load_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        #cчитываем файл построчно, убираем пробелы и приводим к нижнему регистру и возвращаем мн-во
        return set(line.strip().lower() for line in file)

#функция поиска анаграмм
def find_anagrams(input_word, dictionary):
    #счетчик символов слова
    input_counter = Counter(input_word.lower())
    result = []
    #поиск слова в словаре
    for word in dictionary:
        word_counter = Counter(word.lower())
        #проверка того, что все символы текущего слова есть во введенном слове
        # и их количество не превышает количество во введенном слове
        if all(word_counter[char] <= input_counter[char] for char in word_counter):
            result.append(word)
    #сортировка результатов сначала по убыванию длины слова, затем по алфавиту
    result.sort(key=lambda x: (-len(x), x))
    return result

start_time = time.time()
dictionary = load_dictionary("nouns.txt")
input_word = input("Введите ваше слово:: ")
before_anagram_time = time.time()
anagrams = find_anagrams(input_word, dictionary)
after_anagram_time = time.time()
print(anagrams)

end_time = time.time()
print("\n--- Время выполнения ---")
print(f"Загрузка словаря: {before_anagram_time - start_time:.4f} секунд")
print(f"Поиск анаграмм: {after_anagram_time - before_anagram_time:.4f} секунд")
print(f"Общее время: {end_time - start_time:.4f} секунд")
