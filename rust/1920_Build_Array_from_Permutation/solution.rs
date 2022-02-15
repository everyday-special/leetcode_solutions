impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        let mut answer = vec![];
        for i in 0..nums.len() {
            answer.push(nums[nums[i] as usize])
        }
        answer
    }
}
