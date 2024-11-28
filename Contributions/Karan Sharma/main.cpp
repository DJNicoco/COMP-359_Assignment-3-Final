#include "FamilyTree.h"

int main() {
    // Create a family tree with a root person
    FamilyTree family("Grandparent");

    // Add children to the root
    family.addChild(family.root, "Parent1");
    family.addChild(family.root, "Parent2");

    // Add grandchildren to Parent1
    family.addChild(family.root->leftChild, "Child1");
    family.addChild(family.root->leftChild, "Child2");

    // Add grandchildren to Parent2
    family.addChild(family.root->leftChild->rightSibling, "Child3");
    family.addChild(family.root->leftChild->rightSibling, "Child4");

    // Display the family tree
    cout << "Family Tree:\n";
    family.printTree(family.root);

    return 0;
}
