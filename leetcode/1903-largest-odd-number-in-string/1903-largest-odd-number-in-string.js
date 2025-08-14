/**
 * @param {string} num
 * @return {string}
 */
var largestOddNumber = function (num) {
    let pos = -1;
    const n = num.length;
    for (let i = n - 1; i >= 0; i--) {
        if (Number(num[i]) % 2 == 1) {
            pos = i;
            break;
        }
    }
    if (pos === -1) return "";
    return num.substring(0, pos + 1);
};
