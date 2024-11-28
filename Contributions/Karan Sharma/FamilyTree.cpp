#include "FamilyTree.h"
#include <iomanip>

// Constructor
FamilyTree::FamilyTree(string rootName) {
    root = new Person(rootName);
}

// Add a child to a parent
void FamilyTree::addChild(Person* parent, string childName) {
    if (parent->leftChild == nullptr) {
        parent->leftChild = new Person(childName);
    }
    else {
        Person* sibling = parent->leftChild;
        while (sibling->rightSibling != nullptr) {
            sibling = sibling->rightSibling;
        }
        sibling->rightSibling = new Person(childName);
    }
}

// Print the family tree (DFS-style)
void FamilyTree::printTree(Person* node, string prefix) {
    if (node == nullptr)
        return;

    cout << prefix << node->name << endl;

    // Print all children
    printTree(node->leftChild, prefix + "  ");

    // Print siblings
    printTree(node->rightSibling, prefix);
}
// Visualize the tree using an ASCII representation
void FamilyTree::visualizeTree(Person* node, int depth) {
    if (node == nullptr)
        return;

    // Indent based on depth
    cout << string(depth * 4, ' ') << "|-- " << node->name << endl;

    // Visualize the children and siblings
    if (node->leftChild) {
        visualizeTree(node->leftChild, depth + 1);  // Recurse for children
    }
    if (node->rightSibling) {
        visualizeTree(node->rightSibling, depth);  // Recurse for siblings
    }
}
