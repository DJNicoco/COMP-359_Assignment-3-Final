#ifndef PERSON_H
#define PERSON_H
#include <string>
using namespace std;
/*I could have defined this struct in the main.cpp function but wanted a refresher on how header files worked. 
* I had some troubles figuring how linking a header file works so I needed help. 
* https://www.youtube.com/watch?v=w4gNct0QQIY
*/
struct Person {
    string name;
    Person* leftChild;     // first child
    Person* rightSibling;  // next sibling
    Person(string name) : name(name), leftChild(nullptr), rightSibling(nullptr) {}
};
#endif
