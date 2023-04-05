## Approach1 Brute Force

自分の回答とほぼ同じもの。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
```

前から順番にやってくから j の方は i+1 としていいのかと納得。

解説では force approach って揶揄されてた。

## Approach2 Two-pass Hash Table

```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
```

- `complement = target - nums[i]`とすることで complement が nums にあるかだけを判定するだけで良くなる。
- index を見つけなきゃいけないが、先に hashmap(index と数値の組)を作っておき、後から参照することで解決できる

非常に賢いなと思った。

## Approach 3: One-pass Hash Table

```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
```

- 一回の for 文で解決している。すげえ
