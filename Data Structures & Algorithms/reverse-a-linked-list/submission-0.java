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
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return head;
        }
        ListNode result = new ListNode(head.val);
        ListNode currentNode = head.next;
        while (currentNode != null) {
           result = new ListNode(currentNode.val, result);
           currentNode = currentNode.next;
        }
        return result;
    }
}
