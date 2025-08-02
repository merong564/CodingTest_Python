import sys

sensor_cnt = int(sys.stdin.readline().strip())
building_cnt = int(sys.stdin.readline().strip())
sensor_distances = list(map(int, sys.stdin.readline().strip().split()))

sensor_distances.sort()

diffs = [
    sensor_distances[i + 1] - sensor_distances[i] 
    for i in range(0, len(sensor_distances) - 1)
]
diffs.sort()

result = sum(diffs[0:len(diffs) - (building_cnt - 1)])
print(result)