/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumArea = function (grid) {
    let [top, bottom, left, right] = [Infinity, -Infinity, Infinity, -Infinity];
    const n = grid.length;
    const m = grid[0].length;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (grid[i][j] === 1) {
                top = Math.min(top, i);
                bottom = Math.max(bottom, i);
                left = Math.min(left, j);
                right = Math.max(right, j);
            }
        }
    }
    return (bottom - top + 1) * (right - left + 1);
};
