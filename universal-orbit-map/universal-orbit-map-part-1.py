def convert_input_file_to_orbit_tuples():
    f = open('input.txt', 'r')
    return [tuple(orbit.split(')')) for orbit in f.read().splitlines()]


def count_total_orbits(orbits, space_object='COM', tree_depth=0):
    result = tree_depth
    # loop through all children of this space object
    for orbit in filter(lambda x: x[0] == space_object, orbits):
        result += count_total_orbits(orbits, orbit[1], tree_depth + 1)
    return result


orbit_tuples = convert_input_file_to_orbit_tuples()

print('Universal Orbit Map, part 1')
print('Answer:', count_total_orbits(orbit_tuples))
