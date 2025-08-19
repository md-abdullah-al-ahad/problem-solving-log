/**
 * @param {number[]} nums
 * @return {number}
 */
var zeroFilledSubarray = function (nums) {
    let currentZeroCount = 0;
    let ans = 0;
    for (const num of nums) {
        if (num === 0) {
            currentZeroCount++;
            ans += currentZeroCount;
        } else {
            currentZeroCount = 0;
        }
    }
    return ans;
};
