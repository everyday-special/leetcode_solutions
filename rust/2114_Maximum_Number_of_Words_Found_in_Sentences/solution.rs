use std::cmp;

impl Solution {
    pub fn most_words_found(sentences: Vec<String>) -> i32 {
        sentences.iter().fold(0, |acc, sentence| cmp::max(acc, (sentence.matches(' ').count() + 1) as i32))
    }
}
