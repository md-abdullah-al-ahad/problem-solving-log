/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number = function (num) {
    const num1 = String(num);
    const n = num1.length;
    let idx = -1;
    let ans = num1;
    for (let i = 0; i < n; i++) {
        if (num1[i] === "6") {
            ans = num1.slice(0, i) + "9" + num1.slice(i + 1);
            break;
        }
    }
    return Number(ans);
};
