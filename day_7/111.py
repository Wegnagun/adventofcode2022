from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # return list(set(nums))
        return len(set(nums))


if __name__ == '__main__':
    nums = [1, 1, 2]
    print(Solution().removeDuplicates(nums))
