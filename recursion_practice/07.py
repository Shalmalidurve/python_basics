'''start=0

[]
├── choose 1
│      [1]
│      │
│      ├── choose 2
│      │      [1,2]
│      │      │
│      │      ├── choose 3
│      │      └── choose 4
│      │
│      ├── choose 3
│      └── choose 4
│
├── choose 2
│      [2]
│      ├── choose 3
│      └── choose 4
│
├── choose 3
└── choose 4'''
output=[]
def f(remaining=[1,2,3,4],path=[]):
    if len(remaining)==0:
        output.append(list(path))
        return

    for i in remaining:
        path.append(i)
        new=remaining[:i]+remaining[(i+1):]
        f(new,path)
        path.pop()
    return output

f()