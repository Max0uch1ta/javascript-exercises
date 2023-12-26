const reverseString = function(string) {
    let stringToArr = string.split("")
    let newString = ""
    let lastChar = ""
    for (let i = 1, l = stringToArr.length; i <= l; i++) {
        lastChar = stringToArr.pop()
        newString += lastChar
    }
    return newString
};

reverseString("hello")


// Do not edit below this line
module.exports = reverseString;
