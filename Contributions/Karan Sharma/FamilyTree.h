#ifndef FAMILYTREE_H
#define FAMILYTREE_H

#include "Person.h"
#include <iostream>
using namespace std;

class FamilyTree {
public:
    Person* root;

    // Constructor
    FamilyTree(string rootName);

    // Add a child to a parent
    void addChild(Person* parent, string childName);

    // Print the family tree (DFS-style)
    void printTree(Person* node, string prefix = "");
};

#endif
