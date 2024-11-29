import java.util.Scanner;
public class DecisionOBST {
    // Node class to represent each question/decision
    static class Node {
        String question;
        Node left, right;

        public Node(String question) {
            this.question = question;
            this.left = null;
            this.right = null;
        }
    }

    // Build the OBST using dynamic programming
    public static Node OBST(String[] keys, double[] p, double[] q) {
        int n = keys.length;
        double[][] cost = new double[n + 2][n + 2];
        int[][] root = new int[n + 1][n + 1];

        // Initialize cost
        for (int i = 0; i <= n; i++) {
            cost[i][i] = q[i];
        }

        // Calculate costs for subtrees of increasing size
        for (int size = 1; size <= n; size++) {
            for (int i = 1; i <= n - size + 1; i++) {
                int j = i + size - 1;
                cost[i][j] = Double.MAX_VALUE;

                for (int r = i; r <= j; r++) {
                    double c = cost[i][r - 1] + cost[r + 1][j] + SumOfProbabilities(p, q, i, j);
                    if (c < cost[i][j]) {
                        cost[i][j] = c;
                        root[i][j] = r;
                    }
                }
            }
        }

        return buildTree(keys, root, 1, n);
    }

    // Construct the OBST recursively
    private static Node buildTree(String[] keys, int[][] root, int i, int j) {
        if (i > j) return null;
        int r = root[i][j];
        Node node = new Node(keys[r - 1]);
        node.left = buildTree(keys, root, i, r - 1);
        node.right = buildTree(keys, root, r + 1, j);
        return node;
    }

    // Sum probabilities in the range
   private static double SumOfProbabilities(double[] p, double[] q, int i, int j) {
        double sum = 0;
        // Sum probabilities in the range of p
        for (int k = i - 1; k < j; k++) { // Adjust index range for p
            if (k >= 0 && k < p.length) {
                sum += p[k];
            }
        }
        // Sum probabilities in the range of q
        for (int k = i - 1; k <= j; k++) { // Adjust index range for q
            if (k >= 0 && k < q.length) {
                sum += q[k];
            }
        }
        return sum;
    }

    //The actual decision tree
    public static void decision(Node root, Scanner scanner) {
        Node current = root;
        while (current != null) {
            System.out.println("Question: " + current.question);
            System.out.print("Enter 'left' or 'right': ");
            String choice = scanner.nextLine().trim().toLowerCase();

            if (choice.equals("left")) {
                if (current.left == null) {
                    System.out.println("No further options on the left. Game Over!");
                    break;
                }
                current = current.left;
            } else if (choice.equals("right")) {
                if (current.right == null) {
                    System.out.println("No further options on the right. Game Over!");
                    break;
                }
                current = current.right;
            } else {
                System.out.println("Invalid choice. Try again!");
            }
        }
    }
    //Print as ascii art
    public static void printTree(Node node, String prefix, boolean isLeft) {
        if (node != null) {
            System.out.println(prefix + (isLeft ? "|-- " : "\\-- ") + node.question);
            printTree(node.left, prefix + (isLeft ? "|   " : "    "), true);
            printTree(node.right, prefix + (isLeft ? "|   " : "    "), false);
        }
    }


    public static void main(String[] args) {
        String[] keys = {"Is it a fruit?", "Is it sweet?", "Is it round?", "Is it red?"};
        double[] p = {0.1, 0.2, 0.4, 0.3};
        double[] q = {0.1, 0.1, 0.1, 0.1, 0.1};

        Node root = OBST(keys, p, q);

        System.out.println("Welcome to the Decision Path Game!");
        Scanner scanner = new Scanner(System.in);
        decision(root, scanner);
        printTree(root, "", true);
    }
}

