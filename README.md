* TASK 1:

Час виконання без кешу: 6.1206 секунд
Час виконання з кешем (LRU): 0.0233 секунд


* TASK 2:

1. LRU Cache

    Час виконання залишається стабільно низьким і практично не зростає зі збільшенням значення n.

    Це можливо завдяки тому, що обчислення для кожного n використовує кешовані значення попередніх викликів, що дозволяє уникати повторних обчислень.

    Наприклад:

        n = 50: 0.00000759 с

        n = 950: 0.00001095 с

    Складність: приблизно O(n), але завдяки кешу виконується ефективно як O(1) після першого виклику.

2. Splay Tree

    Час виконання монотонно зростає зі збільшенням n.

    Основна причина — відсутність прямої переваги повторного використання раніше обчислених значень. Навіть з урахуванням сплаювання, вставка та пошук у дереві мають логарифмічну або лінійну складність залежно від розбалансованості дерева.

    Наприклад:

        n = 50: 0.00003207 с

        n = 950: 0.00079337 с

    Складність: в середньому O(log n) на операцію, але кількість операцій у n також зростає, тому — гірше за lru_cache.