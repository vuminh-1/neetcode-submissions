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
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) return;
        ListNode slow, fast;
        slow = head;
        fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode second = reverseList(slow.next);
        slow.next = null;

        ListNode first = head;
        while (second != null) {
            ListNode temporaryNext1 = first.next;
            ListNode temporaryNext2 = second.next;

            first.next = second;
            second.next = temporaryNext1;

            first = temporaryNext1;
            second = temporaryNext2;
        }
        
    }
    public ListNode reverseList(ListNode head) {
        ListNode previous = null;
        ListNode current = head;
        while (current != null) {
            ListNode temporaryNextNode = current.next;
            current.next = previous;
            previous = current;
            current = temporaryNextNode;
        }
        return previous;
    }
    
}
