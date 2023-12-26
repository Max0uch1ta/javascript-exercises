
const removeFromArray = function(array, ...moreArgs) {
    let newArray = array
    for (const arg of moreArgs) {
        newArray = newArray.filter(function (element) {
            return element !== arg
        });
        }
    return newArray
};

// Do not edit below this line
module.exports = removeFromArray;
