use std::cmp;

impl Solution {
    pub fn min_partitions(n: String) -> i32 {
        n.chars().fold(-1, |acc, n| cmp::max(acc, n.to_digit(10).unwrap() as i32))
    }
}
