"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school_scores = [{'school_class': '2a', 'school_scores': [5, 2, 2, 5, 3, 5, 4]},
                     {'school_class': '3a', 'school_scores': [3, 4, 5, 2, 3, 2, 2, 2, 2]},
                     {'school_class': '4a', 'school_scores': [5, 3, 3, 5, 4, 2, 2, 5, 4, 3]},
                     {'school_class': '4a', 'school_scores': [2, 2, 3, 2, 2, 2, 2, 4, 4]}]

    school_sum = 0
    for my_class in school_scores:
      ave_score = round(sum(my_class['school_scores']) / len(my_class['school_scores']), ndigits=2)
      school_sum += ave_score
      print(f"Средний балл для класса {my_class['school_class']} составляет{ave_score}")

    print(f"Средний балл по школе составляет {round(school_sum / len(school_scores), ndigits=2)}")

if __name__ == "__main__":
    main()
