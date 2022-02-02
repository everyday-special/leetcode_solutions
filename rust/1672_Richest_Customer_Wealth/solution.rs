impl Solution {
    pub fn maximum_wealth(accounts: Vec<Vec<i32>>) -> i32 {
        let mut max_wealth = 0;
        let mut sum_account = 0;
        for acc in accounts.iter() {
            let sum_account = acc.iter().sum();
            if sum_account > max_wealth {
                max_wealth = sum_account;
            }
        }
        max_wealth
    }
}
