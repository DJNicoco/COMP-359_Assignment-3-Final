# Comp 359 Assignment 3

Link to Github Repo: https://github.com/DJNicoco/COMP-359_Assignment-3-Final.git

Our topic: Optimal shaped BSTs

**Objectve:** This assignment involves implementing the dynamic programming approach to construct an optimal BST for a set of different inputs with probabilities. <br>

## Contributions:

**Nicole:** Wrote the python code <br>
**Navraj:** Wrote the Java code <br>
**Karan Sharma:** Wrote the C++ code <br>
**All Members:** Contributed to this README.

## Introduction into Optimal Binary Search Trees

Optimal Binary Search Trees (OBSTs) are a form of binary search trees designed to minimize the expected search cost for a set of keys with given probabilities. 

**Optimal BST function pseudocode from Levitin (2012)** <br>
Below is the pseudocode for the OBST algorithm, which uses a dynamic programming approach:

![image](https://github.com/user-attachments/assets/1b314b6f-9dd1-4da2-8924-3e2abd9d28dd)

This algorithm outlines a dynamic programming approach to construct an optimal binary search tree. The input takes an array of probabilities for successful searches on n keys, ensuring the keys are sorted. For each subtree of increasing size, the algorithm computes the cost of the optimal tree and returns the minimum average cost of the OBST and the table of roots for the optimal subtrees.

## Analysis Framework

In this assignment, we each focused on implementing different kinds of optimal binary search trees in different programming languages: Python, Java, and C++. <br>

Below is a breakdown of our roles and the key concepts in our implementations: 

### Nicole's Implementation (Python) <br>
For my part, I implemented a Python program that constructs an optimal BST for a set of colors, each with a corresponding probability. <br>
The program allows users to:
1. Input colors and their corresponding probabilities 
2. Combine two colors to generate new colors along with their probabilities.
3. Build a binary tree to represent the color combinations.
4. Calculate the minimal search cost using dynamic programming.
5. Visualize the resulting tree structure using matplotlib and networkx.

To implement this, I developed two classes: **TreeNode** and **ColorCombinationTreeWithProbabilities** and each class has different methods. <br>
The **TreeNode** class manages the nodes of the binary tree, with methods for adding left and right child nodes. These are essential for building the BST structure. <br>
The **ColorCombinationTreeWithProbabilities** class handles the overall process of managing color combinations with their probabilities. It also has the logic for building the binary search tree and calculating its cost.

**ColorCombinationTreeWithProbabilities** <br>

Key methods in this class include:
- the add_combination method combines two colors, calculates their resulting color and probability, and constructs the tree node.
- the build_optimal_bst method compiles the full binary search tree from all combinations
- the optimal_bst_probabilities_with_root_table method uses dynamic programming to calculate the optimal BST cost, minimizing the search cost based on probabilities.
- the visualize_tree method provides a visual representation of the tree using matplotlib and networkx, offering a clear view of the tree structure. <br>

Together, these methods ensure the program builds and visualizes the optimal binary search tree while calculating its minimal search cost.

**The Main Function Flow** <br>

**User Interaction:** The program starts by asking the user to input colors and their corresponding probabilities, which are stored in a dictionary. Users can then input pairs of colors to generate new combinations and their probabilities. <br>
**Combination of Colors:** The user inputs pairs of colors to generate new combinations. Each combination's probability is calculated, and a tree node is created for the combination, forming the binary search tree. <br>
**Tree Visualization:** After all combinations are added, the user can choose to visualize the full optimal BST. If selected, the tree is built and displayed using a hierarchical layout with matplotlib and networkx. The nodes are color-coded based on the combinations, showing the tree structure clearly. <br>
**Dynamic Programming for Optimal BST Cost:** After building the tree, dynamic programming is used to compute the optimal BST’s cost, minimizing the search cost based on the probabilities of each node. This is done using a matrix-based approach where each entry represents the minimum search cost for a subtree, and the algorithm fills out this matrix to compute the optimal BST. <br>

### Navraj's Implementation (Java) <br>

My implementation demonstrates how to create a Decision-Making Game in Java using an Optimal Binary Search Tree (OBST). The OBST is built dynamically with probabilities to optimize decision-making paths. The program uses a custom Node class to represent decision points (questions) and their relationships within the tree structure. ASCII-based visualization were used to make the tree structure clear and intuitive, showing how decisions and outcomes are connected hierarchically. This approach not only makes the OBST concept easier to understand but also provides an interactive way to explore decision-making paths.
#### Key methods used: <br>

##### OBST:
This method constructs the Optimal Binary Search Tree using dynamic programming. It calculates the minimum cost for each subtree and determines the optimal root for every range of keys.

##### buildTree:
Recursively constructs the OBST from the optimal roots computed in OBST. It returns the root node of the tree, which serves as the starting point for decisions.

##### SumOfProbabilities:
Calculates the sum of probabilities (p for keys and q for failure cases) for a given range. This sum is used to compute the expected cost during tree construction.

##### decision:
Implements the interactive logic. Starting at the root of the tree, users answer questions and traverse the tree based on their choices (left or right). The game ends when no further nodes are available.

##### printTree:
Visualizes the OBST as an ASCII diagram. Each level of the tree is displayed hierarchically, making it easy to understand parent-child relationships.



### Karan's Implementation (C++) <br>

My part's implemenation demonstrates how to visualize a BST in the form of a family tree in C++ using a hierarchical structure. The family tree is implemented with a custom **FamilyTree** class and a **Person** struct - which further provides methods for adding family members and visualizing their respective relationhips. I decided to use the ASCII visualization approach to show how this type of BST would work. I also found that this simplifies the process a bit so it is easier to understand family relationships. 

#### Key Components of CPP Program: <br>

#### 1. Person Struct
The **Person** struct represents an individual in the family tree. 
Each person contains: 
- **Name**: The name of the individual
- **leftChild**: A pointer to the first child of the person.
- **rightSibling**: A pointer to the person's next sibling.

#### 2. FamilyTree Class
The **FamilyTree** class gives functionality to: 
- Initialize a family tree with a root person. My tree goes as far as grandparent - so the root is the grandparent.
- Add children to a specific parent.
- Allows to create a visualization of the Family Tree using ASCII art for a more understandable representation of the familial heirarchy.
- Using BST in-order search to find a person within the family tree. 

## Results

### Nicole's Results (Python) <br>
#### Output:
Here is the optimal BST’s structure generated from the input data: <br>
![image](https://github.com/user-attachments/assets/24e81e2a-ca9d-4e46-a206-d3fead8fb0b7)

#### Input Colors and Probabilities: <br>
These are the input values used in the algorithm to calculate the optimal BST: <br>
<p align="center">
  <img src="https://github.com/user-attachments/assets/583ab9ba-af84-4897-a56a-1773398b2d85" width="45%" />
  <img src="https://github.com/user-attachments/assets/c7ab033e-e12c-4bc0-948e-89ad9ea56cd2" width="45%" />
</p>

#### Full Binary Tree with Probabilities:
This is the visualized optimal BST, showing how the colors combine with their probabilities: <br>
![image](https://github.com/user-attachments/assets/6ac2ebf6-67d2-4bb4-8164-4b7033550d4f)

### Navraj's Results (Python) <br>
#### Output: 
Here is the output generated from the user inputs along with ascii visualization: <br>
![obst](https://github.com/user-attachments/assets/175e4017-170b-426d-a76e-0b623c1b7d62)


### Karan's Results (C++) <br>
#### Output: 
Here is a visualization of how the tree looks with some ASCII art: <br>
![image](https://github.com/user-attachments/assets/88fe1517-3ffb-4271-a3da-2f10fdfbb3de)

Below is an output where the user creates a family tree and then uses that to search for a specific family member. 
In the below output, family member exists in the tree: <br>
![image](https://github.com/user-attachments/assets/ee8539fa-468b-4b7f-8d91-2b68a428971e)

Below is another output where the target person is **not** part of the family tree: <br>
![image](https://github.com/user-attachments/assets/a42b4992-c3ec-4a9a-b8e2-1e22e7ecb5c4)


## References

1. Campbell, R. (2024). "Ch 8: Dynamic Programming." Week 10 Slides.
2. Cave of Programming. (2021, March 27). Linking and Header Files | C++ For Java Devs Ep. 3 [Video]. YouTube. https://www.youtube.com/watch?v=w4gNct0QQIY
3. Enzo Ti. (2012, January 8). How to print ascii art in c++? Cplusplus.com. https://cplusplus.com/forum/general/58945/
4. GeeksforGeeks. (2023, May 15). Binary Search Tree in C++. GeeksforGeeks. https://www.geeksforgeeks.org/cpp-binary-search-tree/
5. GeeksforGeeks. (2024, April 8). Binary Search Tree In Python. GeeksforGeeks. https://www.geeksforgeeks.org/binary-search-tree-in-python/
6. GeeksforGeeks. (2023, July 10). Optimal Binary Search Tree: DP-24. GeeksforGeeks. www.geeksforgeeks.org/optimal-binary-search-tree-dp-24/
7. W3Schools. (n.d.). C++ OOP (Object-Oriented Programming). W3Schools. https://www.w3schools.com/cpp/cpp_oop.asp
