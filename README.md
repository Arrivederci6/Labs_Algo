# Лабораторні роботи з дисципліни "Алгоритмів і структур даних"

## Виконав: Морозов Андрій Дмитрович (Група ІР-25)

### Лабораторна робота №1 (Варіант 1 Рівень 1)

Дані два масиви цілих чисел nums1 і nums2, де nums1 є підмасивом nums2, якщо всі елементи nums1 знаходяться в nums2, в тому ж порядку.

Напишіть функцію is_subarray, яка приймає два масиви цілих чисел та повертає True, якщо nums1 є підмасивом nums2, та False в іншому випадку.

Приклади Вхідні дані: nums1 = 1,2,3, nums2 = 1,2,3,4 Результат: True Пояснення: Всі елементи nums1 ([1,2,3]) присутні в nums2.

Вхідні дані: nums1 = [4, 2], nums2 = [1,2,3,4] Результат: False Пояснення: Елементи nums1 ([4, 2]) не знаходяться в тому ж порядку в nums2.

Вхідні дані: nums1 = [1,3,5], nums2 = [1,2,3,4,5] Результат: True Пояснення: Елементи nums1 ([1,3,5]) присутні в nums2.

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку unittest та перевірити роботу вашої функції на прикладах, наведених вище

***
### Лабораторна робота №2 (Варіант 1 Рівень 1)

Магазин модного одягу розпочав сезонний розпродаж, i пропонує покупцям знижку на кожен 3-iй придбаний товар. Ви обрали товари, якi хочете придбати, i бажаєте скористатися цiєю пропозицiєю, щоб максимально зекономити кошти. Зрозумiло, що сума, яку вам доведеться заплатити, залежить вiд того, в якому порядку ви купуватимете товари. Знаючи цiну кожного товару, а також вiдсоток знижки, напишіть функцію підрахунку найвигiднiшої суми, за яку ви зможете придбати усi товари.

Вхiднi данi

Список цiлих чисел вiд 0 до 1000000000 включно — цiни окремих товарiв, якi ви хочете купити. Загальна кiлькiсть товарiв — вiд 1 до 10000. Значення discount — цiле число вiд 0 до 100 включно, яке означає вiдсоток знижки за кожен третiй товар.

Очікуваний результат мiнiмальна сума, яку потрiбно витратити, щоб придбати всi товари. Число повинне завжди мати два дробовi знаки, i округлюватися до другого знаку пiсля крапки.

Приклад 1 prices = 50 20 30 17 100 discount = 10

Результат prices = 207.00 Пояснення: Можна придбати в такому порядку: (20 + 50 + 100 · 0.9 + 17 + 30) = 207

Приклад 2 prices = 1 2 3 4 5 6 7 discount= 100

Результат 15.00

Приклад 3 prices = 1 1 1 discount=33 Результат 2.67

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку unittest та перевірити роботу вашої функції на прикладах, наведених вище

***
### Лабораторна робота №3 (Варіант 1 Рівень 1)

Існує три найпоширеніші способи проходження бінарних дерев вглиб: прямий (pre-order), зворотній (post-order) та серединний (in-order).

Реалізуйте функцію, яка отримує на вхід вершину бінарного дерева та виконує його зворотній обхід (pre-order traversal) та повертає значення вузлів у списку у відповідному порядку.
   Розглянемо таке бінарне дерево:

        1
       / \
      2    3
       \  / \
       5  6  7
Під час прямого обходу це дерево буде відвідане в такому порядку: [1, 2, 5, 3, 6, 7]

Функція pre_order_traversal(root: BinaryTree) -> List отримує на вхід корінь бінарного дерева, який має наступний вигляд:

    class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right

Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу BinaryTree наступним чином:

root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)

***
### Лабораторна робота №4 (Варіант 1 Рівень 2)
Дано лабіринт у формі двійкової прямокутної матриці, знайдіть найкоротший шлях у лабіринті від заданої точки до вказаного пункту призначення.

Шлях можна побудувати лише з використанням комірок, які містіть 1.  В будь-який момент ми можемо рухатися лише на один крок в одному з чотирьох напрямків:
Go Top: (x, y) ——> (x – 1, y)
Go Left: (x, y) ——> (x, y – 1)
Go Down: (x, y) ——> (x + 1, y)
Go Right: (x, y) ——> (x, y + 1)

