// #### reverse a string 

const reverseString = (str) => {
    if (str.length === 1) return str;
    return str[str.length - 1] + reverseString(str.slice(0, str.length - 1));
}

// #### The fibonacci sequence
const fibonacci = (n) => {
    if (n <= 0) return 0;
    if (n === 1) return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

// #### add all the number in an array

const sumArr = (arr) => {
    if (arr.length === 1) return arr[0];
    return arr[arr.length - 1] + sumArr(arr.slice(0, arr.length - 1))
}

console.log(sumArr([1, 2, 3, 15]))


// #### factorial
const factorial = (num) => {
    if (num === 1) return 1
    return num * factorial(num - 1)
}

console.log(factorial(10))

// #### Flatten an array
const flatArr = (arr) => {
    const result = [];

    for (let i = 0; i < arr.length; i++) {
        let val = arr[i];
        if (Array.isArray(val)) {
            result.push(...flatArr(val));
        }
        else {
            result.push(val)
        }
    }
    return result;
}
const input = [1, [2, 4, [3, 5, 6, [5, 6]]], 8];
const output = flatArr(input);
console.log(output);


// #### power function (base, exp)
const powMath = (base, pow) => {
    if (pow === 0) { return 1 };
    return base * powMath(base, pow - 1)
};


console.log(powMath(8, 2))


let testStr = "s";
let testStr2 = "racecar";
let testStr3 = "hello world";
let testStr4 = "a man a plan a canal panama";
let testStr5 = "no 'x' in nixon";

// Palindromme Checker 
const isPalindromme = (str, left = 0, right = str.length - 1) => {
    if (left >= right) {
        return true;
    }
    if (str[left] !== str[right]) {
        return false;
    }

    return isPalindromme(str, ++left, --right)
}

// Tetsing the palindromme function
console.log("---> ", testStr[0], testStr[testStr.length - 1])
console.log(isPalindromme(testStr))
console.log(isPalindromme(testStr2))
console.log(isPalindromme(testStr3))
console.log(isPalindromme(testStr4))
console.log(isPalindromme(testStr5))


// Binary Search -----> Note that the array must be sorted

const binarySearch = (arr, target, left = 0, right = arr.length - 1) => {
    // Edge case
    if (left > right) return false;
    let mid = Math.floor((right + left) / 2);
    //base case
    if (arr[mid] === target) return true;

    if (target > arr[mid]) {
        return binarySearch(arr, target, ++mid, right)
    }

    return binarySearch(arr, target, left, --mid)
}

// Testing the binary search function
const sortedArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log("----> ", sortedArr[0], sortedArr[sortedArr.length - 1])

console.log(binarySearch(sortedArr, 5)) // true
console.log(binarySearch(sortedArr, 11)) // false

//climbing stairs problem (with memoization and can also be used in the fibonacci sequence solution above)
function climbStairsMemo(n, memo = {}) {
  if (n === 0) return 1;
  if (n < 0) return 0;

  // Check cache
  if (memo[n]) return memo[n];

  // Store result
  memo[n] = climbStairsMemo(n - 1, memo) + climbStairsMemo(n - 2, memo);

  return memo[n];
}