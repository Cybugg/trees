class Node{
    constructor(val){
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");
const e = new Node("e");
const f = new Node("f");
const g = new Node("g");


a.left = b;
a.right = c;

b.left = d;
b.right = e;

c.left = f;
// c.right = g;


//          a
//        /   \
//       b     c
//      / \   / \
//     d   e f   g


// using stack for the traverssal depth search
// const depthFirstValues = (root) => {
//     // check for edge cases
//     if (!root) return [];
//     const stack = [root];
//     const results = [];

//     while(stack.length > 0){
//        const current = stack.pop();
//         results.push(current.val)
//         console.log(current.val)
//         if(current.right) stack.push(current.right);
//         if(current.left) stack.push(current.left);

//     }
// }


// Using recursion method for the traversal depth search

const depthFirstValues = (root)=>{
    if(!root) return [];
    const leftValues = depthFirstValues(root.left);
    const rightValues = depthFirstValues(root.right);
    return [root, ...leftValues, ...rightValues];
}

// using queue for the breadth traversal search
const breadthFirstValue = (root)=>{
    if(!root)return [];
    const queue = [root];
    const results = [];
    while(queue.length > 0){
        const current = queue.shift();
        console.log(current.val);
        results.push(current.val)
        if(current.left)queue.push(current.left);
        if(current.right)queue.push(current.right);
    }
    return results;
}

// Lets use recursion for the breadth first search


console.log("## Depth first search: ##");
// console.log(
// depthFirstValues(a))
console.log("## Breadth first search: ##");
console.log(breadthFirstValue(a));