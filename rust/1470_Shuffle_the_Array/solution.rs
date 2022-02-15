impl Solution {
    pub fn shuffle(nums: Vec<i32>, n: i32) -> Vec<i32> {
        let mut answer = vec![];
        for i in 0..n {
            answer.push(nums[i as usize]);
            answer.push(nums[(i+n) as usize]);
        }
        answer
    }
}
