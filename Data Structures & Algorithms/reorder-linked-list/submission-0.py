# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        nodes=[]
        #nodes.append(head)
        
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        start=0
        end=len(nodes)-1
        while start<end:
            nodes[start].next=nodes[end]
            start+=1
            if start>=end:
                break
            
            nodes[end].next=nodes[start]
            #start+=1
            end-=1
        nodes[start].next=None
        #return nodes
        

        

        
        