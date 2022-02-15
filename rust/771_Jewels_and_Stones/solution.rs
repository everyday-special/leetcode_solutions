impl Solution_fold {
    pub fn num_jewels_in_stones(jewels: String, stones: String) -> i32 {
        jewels.chars().fold(0, |acc, j| acc + stones.matches(j).count()) as i32
    }
}

impl Solution_map {
    pub fn num_jewels_in_stones(jewels: String, stones: String) -> i32 {
        jewels.chars().map(|j| stones.matches(j).count() as i32).sum()
    }
}
