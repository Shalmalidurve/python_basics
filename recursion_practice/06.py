'''
solve(i=0, path=[])

├── take nums[0]
│      path=[1]
│
│      solve(i=1)
│      │
│      ├── take nums[1]
│      │      path=[1,2]
│      │
│      │      solve(i=2)
│      │      │
│      │      ├── take nums[2]
│      │      └── skip nums[2]
│      │
│      └── skip nums[1]
│             path=[1]
│             solve(i=2)
│
└── skip nums[0]
       path=[]
       solve(i=1)'''

output=[]
def solve(nums=[1,2,3],i=0,path=[]):
    if i==len(nums):
        output.append(list(path))
        return 
    path.append(nums[i])
    solve(nums,i+1,path)
    path.pop()
    solve(nums,i+1,path)
    return output

print(solve([1,2,3]))