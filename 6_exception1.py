"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    questions_dict = {"Привет!": "Рада тебя видеть", "Как дела?": "Хорошо!",
               "Что делаешь?": "Программирую", "Как тебя зовут?": "Командная строка", "Как меня зовут?": "Наташа", "В чем смысл жизни?": 42,
               "Какое у тебя любимое животное?": "Черная кошка", "Пока!": "До свидания"}
    
    user_question = ""
    while user_question != "Пока!":
      try:
        user_question = input("Задайте мне вопрос: ")
        if user_question in questions_dict:
          print(questions_dict[user_question])
        else:
          print("Я пока этого не знаю")
      except KeyboardInterrupt:
        print("Пока!")
        break
    
if __name__ == "__main__":
    ask_user()
