# Prefix Product 

This is a type of a data structure that stores product of all elements up to 
point. 

Asked in : https://leetcode.com/problems/product-of-the-last-k-numbers/

---

## Case 1 : The array has only non zero elements:

Let the array be 

```python

   a = [2,4,6,8,9,10]
```

If we want to the product of the last k (say k is 3 here) : we can either 
do a loop of k from k=3 to k=1 and multiply this elements. 

The complexity here is O(k). If this is a clear cut question to find the product
of last k elements of an array; I believe this is the best way to do.

However, in case the data comes in stream we can use prefix array.

We create an array ```prefix``` of length 1 having an element 1. Whenever a new
element comes, we append the product of the previous element of ```prefix``` 
with the current element; thus every element of ```prefix``` array has the product
of all preceding elements. 

Now, if we want the last k elements. We can divide the last entry of ```prefix```
with the element preceding the kth element from the end. 
So looking at a, our prefix element will be 

```python

prefix = [1 2 8 48 ... ]
```

## Case 2 : The element has one or more zero elements:

The previous approach reaches a road block when any element is 0 cause product 
of all elements upto that point becomes 0 but we cannot have an element in 
```prefix``` to be 0. 
In this case, we reinitialise ```prefix``` as ```[1]```. 
So the product of k elements in this case becomes 

```python
        n = len(prefix) - 1
        # there is a zero in the product
        if k >n : 
            return 0        

        return prefix[-1] // prefix[n-k]
```



