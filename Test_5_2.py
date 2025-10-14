Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> text = input()
def_leppard
>>> a = len(text)
>>> print("Чудовищно мало" if a < 2 else
...       "Очень мало" if a < 5 else
...       "мало" if a < 10 else
...       "ok" if a < 30 else
...       "много" if a < 100 else
...       "чудовищно много"
... )
ok
