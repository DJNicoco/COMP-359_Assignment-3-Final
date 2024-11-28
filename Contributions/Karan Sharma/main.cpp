#include "FamilyTree.h"
#include <iostream>
using namespace std;

// Recursive function to add children interactively
void addChildrenInteractively(FamilyTree& tree, Person* parent) {
    int numChildren;

    // Explicitly state whose children are being entered
    cout << "\nHow many children does " << parent->name << " have? ";
    cin >> numChildren;

    for (int i = 0; i < numChildren; ++i) {
        string childName;

        // Prompt for each child’s name
        cout << "Enter the name of child " << i + 1 << " of " << parent->name << ": ";
        cin >> childName;

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

        if (addGrandchildren == 'y' || addGrandchildren == 'Y') {
            addChildrenInteractively(tree, newChild); // Recursive call for grandchildren
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
    addChildrenInteractively(family, family.root);

    // Display the entire family tree
    cout << "\nFamily Tree Visualization:\n";
    family.visualizeTree(family.root);

    return 0;
}
