# Made with some help from the discussion section
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        mapp = {}
        for i, val in enumerate(arr):
            if val not in mapp:
                mapp[val] = {i}
            else:
                mapp[val].add(i)
        seen = [False] * len(arr)
        curr, nxt, count = [0], [], 0
        while len(curr) > 0:
            for i in curr:
                if seen[i]:
                    continue
                seen[i] = True
                if i == len(arr)-1:
                    return count
                if not seen[i-1] and i-1 > 0 and arr[i] != arr[i-1]:
                    nxt.append(i-1)
                if not seen[i+1] and i+1 > 0 and arr[i] != arr[i+1]:
                    nxt.append(i+1)
                if arr[i] not in mapp:
                    continue
                for node in mapp[arr[i]]:
                    if not seen[node]:
                        nxt.append(node)
                del mapp[arr[i]]
            curr, nxt = nxt, []
            count += 1
