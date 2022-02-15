struct ParkingSystem {
    big_spaces: i32,
    med_spaces: i32,
    small_spaces: i32,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ParkingSystem {

    fn new(big: i32, medium: i32, small: i32) -> Self {
        Self {
            big_spaces: big,
            med_spaces: medium,
            small_spaces: small,
        }
    }
    
    fn add_car(&mut self, car_type: i32) -> bool {
        match car_type {
            1 => {
                if self.big_spaces > 0 {
                    self.big_spaces -= 1;
                    true
                }
                else {
                    false
                }
            }
            2 => {
                if self.med_spaces > 0 {
                    self.med_spaces -= 1;
                    true
                }
                else {
                    false
                }
            }
            3 => {
                if self.small_spaces > 0 {
                    self.small_spaces -= 1;
                    true
                }
                else {
                    false
                }
            }
            _ => false
        }
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * let obj = ParkingSystem::new(big, medium, small);
 * let ret_1: bool = obj.add_car(carType);
 */
