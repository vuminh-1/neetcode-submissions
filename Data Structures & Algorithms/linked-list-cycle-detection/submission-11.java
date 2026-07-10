/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode pointer1 = head;
        if (pointer1 == null) {
            return false;
        }
        ListNode pointer2 = head.next;
        if (pointer2 == null) {
            return false;
        }
        while (pointer1 != pointer2) {
            pointer1 = pointer1.next;
            if (pointer2.next == null) {
                return false;
            }
            else {
                pointer2 = pointer2.next.next;
            }
            if (pointer1 == null || pointer2 == null) {
                return false;
            }
        }
        return true;
    }
}
