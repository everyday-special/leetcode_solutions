impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        t.chars()
            .fold(0, |acc, ch| {
                match s.chars().nth(acc) {
                    Some(x) => acc + (ch == x) as usize,
                    None => acc,
                }
            }) == s.chars().count()
    }
}
