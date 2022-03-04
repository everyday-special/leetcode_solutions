impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
        let mut answer: Vec<i32> = vec![0];
        for i in 1..=n {
            if i % 2 == 1 {
                answer.push(answer[(i - 1) as usize] + 1);
            } else {
                answer.push(answer[(i / 2) as usize]);
            }
        }
        answer
    }
}
