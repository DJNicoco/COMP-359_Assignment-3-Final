import matplotlib.pyplot as plt
import networkx as nx
import sys

# This is the TreeNode class to represent nodes in a binary tree
class TreeNode:
    # A node in a binary tree
    def __init__(self, value, probability = 1.0):
        self.value = value
        self.probability = probability # This stores the probability associated with the node
        self.left = None # Left child node
        self.right = None # Right child node

    # This is the method to add the left child to the current node
    def add_left(self, node):
        self.left = node
    
    # This is the method to add the right child to the current node
    def add_right(self, node):
        self.right = node

# This handles the creation of trees and an optimal BST with probabilities
class ColorCombinationTreeWithProbabilities:
    def __init__(self):
        self.color_probabilities = {}  # This stores probabilities of individual colors
        self.combinations = []  # This stores individual color combinations

    def add_color(self, color, probability):
        self.color_probabilities[color] = probability # This adds a color with its probability

    def add_combination(self, color1, color2):
        result = self.combine_colors(color1, color2)
        if result == 'unknown':
            print(f"Combination of {color1} and {color2} is not recognized.")
        else:
            probability = (
                self.color_probabilities.get(color1, 1.0)
                * self.color_probabilities.get(color2, 1.0)
            )
            probability = round(probability, 2)  # Rounding probability
            self.combinations.append((color1, color2, result, probability))
            tree = self.build_small_tree(color1, color2, result, probability)
            print(f"\nTree for combination {color1} + {color2} = {result} (Probability: {probability}):")
            self.visualize_tree(tree, f"combination_{color1}_{color2}_{result}")

    def combine_colors(self, color1, color2):
        color_combinations = {
            ('red', 'blue'): 'purple',
            ('blue', 'yellow'): 'green',
            ('red', 'yellow'): 'orange',
            ('blue', 'green'): 'cyan',
            ('red', 'green'): 'brown',
            ('yellow', 'green'): 'lime',
            ('black', 'white'): 'gray',
            ('red', 'white'): 'pink',
            ('blue', 'black'): 'navy',
        }
        if (color2, color1) in color_combinations:
            return color_combinations[(color2, color1)]
        return color_combinations.get((color1, color2), 'unknown')

    # This method builds a binary tree for two colors and their result
    def build_small_tree(self, color1, color2, result, probability):
        root = TreeNode(result, probability)
        root.add_left(TreeNode(color1, self.color_probabilities.get(color1, 1.0)))
        root.add_right(TreeNode(color2, self.color_probabilities.get(color2, 1.0)))
        return root

    # This method builds an optimal binary search tree using the combinations and probabilities
    def build_optimal_bst(self):
        # This creates a dictionary to store the TreeNode for each color and result
        node_map = {}

        # Helper function to retrieve or create nodes
        def get_node(value, probability = 1.0):
            if value not in node_map:
                node_map[value] = TreeNode(value, probability)
            return node_map[value]

        # This iterates through all combinations and builds the tree
        for color1, color2, result, probability in self.combinations:
            # Get or create nodes for the result and the two input colors
            result_node = get_node(result, probability)
            color1_node = get_node(color1, self.color_probabilities.get(color1, 1.0))
            color2_node = get_node(color2, self.color_probabilities.get(color2, 1.0))

            # If the result node doesn't already have children, assign them
            if result_node.left is None:
                result_node.add_left(color1_node)
            if result_node.right is None:
                result_node.add_right(color2_node)

        # Find the root node (the last combination's result will be the tree root)
        if self.combinations:
            final_result = self.combinations[-1][2]
            return node_map[final_result]

        return None

    def hierarchical_layout(self, root):
        # Creates a custom hierarchical layout for a tree with adjustable spacing
        def traverse(node, x=0, depth=0, pos=None, width=1):
            if not pos:
                pos = {}
            if node:
                # Adjust vertical spacing by scaling with depth
                pos[str(id(node))] = (x, -depth * 1.5)  # Adjusted vertical spacing
            
                # Spread out child nodes more evenly
                dx = width / 2  # Adjust the width factor here to control node spread

                # Traverse the left and right child nodes, positioning them horizontally
                if node.left:
                    traverse(node.left, x - dx, depth + 1, pos, width / 2)
                if node.right:
                    traverse(node.right, x + dx, depth + 1, pos, width / 2)
            return pos

        return traverse(root)

    # This method gets the hex color for a given color name
    def get_color_hex(self, color_name):
        color_map = {
            'red': '#FF0000',
            'blue': '#0000FF',
            'yellow': '#FFFF00',
            'green': '#008000',
            'orange': '#FFA500',
            'purple': '#800080',
            'cyan': '#00FFFF',
            'brown': '#A52A2A',
            'lime': '#00FF00',
            'gray': '#808080',
            'pink': '#FFC0CB',
            'navy': '#000080',
            'black': '#000000',
            'white': '#FFFFFF'
        }
        return color_map.get(color_name.lower(), '#FFFFFF')

    def add_edges_to_graph(self, node, G):
        # Add the edges of a tree to the graph
        if node:
            current_id = str(id(node))
            label = f"{node.value}\nP={node.probability:.2f}"
            color = self.get_color_hex(node.value)
            G.add_node(current_id, label=label, color=color)
            if node.left:
                G.add_edge(current_id, str(id(node.left)))
                self.add_edges_to_graph(node.left, G)
            if node.right:
                G.add_edge(current_id, str(id(node.right)))
                self.add_edges_to_graph(node.right, G)

    def visualize_tree(self, root, filename):
        # Visualizes the tree and saves it as a PNG
        G = nx.DiGraph()
        self.add_edges_to_graph(root, G)

        node_colors = [G.nodes[node]['color'] for node in G.nodes]
        pos = self.hierarchical_layout(root)  # Apply layout to the root of the tree
        labels = nx.get_node_attributes(G, 'label')

        plt.figure(figsize=(12, 12))
        nx.draw(
            G,
            pos,
            with_labels=True,
            labels=labels,
            node_color=node_colors,
            font_size= 20,
            node_size= 6000,
            font_color="black",
        )
        plt.title(f"Tree Visualization for {filename}")
        plt.savefig(f"{filename}_tree.png", format="png")
        plt.close()
        print(f"Tree saved as {filename}_tree.png")

    # This visualizes the full optimal binary search tree in a hierarchical format
    def visualize_full_bst(self, root):
        self.visualize_tree(root, "full_optimal_bst")

    # This method computes the optimal BST cost using dynamic programming following the algorithm from textbook
    def optimal_bst_probabilities_with_root_table(self, probs):
        n = len(probs)

        # Initialize cost table C and root table R
        C = [[0] * (n + 1) for _ in range(n + 1)]
        R = [[0] * (n + 1) for _ in range(n + 1)]

        # Fill the diagonal of C with probabilities and set roots for single keys
        for i in range(1, n + 1):
            C[i][i - 1] = 0  # Empty subarray
            C[i][i] = probs[i - 1]  # Diagonal elements (single keys)
            R[i][i] = i  # Root of single key subarray
        

        # Fill C and R for increasing lengths of subarrays
        for d in range(1, n):  # d is the diagonal offset
            for i in range(1, n - d + 1):
                j = i + d  # End of the subarray
            
                # Initialize minimum cost for range [i, j]
                minval = sys.maxsize
                kmin = -1

                # Try all roots k in range [i, j]
                for k in range(i, j + 1):
                    cost_left = C[i][k - 1]
                    cost_right = C[k + 1][j] if k + 1 <= n else 0
                    total_cost = cost_left + cost_right

                    if total_cost < minval:
                        minval = total_cost
                        kmin = k

                # Compute total cost including probabilities
                sum_probs = sum(probs[i - 1:j])
                C[i][j] = minval + sum_probs
                R[i][j] = kmin

        # Return the rounded minimal cost and the root table
        return round(C[1][n], 2), R
    
    # Visualizing method to reconstruct the optimal BST
    def visualize_reconstructed_bst(self, root):
        # Visualizes the reconstructed optimal BST and saves it as a separate PNG
        filename = "reconstructed_optimal_bst"
        self.visualize_tree(root, filename)
        print(f"Reconstructed optimal BST saved as {filename}_tree.png")

    # Backtracking method to find all possible optimal BSTs based on the root table
    def backtrack_optimal_bst(self, root_table, i, j):
        # Backtrack the root table to construct the optimal BST
        if i > j:
            return None
        r = root_table[i][j]
        if r == -1:
            return None
        # Create the current node with the value (we use indices as node values)
        node_value = f"Node {r}"
        node = TreeNode(node_value)
        
        # Recursively build the left and right subtrees
        node.left = self.backtrack_optimal_bst(root_table, i, r - 1)
        node.right = self.backtrack_optimal_bst(root_table, r + 1, j)
        
        return node

