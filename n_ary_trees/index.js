// #### Node class for N-ary Tree


class NaryNode {
    constructor(value) {
        this.value = value;
        this.children = [];
    }
}

// Tree class
class NaryTree {
    constructor(rootValue) {
        this.root = rootValue ? new NaryNode(rootValue) : null;
    }

    // Add child to a parent node
    addChild(parentValue, childValue) {
        const parent = this.find(this.root, parentValue);
        if (!parent) {
            console.log("Parent not found");
            return;
        }
        parent.children.push(new NaryNode(childValue));
    }

    // Remove a node (by value)
    remove(value) {
        if (!this.root) return;

        if (this.root.value === value) {
            this.root = null;
            return;
        }

        const queue = [this.root];

        while (queue.length) {
            const node = queue.shift();

            // filter out the node to remove
            node.children = node.children.filter(child => {
                if (child.value === value) return false;
                queue.push(child);
                return true;
            });
        }
    }

    // Find node (DFS)
    find(node, value) {
        if (!node) return null;
        if (node.value === value) return node;

        for (let child of node.children) {
            const found = this.find(child, value);
            if (found) return found;
        }

        return null;
    }

    // Traverse the tree (DFS)
    dfsPreorder(node) {
        if (!node) return;

        console.log(node.value);

        for (let child of node.children) {
            dfsPreorder(child);
        }
    }
    dfsPostorder(node) {
        if (!node) return;

        for (let child of node.children) {
            dfsPostorder(child);
        }

        console.log(node.value);
    }
    // Traverse the tree (BFS)
    bfs(root) {
        if (!root) return;

        const queue = [root];

        while (queue.length) {
            const node = queue.shift();
            console.log(node.value);

            for (let child of node.children) {
                queue.push(child);
            }
        }
    }
    getHeight(node) {
        if (!node) return 0;

        let maxHeight = 0;

        for (let child of node.children) {
            maxHeight = Math.max(maxHeight, getHeight(child));
        }

        return maxHeight + 1;
    }
    printTree(node, level = 0) {
        if (!node) return;

        console.log("  ".repeat(level) + node.value);

        for (let child of node.children) {
            printTree(child, level + 1);
        }
    }
    countNodes(node) {
        if (!node) return 0;

        let count = 1;

        for (let child of node.children) {
            count += countNodes(child);
        }

        return count;
    }
}
// Example usage
//        A
//  /  |  \
// B   C   D
//   / \      |
//  E   F     G


const tree = new NaryTree("A");

tree.addChild("A", "B");
tree.addChild("A", "C");
tree.addChild("A", "D");

tree.addChild("B", "E");
tree.addChild("B", "F");

tree.addChild("D", "G");

console.log("DFS Preorder:");
dfsPreorder(tree.root);

console.log("DFS Postorder:");
dfsPostorder(tree.root);


console.log("BFS:");
bfs(tree.root);
const found = tree.find(tree.root, "F");
console.log(found ? "Found: " + found.value : "Not found");

tree.remove("B");

console.log("After deleting B:");
bfs(tree.root);