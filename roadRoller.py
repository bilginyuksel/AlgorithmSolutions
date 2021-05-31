def find_road_roller_count_test(X, Y, width):
    locations = [(x, y) for x, y in zip(X, Y)]
    locations.sort(key=lambda loc: loc[0])

    road_roller_count = 1
    lowest_x_pos = locations[0][0]
    minimal_width = width // 2
    best_road_roller_pos = lowest_x_pos + minimal_width
    for location in locations:
        x, y = location
        if x > best_road_roller_pos + minimal_width:
            road_roller_count += 1
            best_road_roller_pos = x + minimal_width

    return road_roller_count


def find_road_roller_count(X, Y, width):
    locations = [(x, y) for x, y in zip(X, Y)]
    locations.sort(key=lambda loc: loc[0])

    road_roller_count = 1
    lowest_x_pos = locations[0][0]
    best_road_roller_pos = lowest_x_pos + width
    for location in locations:
        x, y = location
        if x > best_road_roller_pos:
            road_roller_count += 1
            best_road_roller_pos = x + width

    return road_roller_count

def assert_road_roller(X, Y, W):
    print(find_road_roller_count(X, Y, W), find_road_roller_count_test(X, Y, W))

assert_road_roller([2, 4, 5, 7, 9, 8, 10], [1, 1, 1, 1, 1, 1, 1], 2)
assert_road_roller([2, 4], [1, 1], 2)
assert_road_roller([5, 7, 8, 10], [1, 1, 1, 1], 2)
assert_road_roller([10, 9], [1], 1)
assert_road_roller([7, 10, 5], [4, 1, 9], 5)
assert_road_roller([2], [1], 2)