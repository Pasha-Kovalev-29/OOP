2021-03-24 19:06:37.009469 ERROR:root:Email is already in use.
Traceback (most recent call last):
  File "D:/ALevel/OOP/Lesson 18/app.py", line 9, in main
    ivan = mod.Recruiter("Ivan", 'ivan@gmail.com', 100, 23)
  File "D:\ALevel\OOP\Lesson 18\models.py", line 9, in __init__
    self.validation()
  File "D:\ALevel\OOP\Lesson 18\models.py", line 21, in validation
    raise ValueError('Email is already in use.')
ValueError: Email is already in use.
2021-03-24 19:06:52.763370 ERROR:root:Email is already in use.
Traceback (most recent call last):
  File "D:/ALevel/OOP/Lesson 18/app.py", line 9, in main
    ivan = mod.Recruiter("Ivan", 'ivan@gmail.com', 100, 23)
  File "D:\ALevel\OOP\Lesson 18\models.py", line 9, in __init__
    self.validation()
  File "D:\ALevel\OOP\Lesson 18\models.py", line 21, in validation
    raise ValueError('Email is already in use.')
ValueError: Email is already in use.
