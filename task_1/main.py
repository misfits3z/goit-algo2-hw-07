from LRUCache import LRUCache
import random
import time


def range_sum_no_cache(array, L, R):
    return sum(array[L : R + 1])


def update_no_cache(array, index, value):
    array[index] = value


# кеш
lru_cache = LRUCache(1000)


def range_sum_with_cache(array, L, R):
    key = (L, R)
    cached_result = lru_cache.get(key)
    if cached_result is not None:
        return cached_result
    result = sum(array[L : R + 1])
    lru_cache.put(key, result)
    return result


def update_with_cache(array, index, value):
    array[index] = value
    lru_cache.invalidate_ranges_with_index(index)



N = 100_000
Q = 50_000

array1 = [random.randint(1, 100) for _ in range(N)]
array2 = array1.copy()  # Для кешу

# Змішані запити
queries = []
for _ in range(Q):
    if random.random() < 0.5:
        L = random.randint(0, N - 2)
        R = random.randint(L, N - 1)
        queries.append(("Range", L, R))
    else:
        idx = random.randint(0, N - 1)
        val = random.randint(1, 100)
        queries.append(("Update", idx, val))



start_no_cache = time.time()
for query in queries:
    if query[0] == "Range":
        range_sum_no_cache(array1, query[1], query[2])
    elif query[0] == "Update":
        update_no_cache(array1, query[1], query[2])
end_no_cache = time.time()



start_with_cache = time.time()
for query in queries:
    if query[0] == "Range":
        range_sum_with_cache(array2, query[1], query[2])
    elif query[0] == "Update":
        update_with_cache(array2, query[1], query[2])
end_with_cache = time.time()



print("Час виконання без кешу: {:.4f} секунд".format(end_no_cache - start_no_cache))
print("Час виконання з кешем (LRU): {:.4f} секунд".format(end_with_cache - start_with_cache))
