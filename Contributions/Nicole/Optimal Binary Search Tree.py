import matplotlib.pyplot as plt

# Function Definitions
def optimal_bst(keys, p, q, n):
    # Construct an Optimal BST and compute the minimum search cost.
    cost = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    root = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # Initialize the diagonal of cost matrix
    for i in range(n + 1):
        cost[i][i] = q[i]

    # Iterate over chain lengths
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length
            cost[i][j] = float('inf')
            total_prob = sum(p[i:j]) + sum(q[i:j + 1])
            for r in range(i, j):  # Try every root
                c = cost[i][r] + cost[r + 1][j] + total_prob
                if c < cost[i][j]:
                    cost[i][j] = round(c, 2)  # Round to 2 decimal places
                    root[i][j] = r

    return cost, root

def construct_obst(root, keys, i, j):
    # Construct the tree structure from the root matrix.
    if i >= j:
        return None
    r = root[i][j]
    return {
        "key": keys[r],
        "left": construct_obst(root, keys, i, r),
        "right": construct_obst(root, keys, r + 1, j)
    }

def plot_tree(tree, x=0, y=0, level_gap=1, x_gap=2, ax=None):
    # Visualize the binary tree using matplotlib.
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))

    if tree:
        ax.text(x, y, str(tree["key"]), fontsize=12, ha='center',
                bbox=dict(facecolor='skyblue', edgecolor='black', boxstyle='round,pad=0.5'))

        # Plot left child
        if tree["left"]:
            child_x, child_y = x - x_gap, y - level_gap
            ax.plot([x, child_x], [y, child_y], color='black')  # Draw edge
            plot_tree(tree["left"], child_x, child_y, level_gap, x_gap / 2, ax)

        # Plot right child
        if tree["right"]:
            child_x, child_y = x + x_gap, y - level_gap
            ax.plot([x, child_x], [y, child_y], color='black')  # Draw edge
            plot_tree(tree["right"], child_x, child_y, level_gap, x_gap / 2, ax)

    ax.axis('off')
    if ax is None:
        plt.show()

def tree_to_dot(tree):
    # Converts the tree structure to DOT format.
    dot_string = "digraph OptimalBST {\n"
    
    def add_edges(node):
        nonlocal dot_string
        if node:
            if node['left']:
                dot_string += f'    {node["key"]} -> {node["left"]["key"]};\n'
                add_edges(node['left'])
            if node['right']:
                dot_string += f'    {node["key"]} -> {node["right"]["key"]};\n'
                add_edges(node['right'])

    add_edges(tree)
    dot_string += "}\n"
    return dot_string

def save_dot_file(dot_string, filename="optimal_bst.dot"):
    # Saves the DOT format string to a file.
    with open(filename, 'w') as f:
        f.write(dot_string)


# Hardcoded values
keys = [10, 20, 30, 40, 50]  # Node values (keys)
p = [0.1, 0.3, 0.2, 0.2, 0.2]  # Probabilities for successful search (p)
q = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]  # Probabilities for unsuccessful search (q)
n = len(keys)

# Compute the cost and root matrices (Optimal BST computation)
cost, root = optimal_bst(keys, p, q, n)

# Reconstruct the tree based on the root matrix
tree = construct_obst(root, keys, 0, n)

# Print results for debugging
print("\nRounded Cost Matrix:")
for row in cost:
    print(row)
    
print("\nRoot Matrix:")
for row in root:
    print(row)

# Visualize the Optimal BST
plot_tree(tree)

# Display the minimum search cost rounded to 2 decimal places
min_search_cost = cost[0][n]
rounded_cost = round(min_search_cost, 2)  # Round to 2 decimal places
print(f"\nMinimum Search Cost: {rounded_cost}")

# Convert the tree to DOT format and save to a file
dot_string = tree_to_dot(tree)
save_dot_file(dot_string, "optimal_bst.dot")
print("\nDOT file 'optimal_bst.dot' has been saved.")

