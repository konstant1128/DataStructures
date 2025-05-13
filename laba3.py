import timeit
from collections import defaultdict, deque


def is_complete_and_consistent_matrix(pairs):
    if not pairs:
        return (True, False)

    chars = set()
    for a, b in pairs:
        chars.add(a)
        chars.add(b)
    chars = list(chars)
    n = len(chars)
    char_to_index = {c: i for i, c in enumerate(chars)}

    adjacency_matrix = [[False] * n for _ in range(n)]
    for a, b in pairs:
        i = char_to_index[a]
        j = char_to_index[b]
        adjacency_matrix[i][j] = True

    in_degree = [0] * n
    for i in range(n):
        for j in range(n):
            if adjacency_matrix[i][j]:
                in_degree[j] += 1

    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    topo_order = []
    is_unique_order = True
    while queue:
        if len(queue) > 1:
            is_unique_order = False
        u = queue.popleft()
        topo_order.append(u)
        for v in range(n):
            if adjacency_matrix[u][v]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

    if len(topo_order) != n:
        return (False, True)
    else:
        return (is_unique_order, False)


def is_complete_and_consistent_list(pairs):
    if not pairs:
        return (True, False)

    graph = defaultdict(list)
    in_degree = defaultdict(int)
    all_chars = set()

    for a, b in pairs:
        graph[a].append(b)
        in_degree[b] += 1
        all_chars.add(a)
        all_chars.add(b)

    for c in all_chars:
        if c not in in_degree:
            in_degree[c] = 0

    queue = deque()
    for c in all_chars:
        if in_degree[c] == 0:
            queue.append(c)

    topo_order = []
    is_unique_order = True
    while queue:
        if len(queue) > 1:
            is_unique_order = False
        u = queue.popleft()
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(topo_order) != len(all_chars):
        return (False, True)
    else:
        return (is_unique_order, False)


def is_complete_and_consistent_defaultdict(pairs):
    return is_complete_and_consistent_list(pairs)


def compare_performance(pairs, num_runs=1000):
    print("\nСравнение производительности:")

    # Измеряем время для матричной реализации
    matrix_time = timeit.timeit(
        'is_complete_and_consistent_matrix(pairs)',
        globals=globals(),
        number=num_runs
    )
    print(f"Матричная реализация: {matrix_time:.5f} сек за {num_runs} запусков")

    # Измеряем время для реализации со списком смежности
    list_time = timeit.timeit(
        'is_complete_and_consistent_list(pairs)',
        globals=globals(),
        number=num_runs
    )
    print(f"Реализация со списком смежности: {list_time:.5f} сек за {num_runs} запусков")

    # Измеряем время для реализации с defaultdict
    defaultdict_time = timeit.timeit(
        'is_complete_and_consistent_defaultdict(pairs)',
        globals=globals(),
        number=num_runs
    )
    print(f"Реализация с defaultdict: {defaultdict_time:.5f} сек за {num_runs} запусков")

    # Определяем самую быструю реализацию
    fastest = min(matrix_time, list_time, defaultdict_time)
    if fastest == matrix_time:
        print("Вывод: Матричная реализация самая быстрая")
    elif fastest == list_time:
        print("Вывод: Реализация со списком смежности самая быстрая")
    else:
        print("Вывод: Реализация с defaultdict самая быстрая")


if __name__ == "__main__":
    print("Савченко К О 090304-РПИа-о24")
    pairs = [('b', 'c'), ('c', 'a'), ('a', 'd')]

    print("Реализация через матрицу смежности (массив):")
    complete, contradictory = is_complete_and_consistent_matrix(pairs)
    print(f"Полный порядок: {complete}, Противоречиво: {contradictory}")

    print("\nРеализация через список смежности (связный список):")
    complete, contradictory = is_complete_and_consistent_list(pairs)
    print(f"Полный порядок: {complete}, Противоречиво: {contradictory}")

    print("\nРеализация с использованием стандартной библиотеки Python:")
    complete, contradictory = is_complete_and_consistent_defaultdict(pairs)
    print(f"Полный порядок: {complete}, Противоречиво: {contradictory}")

    # Сравниваем производительность реализаций
    compare_performance(pairs)

    # Добавляем тест с большим количеством данных для демонстрации масштабируемости
    large_pairs = [(str(i), str(i + 1)) for i in range(100)]
    print("\nТестирование на большом наборе данных (100 пар):")
    compare_performance(large_pairs, num_runs=100)
