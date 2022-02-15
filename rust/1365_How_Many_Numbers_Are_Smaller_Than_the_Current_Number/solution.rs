impl Solution {
    pub fn smaller_numbers_than_current(nums: Vec<i32>) -> Vec<i32> {
        let mut nums_sorted = nums.clone();
        nums_sorted.sort_unstable();
        nums.iter().map(|num| nums_sorted.iter().position(|r| r == num).unwrap() as i32).collect()
    }
}
