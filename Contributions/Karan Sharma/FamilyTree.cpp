#include "FamilyTree.h"

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
