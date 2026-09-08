test = input().split()
N = int(test[0])
Q = int(test[1])
char_list = []
for i in range(N):
  char_list.append(chr(65+i))

def ask(x, y):
    # True if x is lighter than y
    print("? " + x + " " + y, flush=True)
    return input() == "<"

def insert(chain, x, lo, hi):
    # binary-insert x into the sorted slice chain[lo:hi]
    while lo < hi:
        mid = (lo + hi) // 2
        if ask(x, chain[mid]):
            hi = mid
        else:
            lo = mid + 1
    chain.insert(lo, x)

def sort5():
    a, b = ("A", "B") if ask("A", "B") else ("B", "A")   # a < b
    c, d = ("C", "D") if ask("C", "D") else ("D", "C")   # c < d
    if ask(b, d):             # chain a < b < d, and c is known to be < d
        chain = [a, b, d]
        loser = c
    else:                     # chain c < d < b, and a is known to be < b
        chain = [c, d, b]
        loser = a
    insert(chain, "E", 0, 3)                   # 2 queries
    insert(chain, loser, 0, len(chain) - 1)    # at most 2 queries, skips the known max
    return chain

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        print("? " + left_half[i] + " " + right_half[j], flush=True)
        ans = input()

        if ans == "<":
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
if N == 5:
    char_list = sort5()
else:
    merge_sort(char_list)
final = "! "
for i in char_list:
    final += i
print(final, flush=True)