def getOtherPoint(point, segment):
    return [other for other in segment if other != point][0]

def draw(segments):
    points = set()
    for i in segments:
        points.update(((i[0], i[1]),))
        points.update(((i[2], i[3]),))
    #print points
    new_segments = [((x1, y1), (x2, y2)) for x1, y1, x2, y2 in segments]
    point_paths = dict()
    for i in points:
        point_paths[i] = sum(i in j for j in new_segments)
    #print point_paths
    odd_paths_point = filter(lambda x:(x[1] % 2) == 1, point_paths.items())
    #print odd_paths_point
    def draw_segment(point, segments, sofar):
        for match in [segment for segment in segments if point in segment]:
            segments_copy = list(segments)
            #print segments_copy
            segments_copy.remove(match)
            other_point = getOtherPoint(point, match)
            result = draw_segment(other_point, segments_copy, sofar + [other_point])
            if len(result) > 0:
                #print result
                return result
        return sofar if len(segments) == 0 else []
            #return sofar

    if len(odd_paths_point) > 2: return []
    if len(odd_paths_point) == 0:
        point = points.pop()
        return draw_segment(point, new_segments, [point])
    else:
        return draw_segment(odd_paths_point[0][0], new_segments, [odd_paths_point[0][0]])
    #for point in points:
    #    result = draw_segment(point, new_segments, [point])
    #    if len(result) != 0:
    #        return result
    ##print result
    #return []


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def checker(func, in_data, is_possible=True):
        user_result = func(in_data)
        if not is_possible:
            if user_result:
                print("How did you draw this?")
                return False
            else:
                return True
        if len(user_result) < 2:
            print("More points please.")
            return False
        data = list(in_data)
        for i in range(len(user_result) - 1):
            f, s = user_result[i], user_result[i + 1]
            if (f + s) in data:
                data.remove(f + s)
            elif (s + f) in data:
                data.remove(s + f)
            else:
                print("The wrong segment {}.".format(f + s))
                return False
        if data:
            print("You forgot about {}.".format(data[0]))
            return False
        return True

    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5)}), "Example 1"
    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7),
                    (4, 7, 7, 5), (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2)},
                   False), "Example 2"
    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5),
                    (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2), (1, 5, 7, 5)}), "Example 3"
    draw({(1,1,1,99),(99,99,1,99),(99,99,99,1),(99,1,1,1)})


