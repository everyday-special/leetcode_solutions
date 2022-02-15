use std::collections::HashMap;

impl Solution {
    pub fn num_identical_pairs(nums: Vec<i32>) -> i32 {
        let mut hash_map = HashMap::new();
        let mut answer = 0;
        for num in &nums {
            match hash_map.get(num) {
                None => hash_map.insert(num, 1),
                Some(&count) => {
                    answer += count;
                    hash_map.insert(num, count + 1)
                }
            };
        }
        answer
    }
}
