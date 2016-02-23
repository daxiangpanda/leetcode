from __future__ import division
import itertools
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        # lines = []
        # dict = {}
        # max = 0
        # for i in itertools.combinations(points,2):
        #     x1,x2,y1,y2 = i[0].x,i[1].x,i[0].y,i[1].y
        #     if x1 == x2:
        #         k = float("inf")
        #         b = x1
        #     else:
        #         k = (y1-y2)/(x1-x2)
        #         b = y1-k*(y1-y2)/(x1-x2)
        #     line = (round(k,10),round(b,10))
        #     line.append(line)
        # for i in lines:
        #     dict[i]=0
        # for i in lines:
        #     for j in points:
        #         if i[0] == float("inf"):
        #             if j[0] == i[1]:
        #                 dict[i]+=1
        #         elif j[1] == j[0]*i[0]+i[1]:
        #             dict[i]+=1
        # for i in lines:
        #     if dict[i]>max:
        #         max = dict[i]
        # return max


        if len(points) == 0:
            return 0
        if len(points) <= 2:
            return len(points)
        result = 0
        # 对于某个点来说，如果他和另外两个点分别组成的直线的斜率相同，则这三个点在同一直线上
        for i in range(len(points)):
            hm = {}
            samex = 1
            samep = 0
            for j in range(len(points)):
                if j != i:
                    # x,y值相同的点肯定是在同一个直线上的点，且samep表示的是与i点相同的点的数量
                    if points[j].x == points[i].x and points[j].y == points[i].y:
                        samep+=1
                    如果两个点的x值相同，则在同一条垂直于x轴的线上，samex指垂直于x轴的x值等于x的点的数量
                    if points[j].x == points[i].x:
                        samex+=1
                        continue
                    k = float(points[j].y-points[i].y)/float(points[j].x-points[i].x)
                    if hm.has_key(k):
                        hm[k] += 1
                    else:
                        hm[k] = 2
                    # 结果为过i点的斜率为k的点的数量（包括相同位置的点）
                    result = max(result,hm[k]+samep)
            # 对每个点都更新一次最大值
            result = max(result,samex)
        return result
