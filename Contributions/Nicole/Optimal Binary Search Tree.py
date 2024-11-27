import matplotlib.pyplot as plt
import networkx as nx
import sys

# This is the TreeNode class to represent nodes in a binary tree
class TreeNode:
    """A node in a binary tree."""
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
        # This adds a combination of two colors and generates the resulting color
        result = self.combine_colors(color1, color2)
        if result == 'unknown':
            print(f"Combination of {color1} and {color2} is not recognized.")
        else:
            probability = (
                self.color_probabilities.get(color1, 1.0)
                * self.color_probabilities.get(color2, 1.0)
            )
            # This rounds the probability to 2 decimal places
            probability = round(probability, 2) 
            
            # This add the combination to the list with rounded probabilities
            self.combinations.append((color1, color2, result, probability))
            
            # This builds the tree for the combination
            tree = self.build_small_tree(color1, color2, result, probability)
            
            # This prints and visualizes the tree for the combination
            print(f"\nTree for combination {color1} + {color2} = {result} (Probability: {probability}):")
            self.visualize_tree(tree, f"combination_{color1}_{color2}_{result}")

    def combine_colors(self, color1, color2):
        # This automatically determines the result of combining two colors
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
        
        # Handle reverse combinations (e.g., 'blue' + 'red' -> 'purple')
        if (color2, color1) in color_combinations:
            return color_combinations[(color2, color1)]
        
        # If not found in the dictionary, return 'unknown'
        return color_combinations.get((color1, color2), 'unknown')

    # This method builds a binary tree for two colors and their result
    def build_small_tree(self, color1, color2, result, probability):
        # This creates the root node with the result of the combination and its probability
        root = TreeNode(result, probability)
        # This adds the color1 and color2 as the left and right children respectively
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
        """Creates a custom hierarchical layout for a tree."""
        def traverse(node, x = 0, depth = 0, pos = None, width = 1):
            if not pos:
                pos = {}
            if node:
                pos[str(id(node))] = (x, -depth)  # Position nodes based on depth
                dx = width / 2  # Spread children based on width
                traverse(node.left, x - dx, depth + 1, pos, width / 2)
                traverse(node.right, x + dx, depth + 1, pos, width / 2)
            return pos

        return traverse(root)

    # This method gets the hex color for a given color name
    def get_color_hex(self, color_name):
        # This returns the corresponding hex color value for a given color name
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
        return color_map.get(color_name.lower(), '#FFFFFF')  # Default to white if color not found

    def visualize_tree(self, root, filename):
        """Visualizes the tree in a hierarchical format and saves it as a PNG file."""
        G = nx.DiGraph()

        # This function is to add edges and nodes to the graph
        def add_edges(node):
            if node:
                current_id = str(id(node))
                label = f"{node.value}\nP={node.probability:.2f}"
                color = self.get_color_hex(node.value)  # Get the color for the node
                G.add_node(current_id, label = label, color = color)
                if node.left:
                    G.add_edge(current_id, str(id(node.left)))
                    add_edges(node.left)
                if node.right:
                    G.add_edge(current_id, str(id(node.right)))
                    add_edges(node.right)

        # Start adding edges from the root
        add_edges(root)

        # Get node colors
        node_colors = [G.nodes[node]['color'] for node in G.nodes]

        # Use the hierarchical layout
        pos = self.hierarchical_layout(root)
        labels = nx.get_node_attributes(G, 'label')
        # This draws the tree using NetworkX that I imported and installed
        nx.draw(
            G,
            pos,
            with_labels = True,
            labels = labels,
            node_color = node_colors,
            font_size = 10,
            node_size = 3000,
            font_color = "black",
        )

        # This saves the tree visualization as a PNG file
        plt.title(f"Tree Visualization for {filename}")
        plt.savefig(f"{filename}_tree.png", format = "png")
        plt.close()

        print(f"Tree saved as {filename}_tree.png")
    # This visualizes the full optimal binary search tree in a hierarchical format
    def visualize_full_bst(self, root):
        self.visualize_tree(root, "full_optimal_bst")

    # This method computes the optimal BST cost using dynamic programming
    def optimal_bst_probabilities(self, probs):
        n = len(probs)
        # dp[i][j] will store the minimum cost of BST from i to j
        dp = [[0] * n for _ in range(n)]
        # sum_probs[i][j] will store the sum of probabilities from i to j
        sum_probs = [[0] * n for _ in range(n)]

        # Calculate the sum of probabilities for ranges [i, j]
        for i in range(n):
            sum_probs[i][i] = probs[i]
            for j in range(i + 1, n):
                sum_probs[i][j] = sum_probs[i][j - 1] + probs[j]

        # This fills the dp table for increasing lengths of subarrays
        for length in range(1, n + 1):  # Length of the subarray
            for i in range(n - length + 1):
                j = i + length - 1  # end of the subarray
                # This initializes dp[i][j] with a large number
                dp[i][j] = sys.maxsize
                # Try each node as the root
                for r in range(i, j + 1):
                    cost_left = dp[i][r - 1] if r > i else 0
                    cost_right = dp[r + 1][j] if r < j else 0
                    total_cost = cost_left + cost_right + sum_probs[i][j]
                    dp[i][j] = min(dp[i][j], total_cost)

        return round(dp[0][n - 1], 2) # This returns the rounded minimal cost for the entire range


