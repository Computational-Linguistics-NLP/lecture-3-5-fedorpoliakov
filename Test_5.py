Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> text = input('Введите текст: ')
Введите текст: Я к вам пишу — чего же боле?
... Что я могу еще сказать?
... Теперь, я знаю, в вашей воле
... Меня презреньем наказать.
... Но вы, к моей несчастной доле
... Хоть каплю жалости храня,
... Вы не оставите меня.
... Сначала я молчать хотела;
... Поверьте: моего стыда
... Вы не узнали б никогда,
... Когда б надежду я имела
... Хоть редко, хоть в неделю раз
... В деревне нашей видеть вас,
>>> lenght = len(text)
>>> if lenght < 2:
...     measure = "Чудовищно мало"
... elif lenght < 5:
...     measure = "Очень мало"
... elif lenght < 10:
...     measure = "Мало"
... elif lenght < 30:
...     measure = "Ок"
... elif lenght < 100:
...     measure = "много"
... else:
...     measure = "чудовищно много"
... print(measure)
SyntaxError: invalid syntax
>>> 
>>> 
>>> if lenght < 2:
...     measure = "Чудовищно мало"
... elif lenght < 5:
...     measure = "Очень мало"
... elif lenght < 10:
...     measure = "Мало"
... elif lenght < 30:
...     measure = "Ок"
... elif lenght < 100:
...     measure = "много"
... else:
...     measure = "чудовищно много"
... 
...     
>>> print(measure)
Ок
>>> 
