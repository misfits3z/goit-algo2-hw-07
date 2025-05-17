from functools import lru_cache
from SplayTree import SplayTree
import timeit
import matplotlib.pyplot as plt

@lru_cache(maxsize=None)
def fibonacci_lru(n):
    if n < 2:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)

def fibonacci_splay(n, tree):
    if tree.contains(n):
        return tree.get(n)
    if n < 2:
        tree.insert(n, n)
        return n
    value = fibonacci_splay(n - 1, tree) + fibonacci_splay(n - 2, tree)
    tree.insert(n, value)
    return value 

# Набір значень n
n_values = list(range(0, 951, 50))
lru_times = []
splay_times = []


# Вимірювання часу виконання 
for n in n_values:
    # LRU Cache
    lru_time = timeit.timeit(lambda: fibonacci_lru(n), number=3)
    lru_times.append(lru_time / 3)

    # Splay Tree
    tree = SplayTree()
    splay_time = timeit.timeit(lambda: fibonacci_splay(n, tree), number=3)
    splay_times.append(splay_time / 3)

# Побудова графіка 
plt.figure(figsize=(12, 6))
plt.plot(n_values, lru_times, marker="o", label="LRU Cache")
plt.plot(n_values, splay_times, marker="s", label="Splay Tree")
plt.title("Порівняння часу обчислення чисел Фібоначчі")
plt.xlabel("n — номер числа Фібоначчі")
plt.ylabel("Середній час виконання (секунди)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Таблиця 
print(f"{'n':<6}{'LRU Cache Time (s)':<25}{'Splay Tree Time (s)':<25}")
print("-" * 60)
for n, lru, splay in zip(n_values, lru_times, splay_times):
    print(f"{n:<6}{lru:<25.8f}{splay:<25.8f}")
