class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = [int(rev) for rev in version1.split('.')], [int(rev) for rev in version2.split('.')]
        while len(v1) != len(v2):
            if len(v1) > len(v2):
                v2.append(0)
            else:
                v1.append(0)
        for i in range(len(v1)):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        return 0
