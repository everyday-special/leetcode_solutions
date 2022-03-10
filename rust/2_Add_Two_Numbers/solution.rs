// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut l1 = l1;
        let mut l2 = l2;
        let mut dummy = Some(Box::new(ListNode::new(-1)));
        let mut curr = dummy.as_mut().unwrap();
        let mut carry = 0;
        while l1 != None && l2 != None {
            let val = (l1.as_ref().unwrap().val + l2.as_ref().unwrap().val + carry) % 10;
            carry = (l1.as_ref().unwrap().val + l2.as_ref().unwrap().val + carry) / 10;
            curr.next = Some(Box::new(ListNode::new(val)));
            l1 = l1.unwrap().next;
            l2 = l2.unwrap().next;
            curr = curr.next.as_mut().unwrap();
        }
        while l1 != None {
            let val = (l1.as_ref().unwrap().val + carry) % 10;
            carry = (l1.as_ref().unwrap().val + carry) / 10;
            curr.next = Some(Box::new(ListNode::new(val)));
            l1 = l1.unwrap().next;
            curr = curr.next.as_mut().unwrap();
        }
        while l2 != None {
            let val = (l2.as_ref().unwrap().val + carry) % 10;
            carry = (l2.as_ref().unwrap().val + carry) / 10;
            curr.next = Some(Box::new(ListNode::new(val)));
            l2 = l2.unwrap().next;
            curr = curr.next.as_mut().unwrap();
        }
        if carry != 0 {
            curr.next = Some(Box::new(ListNode::new(carry)));
        }
        dummy.unwrap().next
    }
}
