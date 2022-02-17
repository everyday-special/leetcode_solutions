class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combos, candidates = {}, set(candidates)
        for i in range(1, target + 1):
            if i in candidates:
                combos[i] = [[i]]
            temp = list(combos.keys())
            seen = set()
            for j in temp:
                if i - j in combos and j in candidates and i - j not in seen:
                    seen.add(j)
                    if i in combos:
                        for vals in combos[i - j]:
                            new = sorted([j] + vals)
                            if new not in combos[i]:
                                combos[i].append(new)
                    else:
                        combos[i] = []
                        for vals in combos[i - j]:
                            new = sorted([j] + vals)
                            if new not in combos[i]:
                                combos[i].append(new)
        if target in combos:
            return combos[target]
        else:
            return []
