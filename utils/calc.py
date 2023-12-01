import math


# convert any list to a list of numbers (works for nested lists too)
def to_nums(lst, convert=int):
    if type(lst) == list:
        return [to_nums(x, convert) for x in lst]
    else:
        return convert(lst)
    
# average of list
def avg(lst):
    return sum(lst)/len(lst)

# list of averages of lists
def avg_list(lst):
    return [avg(x) for x in lst]

# list of sums of lists
def sum_list(lst):
    return [sum(x) for x in lst]

# point1 and point2 are [x, y]
def find_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 
                     + (p2[1] - p1[1]) ** 2)

# point1 and point2 are [x, y, z]
def find_distance_3d(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 
                     + (p2[1] - p1[1]) ** 2
                     + (p2[2] - p1[2]) ** 2)

# point1 and point2 are [x, y]
def find_midpoint(p1, p2):
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

# point1 and point2 are [x, y, z]
def find_midpoint_3d(p1, p2):
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2, (p1[2] + p2[2]) / 2]

# convert degrees to radians
def degrees_to_radians(degrees):
    return degrees * math.pi / 180

# convert radians to degrees
def radians_to_degrees(radians):
    return radians * 180 / math.pi

# inputs a line [[x1, y1], [x2, y2]] and a point [x, y]
def is_on_line(l, p):
    dx, dy = l[1][0] - l[0][0], l[1][1] - l[0][1]
    d = math.sqrt(dx * dx + dy * dy)
    dx /= d
    dy /= d
    
    t = (p[0] - l[0][0]) / dx
    return p[1] == l[0][1] + t * dy

# find the closest 2 points in array of points
# points are [x, y]
def closest_points(points):
    closest = None
    closest_dist = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = find_distance(points[i], points[j])
            if dist < closest_dist:
                closest = [points[i], points[j]]
                closest_dist = dist
    return closest

# find the closest point in array to point p
# points are [x, y]
def closest_point(points, p):
    closest = None
    closest_dist = float('inf')
    for point in points:
        dist = find_distance(point, p)
        if dist < closest_dist:
            closest = point
            closest_dist = dist
    return closest


# inputs 2 lines as line: [[x1, y1], [x2, y2]]
def intersect_lines(l1, l2):
    dx1, dy1 = l1[1][0] - l1[0][0], l1[1][1] - l1[0][1]
    dx2, dy2 = l2[1][0] - l2[0][0], l2[1][1] - l2[0][1]
    
    det = dx1 * dy2 - dx2 * dy1
    # avoid parallel lines
    if det == 0:
        return False
    
    t1 = (dx2 * (l1[0][1] - l2[0][1]) - dy2 * (l1[0][0] - l2[0][0])) / det
    t2 = (dx1 * (l1[0][1] - l2[0][1]) - dy1 * (l1[0][0] - l2[0][0])) / det
    
    if 0 <= t1 <= 1 and 0 <= t2 <= 1:
        return [l1[0][0] + t1 * dx1, l1[0][1] + t1 * dy1]
    
    return None


# inputs 2 circles as circle: [[x, y], r]
def intersect_circles(c1, c2):
    dx, dy = c2[0][0] - c1[0][0], c2[0][1] - c1[0][1]
    d = math.sqrt(dx * dx + dy * dy)
    
    # avoid circles inside each other or too far apart
    if d < abs(c1[1] - c2[1]) or d > c1[1] + c2[1]:
        return False
    
    a = (c1[1] * c1[1] - c2[1] * c2[1] + d * d) / (2 * d)
    h = math.sqrt(c1[1] * c1[1] - a * a)
    
    x2 = c1[0][0] + a * dx / d
    y2 = c1[0][1] + a * dy / d
    
    x3 = x2 + h * dy / d
    y3 = y2 - h * dx / d
    
    x4 = x2 - h * dy / d
    y4 = y2 + h * dx / d
    
    return [[x3, y3], [x4, y4]]

# inputs 2 rectengles as rect: [[x1, y1, w1, h1], [x2, y2, w2, h2]]
def intersect_rectangles(r1, r2):
    x1, y1, w1, h1 = r1[0][0], r1[0][1], r1[1][0], r1[1][1]
    x2, y2, w2, h2 = r2[0][0], r2[0][1], r2[1][0], r2[1][1]
    
    # skip rectangles that don't touch
    if x1 + w1 < x2 or x2 + w2 < x1 or y1 + h1 < y2 or y2 + h2 < y1:
        return False
    
    x3 = max(x1, x2)
    y3 = max(y1, y2)
    x4 = min(x1 + w1, x2 + w2)
    y4 = min(y1 + h1, y2 + h2)
    
    return [[x3, y3], [x4, y4]]