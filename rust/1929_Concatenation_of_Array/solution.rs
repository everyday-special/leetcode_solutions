impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let mut answer: Vec<i32> = vec![];
        let mut counter = 0;
        while counter < nums.len() * 2 {
            answer.push(nums[counter % nums.len()]);
            counter += 1;
        }
        answer
    }
}
