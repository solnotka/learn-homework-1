"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def compare_strings(str1, str2):
      if type(str1) == type(str2) == type('a'):
        if str1 == str2:
          return 1
        elif len(str1) > len(str2):
          return 2
        elif str2 == 'learn':
          return 3
      else:
        return 0

    print(compare_strings("learn", "python"))
    print(compare_strings(4, "python"))
    print(compare_strings(2, 18.6))
    print(compare_strings("learn", "learn"))
    print(compare_strings("my", "learn"))
    print(compare_strings("learn", "my"))
    
if __name__ == "__main__":
    main()