Наприклад, розглянемо наступну двійкову матрицю. Якщо початкова точка  має координати (0, 0), а  пункт призначення = (7, 5), тоді найкоротший шлях від джерела до пункту призначення має довжину 12

[ 1  1  1  1  1  0  0  1  1  1 ]

[ 0  1  1  1  1  1  0  1  0  1 ]

[ 0  0  1  0  1  1  1  0  0  1 ]

[ 1  0  1  1  1  0  1  1  0  1 ]

[ 0  0  0  1  0  0  0  1  0  1 ]

[ 1  0  1  1  1  0  0  1  1  0 ]

[ 0  0  0  0  1  0  0  1  0  1 ]

[ 0  1  1  1  1  1  1  1  0  0 ]

[ 1  1  1  1  1  0  0  1  1  1 ]

[ 0  0  1  0  0  1  1  0  0  1 ]

Вхідні дані містяться у файлі input.txt у форматі:
0, 0 #початкова точка
7, 5 #точка призначення
10,10 # кількість рядків та стовпчиків у матриці

[ 1  1  1  1  1  0  0  1  1  1 ]

[ 0  1  1  1  1  1  0  1  0  1 ]

[ 0  0  1  0  1  1  1  0  0  1 ]

[ 1  0  1  1  1  0  1  1  0  1 ]

[ 0  0  0  1  0  0  0  1  0  1 ]

[ 1  0  1  1  1  0  0  1  1  0 ]

[ 0  0  0  0  1  0  0  1  0  1 ]

[ 0  1  1  1  1  1  1  1  0  0 ]

[ 1  1  1  1  1  0  0  1  1  1 ]

[ 0  0  1  0  0  1  1  0  0  1 ]


Результуючий файл має містити значення найкоротшого шляху від початкової точки до точки призначення

### Лабораторна робота №5 (Варіант 1 Рівень 2)
Державна установа

Код задачi: GOVERN

Для закордонної поїздки вам потрiбно отримати кiлька довiдок вiд держустанови.
Проте, виявилося, що для отримання цих довiдок потрiбнi iншi довiдки, а тi, в свою
чергу, потребують ще iнших довiдок.

На отримання кожної довiдки потрiбно вистояти чергу, тому ви хочете зекономити
час, не стоячи в черзi дарма (якщо ви не будете мати потрiбних довiдок, стоячи в
черзi, вам вiдмовлять у видачi цiєї).

Маючи iнформацiю про те, якi довiдки потрiбнi для яких, визначте оптимальний
порядок отримання усiх довiдок, при якому вам жодного разу не вiдмовлять у
видачi. Якщо таких оптимальних варiантiв кiлька — виведiть будь-який iз них.

Вхiднi данi:

Кожен iз N рядкiв вхiдного файлу govern .in мiстить два слова, роздiленi пробiлом
— назва довiдки та довiдка, яку потрiбно отримати перед нею.

   
   • Рядкiв може бути вiд 1 до 100000.
   
   • Слова мають довжину вiд 1 до 50 лiтер i складаються з цифр 0-9 i малих лiтер
латинського алфавiту вiд a до z.

   • Якщо для однiєї довiдки потрiбно отримати N iнших, файл мiститиме N рядкiв,
що починатимуться на одне й те саме слово.

   • Гарантовано iснує хоча б один порядок отримання довiдок, при якому можна
отримати усi довiдки.

Вихiднi данi:

Вихiдний файл govern .out повинен мiстити M рядкiв — назви довiдок в порядку їх
рекомендованого отримання.

Примiтка: Пiсля останнього слова також повинен бути символ переносу рядка (new-
line).

### Лабораторна робота №6 (Варіант 1 Рівень 2)
Створити функцію на мові програмування Python, яка приймає дві стрічки: "haystack" (довільний текст) та "needle" (шукана стрічка). Програма повинна знайти індекси всіх входжень стрічки "needle" в стрічці "haystack" та повернути цей індекс, використовуючи  метод Рабіна-Карпа для пошуку підстрічки у стрічці
