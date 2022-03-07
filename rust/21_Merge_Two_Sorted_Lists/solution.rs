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
    pub fn merge_two_lists(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut list1 = list1;
        let mut list2 = list2;
        let mut dummy = Some(Box::new(ListNode::new(-1)));
        let mut curr = dummy.as_mut().unwrap();
        while list1 != None && list2 != None {
            if list1.as_ref().unwrap().val < list2.as_ref().unwrap().val {
                curr.next = list1.clone();
                list1 = list1.unwrap().next;
            } else {
                curr.next = list2.clone();
                list2 = list2.unwrap().next;
            }
            curr = curr.next.as_mut().unwrap();
        }
        if list1 != None {
            curr.next = list1.clone();
        } else {
            curr.next = list2.clone();
        }
        dummy.unwrap().next
    }
}
