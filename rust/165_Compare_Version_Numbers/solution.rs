impl Solution {
    pub fn compare_version(version1: String, version2: String) -> i32 {
        let mut ver1 = version1.split('.');
        let mut ver2 = version2.split('.');
        loop {
            let (v1, v2): (i32, i32) = match (ver1.next(), ver2.next()) {
                (Some(v1), Some(v2)) => (v1.parse().unwrap(), v2.parse().unwrap()),
                (Some(v1), None) => (v1.parse().unwrap(), 0),
                (None, Some(v2)) => (0, v2.parse().unwrap()),
                (None, None) => break,
            };
            match v1.cmp(&v2) {
                std::cmp::Ordering::Less => return -1,
                std::cmp::Ordering::Equal => continue,
                std::cmp::Ordering::Greater => return 1,
            }
        }
        0
    }
}
