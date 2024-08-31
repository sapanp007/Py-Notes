# Collection

## defaultdict

Use of just a dict would give an KeyError as the key would not have initialized by the time we append a list item.

```python
from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = {} # Gives KeyError
d = defaultdict(list) # Works

for k, v in s:
    d[k].append(v)    
print(d)
```
