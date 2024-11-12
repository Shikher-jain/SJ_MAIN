import math
def polar_to_cartesian(distance, angle):
    angle_rad = math.radians(angle)
    x = distance * math.cos(angle_rad)
    y = distance * math.sin(angle_rad)
    return x, y

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def solve():
    n = int(input())
    device_info = {}

    for _ in range(n):
        device_data = input().split()
        device_id = int(device_data[0][:-1])
        num_connections = int(device_data[1])
        connections = []

        for _ in range(num_connections):
            target_id, distance, angle = map(int, input().split())
            connections.append((target_id, distance, angle))

        device_info[device_id] = connections

    start_device, end_device = map(int, input().split())

    coordinates = {start_device: (0, 0)}

    visited = set()
    visited.add(start_device)

    queue = [start_device]

    while queue:
        current_device = queue.pop(0)

        for target_id, dist, angle in device_info.get(current_device, []):
            if target_id not in visited:
                visited.add(target_id)
                x, y = polar_to_cartesian(dist, angle)
                prev_x, prev_y = coordinates.get(current_device, (0, 0))
                coordinates[target_id] = (prev_x + x, prev_y + y)
                queue.append(target_id)

    if start_device in coordinates and end_device in coordinates:
        x1, y1 = coordinates[start_device]
        x2, y2 = coordinates[end_device]
        distance = euclidean_distance(x1, y1, x2, y2)
        print(f"{distance:.2f}")
    else:
        print("NO")
solve()
