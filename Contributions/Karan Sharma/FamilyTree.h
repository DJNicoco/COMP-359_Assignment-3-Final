#ifndef FAMILYTREE_H
#define FAMILYTREE_H
#include "Person.h"
#include <iostream>
using namespace std;

/*created a header for the FamilyTree class as well.Same reason as person.h, wanted a refresher on how
* header files worked and how to link them. 
*/
class FamilyTree {
public:
    Person* root;

    // Constructor
    FamilyTree(string rootName);

    // in other words setChild - mutator function 
    void addChild(Person* parent, string childName);

    // print function 
    void printTree(Person* node, string prefix = "");

    // visualization function 
    void visualizeTree(Person* node, int depth = 0);

    //search function 
    Person* search(Person* node, const string& name);

};
#endif
