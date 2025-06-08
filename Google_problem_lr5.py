from collections import Counter
import re
import time

def preprocess_text(file_path):
    #Загружает текст, разбивает на слова, строит частотный словарь и индекс для быстрого поиска
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    #Удаляем знаки препинания
    words = re.findall(r'\b\w+\b', text)
    #Строим частотный словарь
    word_counts = Counter(words)
    #Строим индекс: слово -> все слова, содержащие его как подстроку
    #Для ускорения поиска используем словарь, где ключ - подстрока
    substring_index = {}
    for word in word_counts:
        # Для каждого возможного подстрокового запроса (длиной >=3) добавляем слово в индекс
        for i in range(len(word) - 2):
            substring = word[i:i+3]
            if substring not in substring_index:
                substring_index[substring] = []
            substring_index[substring].append(word)
    return word_counts, substring_index

def find_matching_words(query, word_counts, substring_index):
    #Находит слова, содержащие подстроку, сортирует по частоте
    query = query.lower()
    if len(query) < 3:
        return []
    #Находим все слова, содержащие подстроку (используя индекс по первым 3 символам)
    matching_words = set()
    start_substring = query[:3]
    if start_substring in substring_index:
        for word in substring_index[start_substring]:
            if query in word:
                matching_words.add(word)
    #Сортируем по частоте (по убыванию)
    sorted_words = sorted(matching_words, key=lambda x: (-word_counts[x], x))
    return sorted_words

#Предварительная обработка текста
start_time = time.time()
word_counts, substring_index = preprocess_text("war.txt")
preprocessing_time = time.time() - start_time
print(f"Предварительная обработка заняла: {preprocessing_time:.2f} секунд")

#Обработка запросов
while True:
    query = input("\nВведите запрос (не короче 3 символов) или 'exit' для выхода: ")
    if query.lower() == 'exit':
        break
    if len(query) < 3:
        print("Запрос должен быть не короче 3 символов")
        continue
    start_time = time.time()
    results = find_matching_words(query, word_counts, substring_index)
    search_time = time.time() - start_time
    print(f"\nРезультаты для '{query}' (время поиска: {search_time:.4f} сек):")
    for i, word in enumerate(results, 1):
        print(f"{i}. {word} (встречается {word_counts[word]} раз)")
        
