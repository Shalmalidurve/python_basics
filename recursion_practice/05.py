'''
solve("")
│
├── choose A
│    │
│    ├── solve("A")
│    │      ├── choose B
│    │      └── choose C
│
└── choose B
     │
     ├── solve("B")
     │      ├── choose A
     │      └── choose C'''

def solve(path=[]):
    if len(path)==2:
        print(list(path))
        return
    for ch in ['a','b','c']:
        if ch not in path:

            path.append(ch)
            solve(path)
            path.pop()
 
solve([])