/**
 * @param {string} num
 * @return {string}
 */
var largestGoodInteger = function (num) {
    let largestDigit = -1;
    const n = num.length;
    for (let i = 2; i < n; i++) {
        if (num[i - 2] === num[i - 1] && num[i - 1] === num[i]) {
            largestDigit = Math.max(largestDigit, Number(num[i]));
        }
    }
    if (largestDigit !== -1) return String(largestDigit).repeat(3);
    return "";
};
