# Tutorial and concepts for linked list



This tutorial records the various concepts and tricks I learnt in solving 
linkedlist problem in leetcode. 

> It is important to have a methodical approach for pointers while solving linked list. Sometimes, correct logic but haphazard pointers gives wrong answer.



## Reversing a linked list 



We use pointers for reversing a linked list. There are three pointers namely
curr, next and prev. As the name suggests ```curr``` points to the current node. 
The ```next``` pointer points to the node after ```curr``` and the ```prev``` 
points to the node before curr. 

At the beginning of the problem, ```prev``` points to ```None```, ```curr```
points to ```head``` (which is the head of the list) and ```next``` points to 
```None```. 

The loop goes till ```curr``` is ```None``` i.e. it has traversed the entire
list. 

```python
        prev = None
        curr = head
        next_ptr = None
        
        while curr !=None:
            next_ptr = curr.next
            
            curr.next = prev
            
            prev = curr
            curr = next_ptr
            
        head = prev
        
        return head
```

## Checking if a linked list is circular

To check if a linked list is circular we use the ```tortoise and hare``` problem.
We have a ```fast``` pointer and a ```slow``` pointer. 
While traversing, the ```fast``` pointer traverses two nodes and the ```slow```
traverses a single node in each iteration. 
If there is a loop in the linked list, there will be one such traversal iteration
when ```fast == slow```. 

```python
        if head == None or head.next == None:
            return False

        slow = head
        fast = head

        while fast.next !=None and fast.next.next !=None:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
```

## Finding the node where the loop for a circular linked list starts 

This problem is solved using two sub problems.

1. Find if the linked list has a loop (this was done in the above problem). 
2. Once you got the node where ```slow``` and ```fast``` pointer intersect, either
reinitialise ```slow``` or ```fast``` to ```head```  and traverse the linked list 
(1 node at a time for both ```slow``` and ```fast``` pointer ) ; the node where
this intersects is the node where the loop starts.

```python
        slow = head

        if slow == None or slow.next == None:
            return None

        fast = head

        # solves sub problem 1
        while fast != None and fast.next != None:

            try:
                slow = slow.next
                fast = fast.next.next
                if fast == slow:
                    break
            except:
                return None
         
         # Checks if fast does not go into a loop
        if fast == None or fast.next == None:
            return None
         
         # solves the second problem 
        fast = head
        while fast !=slow:
            fast = fast.next
            slow = slow.next

        return fast
```
 
