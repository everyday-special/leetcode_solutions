// Naive approach using a HashMap

use std::collections::HashMap;
use std::cmp::max;

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut counts: HashMap<i32, i32> = HashMap::new();
        for num in nums.iter() {
            if !counts.contains_key(num) {
                counts.insert(*num, 1);
            }
            else {
                counts.insert(*num, counts[&num] + 1);
            }
        }
        counts.keys().fold(nums[0], |acc, n| {
            if counts[&n] > counts[&acc] {
                *n
            }
            else {
                acc
            }
        })
    }
}

// Solution using algorithm from discussion (linear time, constant space)

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut majority = nums[0];
        let mut freq = 0;
        for num in nums.iter() {
            if *num == majority {
                freq += 1;
            }
            else {
                freq -= 1;
                if freq == 0 {
                    freq = 1;
                    majority = *num;
                }
            }
        }
        majority
    }
}
