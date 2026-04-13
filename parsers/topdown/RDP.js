const parse = (input) => {
    let pos = 0;

    const match = (terminal) => {
        if (pos < input.length && input[pos] === terminal) {
            pos++;
            return true;
        }
        return false;
    };

    // E -> iB
    const parseE = () => {
        if (match("i")) {
            return parseB();
        }
        return false;
    };

    // B -> +iB | ε
    const parseB = () => {
        if (pos < input.length && input[pos] === "+") {
            if (match("+") && match("i")) {
                return parseB();
            }
            return false;
        }
        // ε production
        return true;
    };

    if (parseE() && pos === input.length) {
        return "Successful";
    }


    return "Failed";
};
