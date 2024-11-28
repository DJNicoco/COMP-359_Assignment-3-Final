# Comp 359 Assignment 3

Link to Github Repo: https://github.com/DJNicoco/COMP-359_Assignment-3-Final.git

Our topic: Optimal shaped BSTs

## Contributions:

We all contributed to this README. <br>
**Nicole** - Wrote the python code <br>
**Navraj** - Wrote the Java code <br>
**Karan Sharma** - Wrote the C++ code <br>

## Introduction into Optimal Binary Search Trees

Optimal Binary Search Trees (BSTs) are a type of binary tree that minimize the expected cost of searching. This assignment involves implementing the dynamic programming approach to construct an optimal BST for a set of different inputs with given search probabilities. 

Optimal BST function pseudocode from Levitin (2012): <br>

![image](https://github.com/user-attachments/assets/1b314b6f-9dd1-4da2-8924-3e2abd9d28dd)

## Analysis Framework

In this assignment, we each focused on implementing different kinds of optimal binary search trees in different programming languages: Python, Java, and C++. <br>

Below is a breakdown of each member's role and the key concepts of their implementation: 
#### Nicole's Implementation (Python) <br>
For my part, I implemented a Python program that constructs an optimal BST for a set of colors, each with a corresponding probability. <br>
The program allows users to:
1. Input colors and their corresponding probabilities 
2. Combine two colors to generate new colors along with their probabilities.
3. Build a binary tree to represent the color combinations.
4. Calculate the cost of an Optimal Binary Search Tree using dynamic programming.
5. Visualize the resulting tree structure using matplotlib and networkx.

To implement this, I developed two classes: **TreeNode** and **ColorCombinationTreeWithProbabilities** and each class has different methods. <br>
The **TreeNode** class includes two methods for managing child nodes: one for assigning a left child and another for assigning a right child. <br>
These methods are important for structuring the binary tree and this will later be used to compute the optimal BST. <br>
In the **ColorCombinationTreeWithProbabilities** class, it handles the overall process of managing color combinations with their probabilities. It also has the logic for building the binary search tree and calculating its cost.

**The Main Function Flow** <br>

**User Interaction:** The program starts by asking the user to input colors and their corresponding probabilities, which are stored in a dictionary. The user can then input pairs of colors to generate new combinations and calculate their probabilities. <br>
**Combination of Colors:** Next, the user inputs pairs of colors to generate new combinations Each combination's probability is calculated, and a tree node is created for each color combination. These nodes are linked to form the binary search tree.<br>
**Tree Visualization:** After all combinations are added, the user can choose to visualize the full optimal BST. If selected, the tree is built and displayed using a hierarchical layout with matplotlib and networkx. The nodes are color-coded based on the combinations, showing the tree structure clearly. <br>
**Dynamic Programming for Optimal BST Cost:** After building the tree, dynamic programming is used to compute the optimal BST’s cost, minimizing the search cost based on the probabilities of each node. this is done using a matrix-based approach where each entry in the matrix represents the minimum search cost for a subtree of the BST. The algorithm computes the optimal BST by filling out this matrix based on the probabilities of each color combination. <br>

#### Navraj's Implementation (Java) <br>

#### Karan's Implementation (C++) <br>
My part's implemenation demonstrates how to visualize a BST in the form of a family tree in C++ using a hierarchical structure. The family tree is implemented with a customer **FamilyTree** class and a **Person** struct - which further provides methods for adding family members and visualizing their respective relationhips. I decided to use the ASCII visualization approach to show how this type of BST would work. I also found that this simplifies the process a bit so it is easier to understand family relationships. 

### sdfkjh.ads <br>

## Results

#### Nicole's Results (Python) <br>
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

#### Navraj's Results (Python) <br>

#### Karan's Results (C++) <br>

## References

Campbell, R. (2024). "Ch 8: Dynamic Programming." Week 10 Slides. <br>
“Optimal Binary Search Tree: DP-24.” GeeksforGeeks, 10 July 2023, www.geeksforgeeks.org/optimal-binary-search-tree-dp-24/ <br>






