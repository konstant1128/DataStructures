#include <iostream>
#include <cstdlib>
#include <vector>
#include <climits>
#include <chrono>
#include <random>
#include <cassert>
using namespace std;
using namespace std::chrono;

class StackArray
{
private:
    int top;
    int* arr;
    int capacity;
public:
    StackArray(int initialCapacity = 10) 
    {
        arr = new int[initialCapacity];
        top = -1;
        capacity = initialCapacity;
    }

    ~StackArray() 
    {
        delete[] arr;
    }

    void resize() 
    {
        int newCapacity = capacity * 2;
        int* newArr = new int[newCapacity];
        for (int i = 0; i <= top; i++) 
        {
            newArr[i] = arr[i];
        }
        delete[] arr;
        arr = newArr; 
        capacity = newCapacity;
        cout << "Stack resized to " << newCapacity << endl;
    }

    bool is_empty() const
    {
        return (top < 0);
    }

    void push(int x)
    {
        if(top == capacity - 1)
        {
            resize();
        }
        arr[++top] = x; 
        cout << "Element " << x << " pushed to stack!" << endl; 
    }

    int pop()
    {
        if(is_empty())
        {
            cerr << "Stack is empty!" << endl;
            return -1;
        }
        return arr[top--];
    }

    int peek() const
    {
        if (is_empty()) 
        {
            cerr << "Stack is empty!" << endl; 
            return -1; 
        }
        return arr[top];
    }

    int size() const  
    {
        return top + 1;
    }
};

class Node {
public:
    int data;
    Node* next;
    Node(int new_data) {
        this->data = new_data;
        this->next = nullptr;
    }
};

class StackLinkedList 
{
    Node* head;
    
public:
    StackLinkedList() { this->head = nullptr; }  
    
    bool is_empty() const  
    {
        return head == nullptr;
    }
    
    void push(int new_data) 
    {
        Node* new_node = new Node(new_data);
        if (!new_node) 
        {
            cout << "\nStack Overflow";
            return; 
        }
        new_node->next = head;
        head = new_node;
    }
    
    int pop()  
    {
        if (this->is_empty()) 
        {
            cout << "\nStack Underflow" << endl;
            return INT_MIN;
        }
        Node* temp = head;
        int popped_value = temp->data;
        head = head->next;
        delete temp;
        return popped_value;
    }
    
    int peek() const  
    {
        if (!is_empty())
            return head->data;
        else {
            cout << "\nStack is empty";
            return INT_MIN;
        }
    }
    
    int size() const
    {
        int count = 0;
        Node* current = head;
        while (current != nullptr) {
            count++;
            current = current->next;
        }
        return count;
    }
};

class StackSTL 
{
private:
    vector<int> items;  
public:
    StackSTL() {}
    
    bool is_empty() const 
    {
        return items.empty(); 
    }
    
    void push(int item) 
    {
        items.push_back(item); 
    }
    
    int pop() 
    {
        if (is_empty()) 
        {
            cerr << "Stack is empty!" << endl;
            return -1;
        }
        int top_item = items.back();
        items.pop_back();
        return top_item; 
    }
    
    int peek() const 
    {
        if (is_empty()) 
        {
            cerr << "Stack is empty!" << endl; 
            return -1; 
        }
        return items.back();
    }
    
    size_t size() const 
    {
        return items.size(); 
    }
};

//функция для тестирования производительности реализации
template<typename StackType>
void TestPerformance(const string& name, int operations = 100000)
{
    StackType stack;
    auto start = high_resolution_clock::now();
    //push тест
    for (int i = 0; i < operations; ++i)
    {
        stack.push(i);
    }
    auto push_end = high_resolution_clock::now();
    //pop тест
    for (int i = 0; i < operations; ++i)
    {
        stack.pop();
    }
    auto end = high_resolution_clock::now();
    auto push_duration = duration_cast<milliseconds>(push_end - start);
    auto pop_duration = duration_cast<milliseconds>(end - push_end);
    auto total_duration = duration_cast<milliseconds>(end - start);
    cout<<name<<"performance: \n"<<"push: "<<push_duration.count()<<"ms\n"<<"pop: "<<pop_duration.count()<<"ms\n"
    <<"total: "<<total_duration.count()<<"ms\n"<<"("<<operations<<" operations each)\n"<<endl;
}

//функция для тестирования работоспособности реализаций
void FuncionalityTest()
{
    StackArray sa;
    assert(sa.is_empty());
    sa.push(1);
    assert(!sa.is_empty());
    assert(sa.peek() == 1);
    assert(sa.pop() == 1);
    assert(sa.is_empty());

    StackLinkedList sll;
    assert(sll.is_empty());
    sll.push(1);
    assert(!sll.is_empty());
    assert(sll.peek() == 1);
    assert(sll.pop() == 1);
    assert(sll.is_empty());

    StackSTL sstl;
    assert(sstl.is_empty());
    sstl.push(1);
    assert(!sstl.is_empty());
    assert(sstl.peek() == 1);
    assert(sstl.pop() == 1);
    assert(sstl.is_empty());

    cout<<"All funcionality tests passed!\n"<<endl;
}

int main()
{
    cout<<"Савченко К.О. 090304-РПИа-о24"
    //тестируем работоспособность реализаций стека
    FuncionalityTest();

    //тестируем производительность реализаций стека
    const int Test_Size = 100000;
    cout<<"Performance comparison (operations: "<<Test_Size<<");"<<endl;
    TestPerformance<StackArray>("StackArray", Test_Size);
    TestPerformance<StackLinkedList>("StackLinkedList", Test_Size);
    TestPerformance<StackSTL>("StackSTL", Test_Size);

    system("pause>nul");
    return 0;
}
