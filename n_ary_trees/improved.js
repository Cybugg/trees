// Improved solutions to the N-ary tree problems
// Why this improved solution?
/**  The reason is simple. In the previous solution, to add value to the tree, we need the value of the parent nod. This itself presents a problem. The value is used as an identifier to search for the value. Identifiers must be unique. Thid means that a node's value must be unique. That is a flaw in our design. So in this solution, I will have it solved. */

const { idGenerate } = require("./utils/uuidGenerator")


class NaryNode {
    constructor(value) {
        this.id = idGenerate()
        this.value = value;
        this.children = [];
    }
}

class NaryTree {
    constructor(rootValue) {
        if (!rootValue) {
            throw new Error("Cannot initialize the tree without a value")
        }
        this.root = new NaryNode(rootValue);
    }

    // add child to the tree
    addChild(parentId, childValue) {
        let parent = this.find(this.root, parentId);
        if (!parent) {
            console.log("Parent not found");
            return;
        }
        parent.children.push(new NaryNode(childValue));

    }

    removeChild(id) {

        if (!this.root) return;
        if (this.root.id === id) {
            throw new Error("You cannot remove the root node");
        }

        const queue = [this.root];
        while (queue.length) {
            let current = queue.shift();

            // Check if any child matches the ID
            const index = current.children.findIndex(child => child.id === id);

            if (index !== -1) {
                // Remove it and stop searching this branch
                current.children.splice(index, 1);
                return;
            } else {
                // Otherwise, add children to queue to keep searching
                queue.push(...current.children);
            }
        }
    }

    // find node
    find(node, id) {
        if (!node) {
            return null;
        }
        if (node.id === id) {
            return node
        }
        for (let child of node.children) {
            let found = this.find(child, id);
            if (found) return found;
        }
        return null;
    }

    printHelper(node, level = 0) {
        if (!node) return;

        console.log("  ".repeat(level) + "value:", node.value, "id:", node.id);

        for (let child of node.children) {
            this.printHelper(child, level + 1);
        }
    }
    printTree() {
        return this.printHelper(this.root);
    }
};



const tree = new NaryTree(6);
console.log(tree);
tree.printTree(tree.root);
// tree.addChild(3);
