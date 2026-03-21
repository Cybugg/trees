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
    if(!root) return []
    const stack = [root]
    const results = []

    while(stack.length > 0){
        const current = stack.pop()
        results.push(current.val);
        console.log(current.val)
        if(current.right) stack.push(current.right)
        if(current.left) stack.push(current.left)
     }
     return results;
}

// Using recursion method for the traversal depth search

const depthFirstValuesRec = (root)=>{
    if(!root) return [];
    const leftValues = depthFirstValuesRec(root.left);
    const rightValues = depthFirstValuesRec(root.right);
    return [root, ...leftValues, ...rightValues];
}

// In-order traversal using recursion method

const inOrderValues = (root)=>{
    if(!root) return [];
    const leftValues = inOrderValues(root.left);
    const rightValues = inOrderValues(root.right);
    return [...leftValues, root, ...rightValues];
}

// Post-order traversal using recursion method

const postOrderValues = (root)=>{
    if(!root) return [];
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
    if (i >= tree.length || !tree[i]) return;
    console.log(tree[i]);
    preOrder(leftChild(i));
    preOrder(rightChild(i));    
}

const inOrderArr = (i) => {
    if (i >= tree.length || !tree[i]) return;
    inOrder(leftChild(i));
    console.log(tree[i]);
    inOrder(rightChild(i));    
}

const postOrderArr = (i) => {
    if (i >= tree.length || !tree[i]) return;
    postOrder(leftChild(i));
    postOrder(rightChild(i));    
    console.log(tree[i]);
}
console.log("## Pre-order traversal: ##");  
console.log(preOrder(0));
console.log("## In-order traversal: ##");  
console.log(inOrder(0));
console.log("## Post-order traversal: ##");  
console.log(postOrder(0));

// Breadth first search using queue

const breadthFirstValue = (root) => {
    if(!root) return [];
    const queue = [root];
    const results = [];

    while(queue.length > 0){
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
    if(!root) return false;
    if(root.value === target) return true;
    return (treeIncludes(root.left, target) || treeIncludes(root.right, target));
}

console.log("## Breadth first search: ##");
console.log(breadthFirstValue(root));

console.log("");

console.log("## Tree Search includes c:", treeIncludes(root, 'c'));
console.log("## Tree Search includes z:", treeIncludes(root, 'z')); 


// Binary search tree implementation