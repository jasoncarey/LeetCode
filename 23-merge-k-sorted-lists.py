Merge k Sorted Lists
# ----------
# Hard
# Linked List, Heap

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        h = []
        dummy = curr = ListNode(0)
        
        for i, l in enumerate(lists):
            if l: heappush(h, (l.val, i))
                
        while h:
            val, i = heappop(h)
            curr.next = ListNode(val)
            curr = curr.next
            
            if lists[i].next:
                heappush(h, (lists[i].next.val, i))
                lists[i] = lists[i].next
        
        return dummy.next
            