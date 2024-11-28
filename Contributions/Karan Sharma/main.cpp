#include "FamilyTree.h"

int main() {
    // Create a family tree with a root person
    FamilyTree family("Billy The 3rd (Grandpa)");

    // Add children to the root
    family.addChild(family.root, "Pablo (child 1)");
    family.addChild(family.root, "Sofia (child 2)");

    // Add grandchildren to Parent1
    family.addChild(family.root->leftChild, "Cono");
    family.addChild(family.root->leftChild, "Jono");
    family.addChild(family.root->leftChild, "Meowdy");

    // Add grandchildren to Parent2
    family.addChild(family.root->leftChild->rightSibling, "Pomo");
    family.addChild(family.root->leftChild->rightSibling, "Poco");
    family.addChild(family.root->leftChild->rightSibling, "Polo");


    // Display the family tree
    cout << "Family Tree:\n";
    family.printTree(family.root);

    cout << "Family Tree Visualization:\n";
    family.visualizeTree(family.root);

    return 0;
}
