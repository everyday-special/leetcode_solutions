impl Solution {
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
        let mut run_sum = 0;
        nums.iter()
            .map(|num| {
                run_sum += num;
                run_sum
            })
            .collect()
    }
}
