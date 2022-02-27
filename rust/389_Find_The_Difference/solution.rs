use std::char;

impl Solution {
    pub fn find_the_difference(s: String, t: String) -> char {
        char::from_u32(s
            .chars()
            .fold(t
                .chars()
                .fold(0, |acc, ch| acc ^ (ch as u32)
            ), |acc, ch| acc ^ (ch as u32)
            )).unwrap()
    }
}
