#include <iostream>
#include <string>
using namespace std;

struct Person {
    string name;
    Person* leftChild;  // Represents the first child
    Person* rightSibling;  // Represents the next sibling

    Person(string name) : name(name), leftChild(nullptr), rightSibling(nullptr) {}
};

class FamilyTree {
public:
    Person* root;

    FamilyTree(string rootName) {
        root = new Person(rootName);
    }

    // Add a child to a parent
    void addChild(Person* parent, string childName) {
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
    void printTree(Person* node, string prefix = "") {
        if (node == nullptr)
            return;

        cout << prefix << node->name << endl;

        // Print all children
        printTree(node->leftChild, prefix + "  ");

        // Print siblings
        printTree(node->rightSibling, prefix);
    }
};

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
