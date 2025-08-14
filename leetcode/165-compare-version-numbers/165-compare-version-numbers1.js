/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
var compareVersion = function (version1, version2) {
    const version1arr = version1.split(".");
    const version2arr = version2.split(".");
    const n1 = version1arr.length;
    const n2 = version2arr.length;
    const mn = Math.min(n1, n2);
    for (let i = 0; i < mn; i++) {
        if (Number(version1arr[i]) > Number(version2arr[i])) {
            return 1;
        }
        if (Number(version1arr[i]) < Number(version2arr[i])) {
            return -1;
        }
    }
    if (n1 > n2) {
        for (let i = mn; i < n1; i++) {
            if (Number(version1arr[i]) > 0) {
                return 1;
            }
        }
    }
    if (n1 < n2) {
        for (let i = mn; i < n2; i++) {
            if (Number(version2arr[i]) > 0) {
                return -1;
            }
        }
    }
    return 0;
};
