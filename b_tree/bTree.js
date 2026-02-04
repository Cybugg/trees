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

const depthFirstValues = (root) => {
    const stack = [root];
    const results = [];

    while(stack.length > 0){
       const current = stack.pop();
        results.push(current.val)
        console.log(current.val)
        if(current.right) stack.push(current.right);
        if(current.left) stack.push(current.left);

    }
}



depthFirstValues(a);