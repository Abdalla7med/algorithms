//create a structure for hash table with seperate chainning
// this defntition to hash strings because it's the most complicated one 
#include <bits/stdc++.h>
#inclulde<vector.h>
using namespace std;
// forward declaration to make it friend at Node class
class HashTable;
class Node
{
    protected:
      string val;
      Node*next;
    Node(){
        this->val=0;
        this->next=NULL;
    }
    Node(string val){
        this->val=val;
        this->next=NULL;
    }
    friend class HashTble;
   
}
class HashTable
{
   private:
      int n;
      int m;
      vector<Node*>chain;
  
        int hashFunction(string value){
            long long sum=0;
            for(int i=1;i<=value.length();i++)
            sum+=(i*value[i-1]);
        return sum%599;  
            // using universal hashing techinque by using random prime number :
            // p which is this case is 599 h(k)= (sum all char in k * position of this char ) % p->599
        }
    public:
        string get(string key){
        int index=hashFunction(key);
        if(index > n){
            cout<<"not founded";
            return "";
        }
        if(chain[index]){
            Node*temp=chain[index];
            while(temp){
            if(temp->val=key){
                return temp->val;
            }
            temp=temp->next;
            }
            cout<<"not founded";
            return "";
        }
          cout<<"not founded";
          return "";
        }
        void add(string value){
        int index=hashFunction(value);
        if(index > n){
            cout<<"not founded";
            return "";
        }
        if(chain[index]!=NULL){
            Node*temp=chain[index];
            while(temp->next!=null){
                temp=temp->next;
            }
            temp->next=new Node(value);
         }
         chain[index]=new Node(value);
        }
        HashTable(int n)
        {
            chain=vector<Node*>(n);
            this->n=n;
        }
        HashTable()
        {
            chain=vector<Node*>(INT_MAX);
            this->n=INT_MAX;
        }
        int resize(int n)
        {
            this->n=n;
        }

}

int main(){
    HashTable HT=new HashTable();
}