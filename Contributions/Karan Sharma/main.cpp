#include "FamilyTree.h"
#include <iostream>
using namespace std;
//I used OOP in CPP for this. To get a refresher, I referred to: https://www.w3schools.com/cpp/cpp_oop.asp
//For BST: https://www.geeksforgeeks.org/cpp-binary-search-tree/

// Recursive function to add children interactively
void dynamicInteractiveChildrenAddition(FamilyTree& tree, Person* parent) {
    int numChildren;

    // Explicitly state whose children are being entered
    cout << "\nHow many children does " << parent->name << " have? ";
    cin >> numChildren;
    cout << endl;

    for (int i = 0; i < numChildren; ++i) {
        string childName;

        // Prompt for each child’s name
        cout << "Enter the name of child " << i + 1 << " of " << parent->name << ": ";
        cin >> childName;
        cout << endl;

        // Add the child to the parent
        tree.addChild(parent, childName);

        // Find the newly added child in the parent's children list
        Person* newChild = parent->leftChild;
        while (newChild->rightSibling != nullptr) {
            newChild = newChild->rightSibling; // Traverse to the last sibling (newly added child)
        }

        // Check if the newly added child has their own children
        char addGrandchildren;
        cout << "Does " << childName << " have children? (y/n): ";
        cin >> addGrandchildren;
        cout << endl;

        if (addGrandchildren == 'y' || addGrandchildren == 'Y') {
            dynamicInteractiveChildrenAddition(tree, newChild); // Recursive call for grandchildren
        }
    }
}

int main() {
    // Start the family tree
    string grandparentName;
    cout << "Enter the name of the grandparent: ";
    cin >> grandparentName;

    FamilyTree family(grandparentName);

    // Add children to the grandparent interactively
    dynamicInteractiveChildrenAddition(family, family.root);

    char search; 
    cout << "Would you like to search for a person in the tree? (y/n): ";
    cin >> search; 
    cout << endl; 

    if (search == 'y' || search == 'Y')
    {
        // Search for a person
        string targetName;
        cout << "\nEnter the name of the person to search for: ";
        cin >> targetName;

        Person* foundPerson = family.search(family.root, targetName);
        if (foundPerson)
            cout << foundPerson->name << " is a part of this family tree." << endl;
        else
            cout << "\nThis person is not part of the familyTree.\n";
    }
    
    // Display the entire family tree
    cout << "\nFamily Tree Visualization:\n";
    family.visualizeTree(family.root);

   

    return 0;
}