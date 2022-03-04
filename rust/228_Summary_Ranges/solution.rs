impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        let mut answer: Vec<String> = Vec::new();
        if nums.is_empty() {
            return answer;
        }
        let mut prev = nums[0];
        let mut start = nums[0];
        for i in 1..nums.len() {
            if nums[i] != prev + 1 {
                if prev != start {
                    answer.push(format!("{}->{}", start, prev));
                } else {
                    answer.push(format!("{}", start));
                }
                start = nums[i];
            }
            prev = nums[i]
        }
        if prev != start {
            answer.push(format!("{}->{}", start, prev));
        } else {
            answer.push(format!("{}", start));
        }
        answer
    }
}
