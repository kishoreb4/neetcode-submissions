# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#         for num in nums:
#             count[num] = 1 + count.get(num,0)
#         arr = []
#         for num, cnt in count.items():
#             arr.append([cnt, num]) 
#         arr.sort()

#         res = []
#         while len(res) < k:
#             res.append(arr.pop()[1])
#         return res       

class Solution:
    def topKFrequent(self, nums: List[int], k:int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        dic = []
        for num, freq in count.items():
            dic.append((freq,num))
        dic.sort(reverse=True)    
        res = []
        for i in range(k):
            res.append(dic[i][1])
        return res 
             
        # res = defaultdict(int)
        # for each_num in nums:
        #     res[each_num]+=1
        # res_value = defaultdict(list)
        # for each_key, each_value in res.items():
        #     res_value[each_value].append(each_key)
        # for each_freq in sorted(res_value.keys(),reverse=True):
        #     [0:k]
        #     res_output = 
        # return 


        