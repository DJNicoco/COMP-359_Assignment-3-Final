#include <iostream>
#include <vector>
#include <limits>
#include <iomanip>
using namespace std;

// Structure to represent a node in the tree
struct TreeNode {
    int key;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int k) : key(k), left(nullptr), right(nullptr) {}
};

//**BACKTRACKING ALGO TO construct the OBST using the Root Matrix**
TreeNode* buildTree(const vector<vector<int>>& R, int i, int j) {
    
    // base case - subtree is empty
    if (i > j) return nullptr; 

    //get root index for the current range [i, j] from root matrix 
    int rootIndex = R[i][j];
    if (rootIndex == -1) return nullptr;

    //new treenode for current root
    TreeNode* root = new TreeNode(rootIndex);

    // recursively build left subtree
    root->left = buildTree(R, i, rootIndex - 1);

    // recursively build right subtree
    root->right = buildTree(R, rootIndex + 1, j);

    return root;
}

// visualize the tree
void visualizeTree(TreeNode* root, int depth = 0) {
    if (!root) return;

    // print right subtree
    visualizeTree(root->right, depth + 1);

    // print current node
    cout << string(depth * 4, ' ') << root->key << "\n";

    // print left subtree
    visualizeTree(root->left, depth + 1);
}

// Function to calculate the Optimal Binary Search Tree using Dynamic Programming
/* Below is the implementation of the pseudocode seen in chp 8.3 in the textbook about creating an OBST: 
* for i ? 1 to n do
    C[i, i ? 1]? 0
    C[i, i]? P[i]
    R[i, i]? i
   C[n + 1, n]? 0
   for d ? 1 to n ? 1 do //diagonal count
        for i ? 1 to n ? d do
            j ? i + d
            minval ? ?
            for k ? i to j do
                if C[i, k ? 1] + C[k + 1, j ] < minval
                    minval ? C[i, k ? 1] + C[k + 1, j ]; kmin ? k
            R[i, j ] ? kmin
            sum ? P[i]; for s ? i + 1 to j do sum ? sum + P[s]
            C[i, j ]? minval + sum
    return C[1, n], R
* 
*///
void calculateOBST(const vector<double>& P, int n, vector<vector<double>>& C, vector<vector<int>>& R) {
    for (int i = 1; i <= n; i++) {
        C[i][i - 1] = 0;        // Cost of an empty subtree
        C[i][i] = P[i - 1];     // Cost of a single key
        R[i][i] = i;            // Single key is its own root
    }
    C[n + 1][n] = 0;            // Cost of an empty subtree after the last key

    //loop over the size of subtrees 
    for (int d = 1; d < n; d++) {
        //loop over the starting index of the subtree
        for (int i = 1; i <= n - d; i++) {
            int j = i + d; //calculate the ending inedx of subtree
            //minimum cost for current subtree range 
            double minCost = numeric_limits<double>::infinity(); 
            int bestRoot = -1;

            // loop over all possible roots
            for (int k = i; k <= j; k++) {
                //cost of left + right subtree
                double cost = C[i][k - 1] + C[k + 1][j];
                //uppdate minimum cost and optimal root for current range 
                if (cost < minCost) {
                    minCost = cost;
                    bestRoot = k;
                }
            }

            double sum = 0;
            for (int s = i - 1; s < j; s++) {
                sum += P[s];
            }
            // sum of probabilities for the current range to min cost 
            C[i][j] = minCost + sum;
            R[i][j] = bestRoot;
        }
    }
}

// Function to print a matrix
void printMatrix(const vector<vector<double>>& matrix, const string& name) {
    cout << name << ":\n";
    for (size_t i = 1; i < matrix.size(); i++) {
        for (size_t j = 1; j < matrix[i].size(); j++) {
            if (matrix[i][j] == numeric_limits<double>::infinity()) {
                cout << setw(8) << "INF";
            }
            else {
                cout << setw(8) << matrix[i][j];
            }
        }
        cout << "\n";
    }
}

void printMatrix(const vector<vector<int>>& matrix, const string& name) {
    cout << name << ":\n";
    for (size_t i = 1; i < matrix.size(); i++) {
        for (size_t j = 1; j < matrix[i].size(); j++) {
            cout << setw(8) << matrix[i][j];
        }
        cout << "\n";
    }
}

int main() {
    int n;
    cout << "Enter the number of keys: ";
    cin >> n;

    vector<double> probabilities(n);
    cout << "Enter the probabilities of the keys: ";
    for (int i = 0; i < n; i++) {
        cin >> probabilities[i];
    }

    // Create cost and root matrices
    vector<vector<double>> C(n + 2, vector<double>(n + 1, numeric_limits<double>::infinity()));
    vector<vector<int>> R(n + 1, vector<int>(n + 1, -1));

    // Calculate the OBST
    calculateOBST(probabilities, n, C, R);

    // Print the results
    printMatrix(C, "Cost Matrix (C)");
    printMatrix(R, "Root Matrix (R)");

    cout << "Optimal Cost: " << C[1][n] << "\n";

    // Build and visualize the tree
    TreeNode* root = buildTree(R, 1, n);
    cout << "\nVisualized Tree:\n";
    visualizeTree(root);

    return 0;
}
