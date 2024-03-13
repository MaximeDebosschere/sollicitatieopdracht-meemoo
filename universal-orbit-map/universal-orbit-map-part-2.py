def convert_input_file_to_orbit_tuples():
    f = open('input.txt', 'r')
    return [tuple(orbit.split(')')) for orbit in f.read().splitlines()]


def get_ancestors(orbits, space_object):
    result = set()
    while space_object != 'COM':
        # get parent of this space object
        space_object = list(filter(lambda x: x[1] == space_object, orbits))[0][0]
        result.add(space_object)
    return result


def count_orbital_transfers(orbits):
    you_ancestors = get_ancestors(orbits, 'YOU')
    san_ancestors = get_ancestors(orbits, 'SAN')

    unique_ancestors = you_ancestors.difference(san_ancestors).union(
        san_ancestors.difference(you_ancestors))

    return len(unique_ancestors)


orbit_tuples = convert_input_file_to_orbit_tuples()

print('Universal Orbit Map, part 2')
print('Answer:', count_orbital_transfers(orbit_tuples))
