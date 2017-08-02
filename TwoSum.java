public class Solution {
	public int[] twoSum(int[] nums, int target) {
		HashMap<Integer, Integer> table = new HashMap<Integer, Integer>();
		for (int i = 0; i < nums.length; i++) {
			int pairValue = target - nums[i];
			if (table.containsKey(pairValue)) {
				int value = table.get(target - nums[i]);
				return new int[] { i, value };
			}
			table.put(nums[i], i);
		}
		return new int[] { -1, -1 };
	}
}
