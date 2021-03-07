#include <iostream>
#include <vector>

class AddingArrayElements {
private:
    int N;
    int limit;
    std::vector<int> heap;
private:
    void swap(int e1, int e2);
    void buildHeap(std::vector<int> arr);
    void heapify(int nodeIndex);
    void insert(int element);

    int peek();
    int remove();
    int getLeftNodeIndex(int nodeIndex);
    int getRightNodeIndex(int nodeIndex);
    int getParentNodeIndex(int nodeIndex);
public:
    int numberOfOperationsRequired(int N, int limit, std::vector<int> arr);
    void print();
};

void AddingArrayElements :: print() {
    std::cout<<"\n";
    for(int element: heap) {
        std::cout<<element<<", ";
    }
}

int AddingArrayElements :: remove() {
    if(heap.size() < 2) return -1;
    
    int lastIndex = heap.size() - 1;
    swap(lastIndex, 1);
    int minElement = heap[lastIndex];
    heap.pop_back();
    heapify(1);

    return minElement; 
}

void AddingArrayElements :: insert(int element) {
    heap.push_back(element);
    int lastIndex = heap.size() - 1;
    
    while(lastIndex > 0 && heap[lastIndex] > heap[getParentNodeIndex(lastIndex)]) {
        heapify(lastIndex);
        lastIndex = getParentNodeIndex(lastIndex);
    }
}

int AddingArrayElements :: getParentNodeIndex(int nodeIndex){
    return nodeIndex / 2;
}

int AddingArrayElements :: peek() {
    return heap.size() < 2 ? 0 : heap[1]; 
}

int AddingArrayElements :: getLeftNodeIndex(int nodeIndex) {
    return 2*nodeIndex;
}

int AddingArrayElements :: getRightNodeIndex(int nodeIndex) {
    return (2*nodeIndex)+1;
}

void AddingArrayElements :: swap(int elemIndex1, int elemIndex2) {
    int temp = heap[elemIndex1];
    heap[elemIndex1] = heap[elemIndex2];
    heap[elemIndex2] = temp;
}

void AddingArrayElements :: heapify(int nodeIndex) {
    if(nodeIndex >= heap.size()) 
        return;

    int leftChildIndex = getLeftNodeIndex(nodeIndex);
    int rightChildIndex = getRightNodeIndex(nodeIndex);
    int minElementIndex = nodeIndex;

    if(leftChildIndex < heap.size() && heap[minElementIndex] > heap[leftChildIndex]) 
        minElementIndex = leftChildIndex;

    if(rightChildIndex < heap.size() && heap[minElementIndex] > heap[rightChildIndex]) 
        minElementIndex = rightChildIndex;

    if(minElementIndex != nodeIndex) {
        swap(nodeIndex, minElementIndex);
        heapify(minElementIndex);
    }
}

void AddingArrayElements :: buildHeap(std::vector<int> arr) {
    heap.push_back(0); // empty element for 1 based indexing.
    for(int element : arr)
        heap.push_back(element);

    int startIndex = (heap.size() / 2) + 1;
    while(startIndex--> 0) {
        heapify(startIndex);
    }
}

int AddingArrayElements :: numberOfOperationsRequired(int N, int limit, std::vector<int> arr) {
    this->buildHeap(arr);
    this->print();
    int operationsRequired = 0;
    while(peek() < limit) {
        int first = remove();
        int second = remove();
        int newElement = first + second;
        insert(newElement);
        this->print();
        operationsRequired++;
    }
    return operationsRequired;
}

int main() {
    int N = 6, K = 6;
    std::vector<int> s{1,10,12,9,2,3};

    AddingArrayElements solution;
    int result = solution.numberOfOperationsRequired(N, K, s);
    std::cout<<"\n#Case 1: " << result;
    return 0;
}