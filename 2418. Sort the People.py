import time
start_time = time.time()
class Solution:
    def sortPeople(self, names, heights):
        for i in range(1,len(heights)):
            namesItem=names[i]
            item=heights[i]
            max_index=i-1
            while max_index>=0 and heights[max_index]<item:
                heights[max_index+1]=heights[max_index]
                names[max_index+1]=names[max_index]
                max_index-=1
            heights[max_index+1]=item
            names[max_index+1]=namesItem
        return names
        pass



s=Solution()
names = ["Mary","John","Emma"]
heights = [180,165,170]
names=["IEO","Sgizfdfrims","QTASHKQ","Vk","RPJOFYZUBFSIYp","EPCFFt","VOYGWWNCf","WSpmqvb"]
heights=[17233,32521,14087,42738,46669,65662,43204,8224]
print(s.sortPeople(names,heights))

print("--- %s seconds ---" % (time.time() - start_time))


["EPCFFt","RPJOFYZUBFSIYp","VOYGWWNCf","Vk","Sgizfdfrims","IEO","QTASHKQ","WSpmqvb"]