def main():
    # Step 1: Create an instance for the ColorCombinationTreeWithProbabilities method
    tree_manager = ColorCombinationTreeWithProbabilities()

    # Step 2: Allow the user to input colors and their corresponding probabilities
    print("Enter colors and their probabilities (e.g., 'red, 0.4'). Type 'done' to stop.")
    
    while True:
        # This prompts the user to enter the color and its probability
        user_input = input("\nEnter a color and its probability: ").strip()
        # If the user enters done, the user can stop entering colors
        if user_input.lower() == 'done':
            break

        try:
            # This splits the input by comma to seperate the color from its probability
            color, probability = user_input.split(',')
            # This adds the color and probability to the tree manager
            tree_manager.add_color(color.strip(), float(probability.strip()))
        except ValueError:
            print("Invalid input. Please enter in the format 'color, probability'.")

    # Step 3: Allow the user to input color combinations to generate new colors
    print("\nEnter color combinations (e.g., 'red, blue'). Type 'no' to stop.")
    
    while True:
        # This prompts the user for color combinations
        user_input = input("\nEnter two colors to combine: ").strip()
        # If the user enters no, the user can stop entering combinations
        if user_input.lower() == 'no':
            break
        colors = [color.strip() for color in user_input.split(',')]
        if len(colors) != 2:
            print("Invalid input. Please enter exactly two colors separated by a comma.")
            continue
        # This adds the color combination to the tree manager
        tree_manager.add_combination(colors[0], colors[1])

    # Step 4: Ask user if they want to visualize the full optimal BST
    visualize_bst = input("\nDo you want to visualize the full optimal binary search tree? (yes/no): ").strip().lower()
    
    if visualize_bst == 'yes':
        # If the user wants to visualize the tree, build and display it
        optimal_bst = tree_manager.build_optimal_bst()
        print("\nVisualizing the full optimal BST...")
        tree_manager.visualize_full_bst(optimal_bst)
    else:
        # If not, this will be printed
        print("\nExiting without visualizing the full optimal BST.")

    # Step 5: Get the list of color probabilities from the tree manager
    probabilities = list(tree_manager.color_probabilities.values())
    
    # Step 6: Calculate the optimal BST cost using dynamic programming
    optimal_bst_cost = tree_manager.optimal_bst_probabilities(probabilities)
    
    # Step 7: Output the optimal BST cost to the user
    print(f"\nOptimal BST cost: {optimal_bst_cost}")

# This makes sure the main function runs when the script is entered
if __name__ == "__main__":
    main()
