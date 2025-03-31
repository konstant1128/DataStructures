#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main() 
{
    cout << "Savchenko Konstantin Olegovich 090304-RPIa-o24" << endl;
    int N;
    cout << "Enter your number from 1 to 10^6" << endl;
    cin >> N;
    if (N <= 0 || N > 1000000) 
    {
        cout << "Please enter a number between 1 and 10^6." << endl;
        return 1;
    }
    // Массив для хранения предыдущих остатков
    vector<int> parent(N, -1); // parent - предыдущий остаток
    vector<int> digit(N, -1);  // digit - последняя добавленная цифра (всегда 1)
    vector<int> length(N, 0);  // length - длина числа
    // Очередь для BFS по остаткам
    vector<int> queue;
    queue.push_back(1 % N);
    parent[1 % N] = -1; // Начальное состояние
    digit[1 % N] = 1;
    length[1 % N] = 1;
    bool found = false;
    int result_rem = 0;
    while (!queue.empty()) 
    {
        int current_rem = queue.front();
        queue.erase(queue.begin());
        if (current_rem == 0) 
        {
            found = true;
            result_rem = current_rem;
            break;
        }
        // Пробуем добавить 1 в конец
        int next_rem = (current_rem * 10 + 1) % N;
        if (parent[next_rem] == -1) 
        {
            parent[next_rem] = current_rem;
            digit[next_rem] = 1;
            length[next_rem] = length[current_rem] + 1;
            queue.push_back(next_rem);
        }
    }
    if (found) 
    {
        // Восстанавливаем число по остаткам
        string number;
        int rem = result_rem;
        while (rem != -1) 
        {
            number = to_string(digit[rem]) + number;
            rem = parent[rem];
        }
        cout << number << endl;
    } else 
    {
        cout << "NO" << endl;
    }
    cout << "Press Enter to continue..." << endl;
    cin.ignore();
    cin.get();
    return 0;
}
