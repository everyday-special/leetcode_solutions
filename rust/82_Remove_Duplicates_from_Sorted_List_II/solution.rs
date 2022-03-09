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
    pub fn delete_duplicates(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if head == None {
            return head;
        }
        let mut head = head;
        let mut dummy = Some(Box::new(ListNode::new(-1000)));
        let mut curr = dummy.as_mut().unwrap();
        let mut temp = head.clone();
        head = head.unwrap().next;
        while head.as_ref() != None {
            if temp.as_ref().unwrap().val != head.as_ref().unwrap().val {
                curr.next = temp.clone();
                curr = curr.next.as_mut().unwrap();
            } else {
                while head.as_ref() != None && head.as_ref().unwrap().val == temp.as_ref().unwrap().val {
                    head = head.unwrap().next;
                }
            }
            temp = head.clone();
            if head.as_ref() != None {
                head = head.unwrap().next;
            } else {
                head = head;
            }
        }
        curr.next = temp;
        dummy.unwrap().next
    }
}
