def combinationSumOptimized(candidates, target):
    results = []
    candidates.sort()  # Sort to enable early stopping

    def backtrack(start_index, target, path):
        if target == 0:
            results.append(list(path))
            return

        for i in range(start_index, len(candidates)):
            # Optimization: If this number is too big, all numbers after it are also too big!
            if candidates[i] > target:
                break  # Stop exploring this entire branch early
            
            path.append(candidates[i])
            # Pass 'i' as the next start_index to allow reusing the same element
            backtrack(i, target - candidates[i], path)
            path.pop()

    backtrack(0, target, [])
    return results
candidates=[int(x) for x in input("Enter numbers: ").split()]
target=int(input("Enter number: "))
print(combinationSumOptimized(candidates,target))