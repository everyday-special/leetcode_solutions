use std::collections::HashMap;

impl Solution {
    pub fn delete_and_earn(nums: Vec<i32>) -> i32 {
        let maxp1 = (nums.iter().max().unwrap() + 1) as usize;
        let mut points = vec![0; maxp1];
        let mut counts = HashMap::new();
        for num in nums {
            match counts.get(&num) {
                Some(x) => counts.insert(num, x + num),
                None => counts.insert(num, num),
            };
        }
        match counts.get(&1) {
            Some(x) => points[1] = *x,
            None => points[1] = 0,
        }
        for i in 2..maxp1 {
            match counts.get(&(i as i32)) {
                Some(x) => points[i] = std::cmp::max(points[i-2] + *x, points[i-1]),
                None => points[i] = std::cmp::max(points[i-2], points[i-1]),
            }
        }
        *points.last().unwrap()
    }
}
