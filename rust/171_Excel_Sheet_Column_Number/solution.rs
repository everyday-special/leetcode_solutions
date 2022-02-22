impl Solution {
    pub fn title_to_number(column_title: String) -> i32 {
        column_title.chars().fold(0, |acc, ch| acc * 26 + (ch as i32) - 64)
    }
}
