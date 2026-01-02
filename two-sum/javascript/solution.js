/**
 * Find two numbers that add up to target using hash map approach.
 *
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 *
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */
function twoSum(nums, target) {
    const seen = new Map();

    for (let index = 0; index < nums.length; index++) {
        const num = nums[index];
        const complement = target - num;

        if (seen.has(complement)) {
            return [seen.get(complement), index];
        }

        seen.set(num, index);
    }

    return [];
}

// Test cases
function testSolution() {
    console.assert(JSON.stringify(twoSum([2, 7, 11, 15], 9)) === JSON.stringify([0, 1]));
    console.assert(JSON.stringify(twoSum([3, 2, 4], 6)) === JSON.stringify([1, 2]));
    console.assert(JSON.stringify(twoSum([3, 3], 6)) === JSON.stringify([0, 1]));

    console.log("All tests passed!");
}

testSolution();
