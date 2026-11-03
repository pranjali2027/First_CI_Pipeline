"""Program 28: Find the intersection of two sets."""

def set_intersection(first, second):
    result = set()

    for item in first:
        if item in second:
            result.add(item)

    return result


if __name__ == "__main__":
    first = set(map(int, input("Enter first set elements: ").split()))
    second = set(map(int, input("Enter second set elements: ").split()))

    print("Intersection:", set_intersection(first, second))