impl Solution {
    pub fn champagne_tower(poured: i32, query_row: i32, query_glass: i32) -> f64 {
        let mut tower: Vec<Vec<f64>> = vec![vec![poured as f64]];
        for row in 1..=(query_row) {
            let mut next_row: Vec<f64> = vec![0.0; (row + 1) as usize];
            for glass in 0..tower.len() {
                let volume = tower[(row - 1) as usize][glass];
                if volume > 1.0 {
                    let runoff = (volume - 1.0) / 2.0;
                    next_row[glass] += runoff;
                    next_row[glass+1] += runoff;
                }
            }
            tower.push(next_row)
        }
        if tower[query_row as usize][query_glass as usize] > 1.0 {
            1.0
        } else {
            tower[query_row as usize][query_glass as usize]
        }
    }
}
