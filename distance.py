import sys
import math
def  find_min_point(x1, y1, x2, y2, x3, y3):
    max_x = int(max(x1, x2, x3))
    min_x = int(min(x1, x2, x3))
    max_y = int(max(y1, y2, y3))
    min_y = int(min(y1, y2, y3))
    result = (None, None)
    min_distance = sys.maxsize
    for j in range(min_y, max_y + 1):
        for i in range(min_x, max_x + 1):
            if isInOrOnTriangle(i, j, x1, y1, x2, y2, x3, y3):
                distance_sum = getDistance(i, j, x1, y1, x2, y2, x3, y3)
                if distance_sum < min_distance:
                    min_distance = distance_sum
                    result = (i, j)
                elif distance_sum == min_distance:
                    min_distance = distance_sum
                    result = max((i, j), result)
    print(min_distance)
    return list(result)

def  isInOrOnTriangle(i, j, x1, y1, x2, y2, x3, y3):
    diff_1 = (i - x1, j - y1)
    diff_2 = (i - x2, j - y2)
    diff_3 = (i - x3, j - y3)
    projection_1 = diff_1[0] * diff_2[1] - diff_1[1] * diff_2[0]
    projection_2 = diff_2[0] * diff_3[1] - diff_2[1] * diff_3[0]
    projection_3 = diff_3[0] * diff_1[1] - diff_3[1] * diff_1[0]
    if (projection_1 <= 0 and projection_2 <= 0 and projection_3 <= 0) or (projection_1 >= 0 and projection_2 >= 0 and projection_3 >= 0):
        return True 
    return False
        
def  getDistance(i, j, x1, y1, x2, y2, x3, y3):
    distance_1 = math.sqrt((i - x1) ** 2 + (j - y1) ** 2)
    distance_2 = math.sqrt((i - x2) ** 2 + (j - y2) ** 2)
    distance_3 = math.sqrt((i - x3) ** 2 + (j - y3) ** 2)
    return distance_1 + distance_2 + distance_3
    

x = find_min_point(0,0,1,1,2,0)
print(x)

    
                            
                