#include <iostream>
#include <vector>
#include <unordered_set>

const int max_size = 30005;
const int int_max = 2147483647;

class disjoint_set {
private:
    int parent[max_size];
    int rank[max_size];

    int find(int c) {
        if(parent[c] != c) {
            parent[c] = find(parent[c]);
            return parent[c];       
        }
        return c;
    }
 
public:
    disjoint_set() {
        for(int i=0; i<max_size;i++){
            parent[i] = i;
            rank[i] = 1;
        }
    }

    int get_size(int child) {
        int parent = find(child);
        return rank[parent];
    }

    void make_union(int c1, int c2) {
        int p1 = find(c1);
        int p2 = find(c2);
        
        if(p1 == p2) return;

        if(rank[p1] > rank[p2]) {
            rank[p1] += rank[p2];
            parent[p2] = p1;
        } else{
            rank[p2] += rank[p1];
            parent[p1] = p2;
        }
    }
};

int main() {

    int size;
    std::cin>>size;

    disjoint_set dj;
    std::unordered_set<int> nodes;

    for(int i=0; i<size; i++) {
        int start, dest;
        std::cin >> start >> dest;
        nodes.insert(start);
        nodes.insert(dest);
        dj.make_union(start, dest);
    }
    
    int min = int_max;
    int max = 0;
    for(auto it = nodes.begin(); it != nodes.end(); it++) {
        int current_node = *it;
        int current_size = dj.get_size(current_node);
        if(current_size == 1) continue;
        if(min > current_size) min = current_size;
        if(max < current_size) max = current_size;
    }

    std::cout<<min<<' '<< max;

    return 0;
}

