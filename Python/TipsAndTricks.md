# Tips and Tricks 

### Author Sudeshna Bora

---


## Finding frequency of Elements of a list

```python

import collections

a = [1,1,3,2,4,2]

frequency = collections.Counter(a)

{'1': 2, '3': 1, '2': 2, '4': 1}
```

---

## Find memory address 

```
id(variable_name)

```

---

## Get size of a variable

```
import sys

sys.getsizeof(variable_name)

```

---

## Render markdown file as html 

<b>Package: </b> grip

```
grip [-b] [port#] fileName.md
```
Here , ```-b``` means ```in browser```. 

---
