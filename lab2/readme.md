Разработка фрагмента веб-приложения, позволяющего фиксировать в журнале (текстовом файле) действия пользователя.
## code
```python
from blogSaveLog import Blogpost, Comment, beginLog, endLog
from time import sleep

beginLog('log.txt')
try:
	blogpost = Blogpost('Bill Gates', 'Unix sux!', 'bla bla bla! \nWindows rulez_!')

	blogpost.addComment(Comment('Linus Torvalds', 'You is stupid! Agrh!!'))

	blogpost.addComment(Comment('Денис Попов', 'Зато в линуксе не скучные обои!'))
finally:
	endLog()
```

## log
```

Blogpost:
  datetime: 2018-12-14 22:57:40.661263
  username: Bill Gates
  caption: Unix sux!
  text: 
---
bla bla bla! 
Windows rulez_!
---
  has 0 comments

Comment:
  datetime: 2018-12-14 22:57:40.661299
  username: Linus Torvalds
  text: 
---
You is stupid! Agrh!!
---

Comment:
  datetime: 2018-12-14 22:57:40.661309
  username: Денис Попов
  text: 
---
Зато в линуксе не скучные обои!
---
```
