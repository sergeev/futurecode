import datetime
import os
import subprocess
from googletrans import Translator

reminders = [] # список напоминаний

def answer_question(question):
    if question == "Какой фильм посмотреть?":
        movies = ["Зеленая миля", "Форест Гамп", "Заводной апельсин"]
        print("Советую посмотреть:")
        for movie in movies:
            print(movie)
    elif question == "Сколько будет 2 ** 10?":
        print(2 ** 10)
    elif question == "Какое сегодня число?":
        print(datetime.date.today())
    elif question.startswith("Напомни мне встречу на"):
        reminder = question[19:]
        reminders.append(reminder)
        print("Я запомнил, что вам надо:", reminder)
    elif question == "Что у меня запланировано на сегодня?":
        if reminders:
            print("Ваши напоминания:")
            for reminder in reminders:
                print(reminder)
        else:
            print("У вас нет запланированных дел на сегодня")
    elif question.startswith("Оптимизируй фотографии в папке"):
        folder_name = question[34:]
        new_folder_name = folder_name + "_optimized"
        os.mkdir(new_folder_name)
        for filename in os.listdir(folder_name):
            if filename.endswith(".jpg") or filename.endswith(".jpeg"):
                subprocess.run(["convert", "-resize", "50%", f"{folder_name}/{filename}",
                                f"{new_folder_name}/{filename}"])
        print("Фотографии оптимизированы и сохранены в новой папке:", new_folder_name)
    elif question.startswith("Переведи слово"):
        word = question[14:]
        translator = Translator()
        translation = translator.translate(word, dest="fr")
        print(f"Перевод слова '{word}' на французский: {translation.text}")
    elif question.startswith("Открой файл"):
        file_name = question[12:]
        os.startfile(file_name)
    else:
        print("Извините, я не понимаю ваш вопрос")

while True:
    user_input = input("Команда: ")
    answer_question(user_input)