class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:

        # Brute Force - not working for long encoded lists
        # nums1, nums2 = [], []
        # for [num, freq] in encoded1:
        #     for i in range(freq):
        #         nums1.append(num)
        # for [num, freq] in encoded2:
        #     for i in range(freq):
        #         nums2.append(num)

        # product_nums = []
        # for i in range(len(nums1)):
        #     product_nums.append(nums1[i] * nums2[i])
        # res = []

        # pointer = 0

        # for i in range(1, len(product_nums)):
        #     if product_nums[i] != product_nums[i - 1]:
        #         res.append([product_nums[i - 1], i - pointer])
        #         pointer = i
        # res.append([product_nums[i], i - pointer + 1])

        # return res

        # two while loops: 1 for get prod pairs, 1 for merge prod pairs => very slow
        # len1, len2 = len(encoded1), len(encoded2)
        # p1, p2 = 0, 0
        # temp_res = []
        # while p1 < len1 and p2 < len2:
        #     if encoded1[p1][1] == encoded2[p2][1]:
        #         temp_res.append([encoded1[p1][0] * encoded2[p2][0], encoded1[p1][1]])
        #         p2 += 1
        #         p1 += 1
        #     elif encoded1[p1][1] < encoded2[p2][1]:
        #         temp_res.append([encoded1[p1][0] * encoded2[p2][0], encoded1[p1][1]])
        #         encoded2[p2][1] -= encoded1[p1][1]
        #         p1 += 1
        #     else:
        #         temp_res.append([encoded1[p1][0] * encoded2[p2][0], encoded2[p2][1]])
        #         encoded1[p1][1] -= encoded2[p2][1]
        #         p2 += 1

        # res = []

        # num, freq = temp_res[0][0], temp_res[0][1]
        # index = 1
        # while index < len(temp_res):
        #     if temp_res[index][0] == num:
        #         freq += temp_res[index][1]
        #     else:
        #         res.append([num, freq])
        #         num, freq = temp_res[index]
        #     index += 1
        # res.append([num, freq])

        # return res

        """
        Intuition:
        2-pointers: 1 points to the pair in encoded1, 1 points to encoded2
        1. every time we append a result => freq -= min(freq1, freq2)
        2. when freq == 1, move the correspondent pointer
        3. check whether we need to merge two results pairs:
            if the num of the new pair equals to the previous one, sum up the two freqs
        """

        len1, len2 = len(encoded1), len(encoded2)
        p1, p2 = 0, 0
        res = []

        while p1 < len1 and p2 < len2:
            num1, freq1 = encoded1[p1]
            num2, freq2 = encoded2[p2]
            prodNum = num1 * num2
            prodFreq = min(freq1, freq2)
            encoded1[p1][1] -= prodFreq
            encoded2[p2][1] -= prodFreq
            if encoded1[p1][1] == 0:
                p1 += 1
            if encoded2[p2][1] == 0:
                p2 += 1
            if not res or prodNum != res[-1][0]:
                res.append([prodNum, prodFreq])
            else:
                res[-1][1] += prodFreq
        return res
