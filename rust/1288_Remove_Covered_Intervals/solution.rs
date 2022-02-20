// Slow O(N ** 2) solution

impl Solution {
    pub fn remove_covered_intervals(intervals: Vec<Vec<i32>>) -> i32 {
        let mut answer = 0;
        let mut overlap = false;
        for i in 0..intervals.len() {
            overlap = false;
            for j in 0..intervals.len() {
                if i == j {
                    continue;
                }
                else if intervals[i][0] >= intervals[j][0] && intervals[i][1] <= intervals[j][1] {
                    overlap = true;
                }
            }
            if !overlap {
                answer += 1;
            }
        }
        answer
    }
}
