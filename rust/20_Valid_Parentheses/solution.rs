use std::char;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack: Vec<char> = vec![];
        for ch in s.chars() {
            match ch {
                '{' => stack.push('}'),
                '[' => stack.push(']'),
                '(' => stack.push(')'),
                ch if stack.len() == 0 || stack.pop().unwrap() != ch => return false,
                _ => (),
            }
        }
        stack.len() == 0
    }
}
