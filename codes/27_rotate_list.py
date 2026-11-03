"""Program 27: Rotate a list by k positions."""

def rotate_list(items, k):
    if not items:
        return []

    k = k % len(items)

    return items[-k:] + items[:-k] if k != 0 else items.copy()


if __name__ == "__main__":
    items = list(map(int, input("Enter numbers separated by spaces: ").split()))
    k = int(input("Enter rotation positions: "))

    print("Rotated list:", rotate_list(items, k))