def main():
    # Step 1: Create an instance for the ColorCombinationTreeWithProbabilities method
    tree_manager = ColorCombinationTreeWithProbabilities()

    # Step 2: Allow the user to input colors and their corresponding probabilities
    print("Enter colors and their probabilities (e.g., 'red, 0.4'). Type 'done' to stop.")
    
    while True:
        user_input = input("\nEnter a color and its probability: ").strip()
        if user_input.lower() == 'done':
            break

        try:
            color, probability = user_input.split(',')
            tree_manager.add_color(color.strip(), float(probability.strip()))
        except ValueError:
            print("Invalid input. Please enter in the format 'color, probability'.")

    # Step 3: Allow the user to input color combinations to generate new colors
    print("\nEnter color combinations (e.g., 'red, blue'). Type 'no' to stop.")
    
    while True:
        user_input = input("\nEnter two colors to combine: ").strip()
        if user_input.lower() == 'no':
            break
        colors = [color.strip() for color in user_input.split(',')]
        if len(colors) != 2:
            print("Invalid input. Please enter exactly two colors separated by a comma.")
            continue
        tree_manager.add_combination(colors[0], colors[1])

    # Step 4: Ask user if they want to visualize the full optimal BST
    visualize_bst = input("\nDo you want to visualize the full optimal binary search tree? (yes/no): ").strip().lower()

    if visualize_bst == 'yes':
        # Build the optimal BST and save it as a separate PNG
        optimal_bst_root = tree_manager.build_optimal_bst()
        if optimal_bst_root:
            print("\nVisualizing the full optimal BST...")
            tree_manager.visualize_full_bst(optimal_bst_root)  # Now visualizing the actual BST root node
    else:
        print("\nExiting without visualizing the full optimal BST.")

    # Step 5: Get the list of color probabilities from the tree manager
    probabilities = list(tree_manager.color_probabilities.values())

    # Step 6: Calculate the optimal BST cost and root table using dynamic programming
    optimal_bst_cost, root_table = tree_manager.optimal_bst_probabilities_with_root_table(probabilities)

    # Step 7: Output the optimal BST cost
    print(f"\nOptimal BST cost: {optimal_bst_cost}")
   
    # Step 8: Print the root table
    print("\nRoot Table:")
    for row in root_table:
        print(row)

    # Step 9: Call the backtracking method to get the optimal BST structure
    print("\nReconstructing the Optimal BST using backtracking...")
    optimal_bst_root = tree_manager.backtrack_optimal_bst(root_table, 0, len(probabilities) - 1)

    # Step 10: Visualize the reconstructed optimal BST
    print("\nVisualizing the reconstructed optimal BST...")
    tree_manager.visualize_reconstructed_bst(optimal_bst_root)

# This makes sure the main function runs when the script is entered
if __name__ == "__main__":
    main()