def subset(arr, index=0, output=None):
    if output == None:
        output = []

    # 1. Print the current subset immediately (every node is an answer)
    print(output)

    # 2. Base case: if we outrun the array, stop
    if index == len(arr):
        return

    # 3. Loop through remaining choices to build combinations
    for i in range(index, len(arr)):
        # Pick the number
        output.append(arr[i])
        
        # Move forward from the current picked element's next index
        subset(arr, i + 1, output)
        
        # Backtrack: remove it to try the next number in the loop
        output.pop()

# --- Run the Code ---
arr = [int(x) for x in input("Enter numbers: ").split()]
subset(arr)



'''
                                        []
                     /                   |            \
             Pick A /             Pick B |             \ Pick C
                   /                     |              \
                ["A"]                  ["B"]           ["C"]
                /   \                    |               (No items left)
        Pick B /     \ Pick C            | Pick C
              /       \                  |
          ["A","B"]  ["A","C"]       ["B","C"]

             |     (No items left)       |
      Pick C |                       (No items left)
             |
        ["A","B","C"]
       (No items left)

'''