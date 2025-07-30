/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function (nums) {
    let n = nums.length;
    let mx = Math.max(...nums);
    let curr = 0;
    let ans = 1;
    for (let i = 0; i < n; i++) {
        if (nums[i] == mx) {
            curr++;
        }
        else {
            ans = Math.max(curr, ans);
            curr = 0;
        }
    }
    return Math.max(curr, ans);
};