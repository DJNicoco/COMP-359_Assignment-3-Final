#include "FamilyTree.h"
#include <iomanip>

// Constructor to initialize the family tree with a root person (grandparent/great-grandparent. 
FamilyTree::FamilyTree(string rootName) {root = new Person(rootName);}

// Add a child to a parent node in the family ree 
void FamilyTree::addChild(Person* parent, string childName) 
{
    if (parent->leftChild == nullptr)
    {
        //if parent has no children, new child is added as the first child 
        parent->leftChild = new Person(childName);
    }
    else
    {
        //if parent already has kids, find the last sibling 
        Person* sibling = parent->leftChild;
        while (sibling->rightSibling != nullptr)
        {
            sibling = sibling->rightSibling; //traverse to the last sibling 
        }
        //new child is added as the next sibling. 
        sibling->rightSibling = new Person(childName);
    }
}

//Prints the family tree using a pre-order traversal approach. 
void FamilyTree::printTree(Person* node, string prefix)
{
    //base case, stops recursion if node is null 
    if (node == nullptr)
        return;

    //print current node 
    cout << prefix << node->name << endl;

    // using recursion, print all children of current node (IOW: print all leaves of tree)
    printTree(node->leftChild, prefix + "  ");

    // using recursion,. print all siblings of the current node 
    printTree(node->rightSibling, prefix);
}

/* *** Visualization of the tree using an ASCII representation. ***
* Here's how I envision it should be after I'm done: 
* grandparent
*  |--child 1
*       |--grandchild 1
*       |--grandchild 2
*  |--child 2
*       |--grandchild(1)1
*           |--great-grandchild 1
*       |--grandchild(1)2
*           |-- great-grandchild(1) 1
*           |-- great-grandchild(1) 2
*  |--child 3
*       |--grandchild(2)
*
* Where did I learn this? https://cplusplus.com/forum/general/58945/
* 
* This is the idea of how this will print out. This is an ASCII art visualization.
* I found this way the easiest as I am not very experienced in creating GUI visualizations in CPP.
* I would have taken some time to learn but felt like I won't have much time as the deadline is approaching.
* Maybe over the winter break I could learn this?
*
* Gosh I don't know if anyone will read this but working in CPP has been so refreshing. This assignment
* really helped me figure out how dynamic memory allocation, recursion, data structures, and etc work in CPP (finally).
* I couldn't for life of me figure this out when I was a younger college student.
*/
// Another note, pre-order traversal approach is also being used here. 
void FamilyTree::visualizeTree(Person* node, int depth)
{
    //bsae case
    if (node == nullptr)
        return;

    // ASCII art - prints out art that can show depth in the tree for visualization 
    cout << string(depth * 4, ' ') << "|-- " << node->name << endl;

    // using recursion, show children of the current node 
    if (node->leftChild) 
        visualizeTree(node->leftChild, depth + 1); 
    //using reucrsion show the siblings of current node 
    if (node->rightSibling)
        visualizeTree(node->rightSibling, depth);  
}
// Search for a person by name in the tree
Person* FamilyTree::search(Person* node, const string& name) 
{
    // base case: node/target person doesn't exist in the family tree
    if (node == nullptr) 
        return nullptr; 

    //ding ding ding, we found 'em!
    if (node->name == name) 
        return node; 

    // searches in the left subtree (children)
    Person* foundInChild = search(node->leftChild, name);
    if (foundInChild != nullptr)
        return foundInChild; // Found in children

    // searches in the right subtree (siblings)
    return search(node->rightSibling, name);
}



