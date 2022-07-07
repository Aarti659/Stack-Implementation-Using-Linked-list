//C++ Program to implement stack using linked list

#include <iostream.h>

#include <string.h>
 
using namespace std;
 
struct Node{
    int student_no;
    char student_name[50];
    int t;
    Node *next;
};
Node *top;
 
class stack{
 
public:
    void push(int n,char name[],int percent);
    void pop();
    void disp();
};
 
void stack :: push(int n,char name[],int percent)
{
    struct Node *newNode=new Node;
    
    newNode->student_no=n;
    newNode->t=percent;
    strcpy(newNode->student_name,name);
    
    newNode->next=top;
    
    top=newNode;
}
void stack ::pop()
{
    if(top==NULL){
        cout<<"List is empty!"<<endl;
        return;
    }
    cout<<top->student_name<<" is removed."<<endl;
    top=top->next;
}
void stack:: disp()
{
if(top==NULL){
        cout<<"List is empty!"<<endl;
        return;
    }
    struct Node *temp=top;
    while(temp!=NULL){
        cout<<temp->student_no<<" ";
        cout<<temp->student_name<<" ";
        cout<<temp->t<<" ";
        cout<<endl;
        temp=temp->next;
    }
    cout<<endl;
}
int main(){
 
    stack st;
    char ch;
    do{
    int n;
     
    cout<<"ENTER CHOICE\n"<<"1.Push\n"<<"2.Pop\n"<<"3.Display\n";
    cout<<"Make a choice: ";
    cin>>n;
     
    switch(n){
        case 1:  
            Node n;
            cout<<"Enter details of the element to be pushed : \n";
            cout<<"Roll Number : ";
            cin>>n.student_no;
            cout<<"Enter Name: ";
            std::cin.ignore(1);
            cin.getline(n.student_name,50);
            cout<<"Enter Percentage: ";
            cin>>n.t;
             
            
            st.push(n.student_no,n.student_name,n.t);
            break;
         
        case 2 : 
            
            st.pop();
            break;
         
        case 3 : 
            
            st.disp();
            break;
             
        default : 
            cout<<"Invalid Choice\n";
    }
     
    cout<<"Do you want to continue ? : ";
    cin>>ch;
 
    }while(ch=='Y'||ch=='y');
     
    return 0;
}
