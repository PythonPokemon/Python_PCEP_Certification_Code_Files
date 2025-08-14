"""
nums bekommt eine leere liste
nums wird vals zugewiesen, nun zeigt vals ebenfalls auf die lehre liste,
wenn man alo veränderung an vals vornimmt passieren diese auch in nums,

da beide jetzt die gleiche speicheradresse referenzieren!
"""

nums = []
vals = nums
vals.append(1)
print(nums)  # [1]
print(vals)  # [1]

print(id(nums))
print(id(vals))