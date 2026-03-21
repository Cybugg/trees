// #### More in-depth on Binary Trees using Javascript ####

class TreeNode {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

let root = new TreeNode('R')
let nodeA = new TreeNode('A')
let nodeB = new TreeNode('B')
let nodeC = new TreeNode('C')
let nodeD = new TreeNode('D')
let nodeE = new TreeNode('E')
let nodeF = new TreeNode('F')
let nodeG = new TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG


//          R
//        /   \
//       A     B
//      / \   / \
//     C   D E   F
//              \
//               G

console.log("root.right.left.data:", root.right.left.val)


// Traversal of a binary tree can be done in three ways: pre-order, in-order, and post-order.

// Pre-order traversal: Visit the root node first, then recursively traverse the left subtree, followed by the right subtree.
// In-order traversal: Recursively traverse the left subtree first, then visit the root node, and finally recursively traverse the right subtree.
// Post-order traversal: Recursively traverse the left subtree first, then recursively traverse the right subtree, and finally visit the root node.

// Pre-order traversal: R, A, C, D, B, E, F, G
// In-order traversal: C, A, D, R, E, B, G, F
// Post-order traversal: C, D, A, E, G, F, B, R

// Let's implement the pre-order traversal using stack and recursion methods.

// Using stack for the traverssal depth search

const depthFirstValues = (root) => {
    // Lets check for edge cases
    if (!root) return []
    const stack = [root]
    const results = []

    while (stack.length > 0) {
        const current = stack.pop()
        results.push(current.val);
        console.log(current.val)
        if (current.right) stack.push(current.right)
        if (current.left) stack.push(current.left)
    }
    return results;
}

// Using recursion method for the traversal depth search

const depthFirstValuesRec = (root) => {
    if (!root) return [];
    const leftValues = depthFirstValuesRec(root.left);
    const rightValues = depthFirstValuesRec(root.right);
    return [root, ...leftValues, ...rightValues];
}

// In-order traversal using recursion method

const inOrderValues = (root) => {
    if (!root) return [];
    const leftValues = inOrderValues(root.left);
    const rightValues = inOrderValues(root.right);
    return [...leftValues, root, ...rightValues];
}

// Post-order traversal using recursion method

const postOrderValues = (root) => {
    if (!root) return [];
    const leftValues = postOrderValues(root.left);
    const rightValues = postOrderValues(root.right);
    return [...leftValues, ...rightValues, root]
}

// Time and space complexity for all three traversal methods is O(n) where n is the number of nodes in the tree, as we need to visit each node exactly once. The space complexity is also O(n) in the worst case (when the tree is completely unbalanced), and O(log n) in the best case (when the tree is perfectly balanced).

// print the previous traversals
console.log("## Pre-order traversal: ##");
console.log(depthFirstValues(root));
console.log(depthFirstValuesRec(root).map((node) => node.val));
console.log("## In-order traversal: ##");
console.log(inOrderValues(root).map((node) => node.val));

console.log("## Post-order traversal: ##");
console.log(postOrderValues(root).map((node) => node.val));

// #### Array implementation of a binary tree ####
const treeArr = ["R", "A", "B", "C", "D", "E", "F", null, null, null, null, null, null, null, "G"]

const leftChildArr = (i) => 2 * i + 1;
const rightChildArr = (i) => 2 * i + 2;

const preOrderArr = (i) => {
    if (i >= treeArr.length || !treeArr[i]) return;
    console.log(treeArr[i]);
    preOrderArr(leftChildArr(i));
    preOrderArr(rightChildArr(i));
}

const inOrderArr = (i) => {
    if (i >= treeArr.length || !treeArr[i]) return;
    inOrderArr(leftChildArr(i));
    console.log(treeArr[i]);
    inOrderArr(rightChildArr(i));
}

const postOrderArr = (i) => {
    if (i >= treeArr.length || !treeArr[i]) return;
    postOrderArr(leftChildArr(i));
    postOrderArr(rightChildArr(i));
    console.log(treeArr[i]);
}
console.log("## Pre-order traversal: ##");
console.log(preOrderArr(0));
console.log("## In-order traversal: ##");
console.log(inOrderArr(0));
console.log("## Post-order traversal: ##");
console.log(postOrderArr(0));

// Breadth first search using queue

const breadthFirstValue = (root) => {
    if (!root) return [];
    const queue = [root];
    const results = [];

    while (queue.length > 0) {
        const current = queue.shift();
        console.log(current.val);
        results.push(current.val)
        if (current.left) queue.push(current.left);
        if (current.right) queue.push(current.right);
    }
    return results;
}

// Search for a value in the tree
const treeIncludes = (root, target) => {
    if (!root) {
        return false;
    }
    if (root.val === target) {
        return true
    };
    return (treeIncludes(root.left, target) || treeIncludes(root.right, target));
}

console.log("## Breadth first search: ##");
console.log("########", breadthFirstValue(root));

console.log("");

console.log("## Tree Search includes C:", treeIncludes(root, 'C'));
console.log("## Tree Search includes z:", treeIncludes(root, 'z'));


// Binary search tree implementation

class BST_Node {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}


const inOrderTraversal = (node) => {
    if (!node || !node.val) return
    inOrderTraversal(node.left)
    console.log(node.val, end = ", ")
    inOrderTraversal(node.right)
}


let rootBST = new BST_Node(13)
let node7 = new BST_Node(7)
let node15 = new BST_Node(15)
let node3 = new BST_Node(3)
let node8 = new BST_Node(8)
let node14 = new BST_Node(14)
let node19 = new BST_Node(19)
let node18 = new BST_Node(18)

rootBST.left = node7
rootBST.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

// Traverse BST
console.log("#### BST Inordertraversal ####")
console.log(inOrderTraversal(rootBST))


// Search for a value in Binary search Tree

const searchBST = (root, target) => {
    if (root) {
        console.log("drop:")
        console.log(root.val)
    }
    if (!root || !target) {
        return false;
    }
    else if (root.val === target) {
        return true
    }
    else if (root.val > target) {
        return searchBST(root.left, target);
    }
    else {
        return searchBST(root.right, target);
    }
}

console.log("Searching BST: ", searchBST(rootBST, 14))

const insertBST = (root, val) => {
    if (!root) {
        return new BST_Node(val)
    }
    else {
        if (root.val < val) {
            root.right = insertBST(root.right, val)
        }
        else {
            root.left = insertBST(root.left, val)
        }
    }
    return root;
}
console.log("Before Insertion: ");
console.log(inOrderTraversal(rootBST));
console.log("After Insertion: ");
console.log(insertBST(rootBST, 45));
console.log(inOrderTraversal(rootBST));


// lets find the lowest 
const lowestValBST = (root) => {
    if (!root.left) {
        return root.val
    }
    return lowestValBST(root.left);
}

console.log("Lowest Value in the BST now: ")
console.log(lowestValBST(rootBST));

const deleteNodeBST = (root, val) => {
    if (!root) return null
    if (val < root.val) {
        root.left = deleteNodeBST(root.left, val)
    }
    else if (val > root.val) {
        root.right = deleteNodeBST(root.right, val)
    }
    else {
        if (!root.left) {
            return root.right;
        }
        else if (!root.right) {
            return root.left;
        }

        root.val = lowestValBST(root.right ,val);
        root.right = deleteNodeBST(root.right, root.val)
    }
    return root;
};

console.log("Before Deletion: ");
console.log(inOrderTraversal(rootBST));
console.log("After Deletion: ");
console.log(deleteNodeBST(rootBST, 15));
console.log(inOrderTraversal(rootBST));