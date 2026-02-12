// This function can only pass the following grammar
// ==> E -> i + E
// ==> E -> i 

//           E
//         / | \
//       i   +   E
//                 \
//                   i

const parse = (input)=>{
    // Initialize the position in the input
    let pos = 0;

    // non-terminal 
    const parseE = () =>{

        let backtrackPos = pos;
    console.log("Trying E → i + E at pos:", pos);

    if (match("i") && match("+") && parseE()) {
        console.log("Matched i + E at pos:", pos);
        return true;
    }

    console.log("Backtracking from pos:", pos, "to", backtrackPos);
    pos = backtrackPos;

    console.log("Trying E → i at pos:", pos);

    if (match("i")) {
        console.log("Matched i at pos:", pos);
        return true;
    }

    pos = backtrackPos;
    return false;
    }

    // Helper to match terminal
    const match = (terminal)=>{
        if(pos < input.length && terminal === input[pos]){
            pos++;
            return true;
        }
        else{
            return false;
        }
    }

    // start parsing 
    console.log(pos);
    // console.log(input.length);
    if(parseE() && pos === input.length){
        return "Accepted";
    }
    else{
        return "Rejected"
    }
};

// Test cases
console.log(parse(['i', '+', 'i', '+', 'i'])); // Accepted
console.log(parse(['i', '+', 'i']));       // Accepted
console.log(parse(['i', '+']));            // Rejected