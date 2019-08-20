

def uni(nums):
  zip = []
  for item in nums:
    if item not in zip:
      zip.append(item)
  return zip

print(uni([1,2,3,3,3,3,4,5])) 