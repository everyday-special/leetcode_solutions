impl Solution {
    pub fn minimum_sum(num: i32) -> i32 {
        let mut digits: Vec<i32> = num.to_string().chars().map(|ch| ch.to_digit(10).unwrap() as i32).collect();
        digits.sort_unstable();
        (digits[0] + digits[1]) * 10 + digits[2] + digits[3]
    }
}
