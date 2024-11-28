#ifndef PERSON_H
#define PERSON_H

#include <string>
using namespace std;

struct Person {
    string name;
    Person* leftChild;     // Represents the first child
    Person* rightSibling;  // Represents the next sibling

    Person(string name) : name(name), leftChild(nullptr), rightSibling(nullptr) {}
};

#endif
