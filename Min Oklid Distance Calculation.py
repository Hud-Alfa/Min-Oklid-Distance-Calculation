def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    result = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return result

points = [(1, 2), (3, 4), (5, 6)]

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

min_distance = min(distances)
print(f"Minimum Mesafe: {min_distance}")
