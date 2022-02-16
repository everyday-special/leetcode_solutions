impl Solution {
    pub fn count_points(points: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        queries.iter().map(|q| points.iter().fold(0, |acc, p| {
            if q[2].pow(2) >= (p[0] - q[0]).pow(2) + (p[1] -  q[1]).pow(2) {
                acc + 1
            }
            else {
                acc
            }
        })).collect()
    }
}
