const sumAll = function(numOne, numTwo) {
    // Checlk that both are numbers over 0
    if (typeof numOne != "number" || typeof numTwo != "number" || numOne < 0 || numTwo < 0) {
        return "ERROR"
    }  
    let sum = 0;
    let smaller = 0;
    let larger = 0;
    // Check which number is largest first
    if (numOne < numTwo) {
        smaller = numOne;
        larger = numTwo;
    } else {
        smaller = numTwo;
        larger = numOne;
    }
    // Add number and increment by one
    while (smaller <= larger) {
        sum += smaller;
        smaller++;
    }

    // Return the sum
    return sum
};

// Do not edit below this line
module.exports = sumAll;
