from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers that add up to target using hash map approach.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], index]

            seen[num] = index

        return []


def test_solution():
    solution = Solution()

    # Test case 1
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]

    # Test case 2
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]

    # Test case 3
    assert solution.twoSum([3, 3], 6) == [0, 1]

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
