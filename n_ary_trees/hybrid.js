class BinaryNode {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
        this.kind = "binary";
    }
    setLeft(val) {
        if (!this.left) {
            this.left = val;
        }
        return this;
    }
    setRight(val) {
        if (!this.right) {
            this.right = val;
        }
        return this;
    }

}

class NaryNode {
    constructor(val) {
        this.val = val;
        this.children = [];
        this.kind = "nary"
    }

    addChild(node) {
        this.children.push(node);
        return this;
    }
}

// Lets build the tree here;
const root = new NaryNode("A");

const n1 = new NaryNode("B");
const n2 = new NaryNode("C");
const n3 = new NaryNode("D");

// Binary subtree
const b1 = new BinaryNode("X");
const b2 = new BinaryNode("Y");
const b3 = new BinaryNode("Z");
const b4 = new BinaryNode("P");
const b5 = new BinaryNode("Q");

b1.setLeft(b2).setRight(b3);
b2.setLeft(b4).setRight(b5);

// Build N-ary side
n1.addChild(new NaryNode("E")).addChild(new NaryNode("F"));
n2.addChild(new NaryNode("G"));

root
    .addChild(n1)
    .addChild(b1) // binary tree inserted as a child
    .addChild(n2)
    .addChild(n3);



function traverseHybrid(node) {
    if (!node) {
        return;
    }
    console.log(node.val);
    if (node.kind === "binary") {
        traverseHybrid(node.left)
        traverseHybrid(node.right)
    }
    else if (node.kind === "nary") {
        for (let child of node.children) {
            traverseHybrid(child)
        }
    }
}

traverseHybrid(root);

// return arr <pre-order>
function traverseHybridRtnInArr(node) {
    if (!node) {
        return [];
    }
    let arr = [node.val]
    if (node.kind === "binary") {
        arr.push(...traverseHybridRtnInArr(node.left), ...traverseHybridRtnInArr(node.right))
    }
    else if (node.kind === "nary") {
        for (let child of node.children) {
            arr.push(...traverseHybridRtnInArr(child))
        }
    }
    return arr;
}

console.log(traverseHybridRtnInArr(root));
console.log("done.")