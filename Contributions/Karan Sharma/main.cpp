#include "FamilyTree.h"
#include <iostream>
using namespace std;
//I used OOP in CPP for this. To get a refresher, I referred to: https://www.w3schools.com/cpp/cpp_oop.asp
//For BST: https://www.geeksforgeeks.org/cpp-binary-search-tree/

// recursive function to add children 
// asks for child's name, asks if that child has further childern and so on. 
void dynamicInteractiveChildrenAddition(FamilyTree& tree, Person* parent) {
    int numChildren;

    // pretty self explanatory 
    cout << "\nHow many children does " << parent->name << " have? ";
    cin >> numChildren;
    cout << endl;


    for (int i = 0; i < numChildren; ++i) {
        string childName;

        // prompts for each child's name
        cout << "Enter the name of child " << i + 1 << " of " << parent->name << ": ";
        cin >> childName;
        cout << endl;

        // adds that child to their corresponding parent
        tree.addChild(parent, childName);

        // finds the newly added child in the parent's children list
        Person* newChild = parent->leftChild;

        // this while loop allows for traversal to the last sibling (newly added child)
        while (newChild->rightSibling != nullptr) 
            newChild = newChild->rightSibling;
        

        // check if the newly added child has their own children
        char addGrandchildren;
        cout << "Does " << childName << " have children? (y/n): ";
        cin >> addGrandchildren;
        cout << endl;

        //recurses back to the beginning to add any potential grandchildren/great-grandchildren
        if (addGrandchildren == 'y' || addGrandchildren == 'Y') {
            dynamicInteractiveChildrenAddition(tree, newChild); 
        }
    }
}

int main() {
    // initialize the family tree
    string grandparentName;
    cout << "Enter the name of the grandparent: ";
    cin >> grandparentName;

    //add grandparent
    FamilyTree family(grandparentName);

    // add children/grandchildren/greatgrandchildren to the grandparent 
    dynamicInteractiveChildrenAddition(family, family.root);

    //searching begins here
    char search; 
    cout << "Would you like to search for a person in the tree? (y/n): ";
    cin >> search; 
    cout << endl; 

    if (search == 'y' || search == 'Y')
    {
        // who would you like to search for?
        string targetName;
        cout << "\nEnter the name of the person to search for: ";
        cin >> targetName;
        cout << endl; 

        //searches the tree using the foundPerson member function in FamilyTree.h defined in FamilyTree.cpp
        Person* foundPerson = family.search(family.root, targetName);
        //if found: output. if not found: other output
        if (foundPerson)
            cout << foundPerson->name << " is a part of this family tree." << endl;
        else
            cout << targetName << " is not part of the familyTree.\n";
    }
    
    // ASCII art visual representation of the family tree. 
    cout << "\nFamily Tree Visualization:\n";
    family.visualizeTree(family.root);

   

    return 0;
}