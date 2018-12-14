# Без выбора
## Анализ работы декоратора deprecated

```python
def deprecated(func):
    import warnings
    code = func.__code__
    warnings.warn_explicit(
        func.__name__ + " is deprecated. ",
        category=DeprecationWarning,
        filename=code.co_filename,
        lineno=code.co_firstlineno + 1
    )
    
    return func
```
Данная функция декоратор позволяет обернуть в себя другую функцию и сделать ее "устаревшей", при использовании которой в стандартный поток ошибок будет печататся уведомлении об использовании устаревшей функции.
Будет напечатано
- имя функции
- имя файла
- номер линии
место откуда ее вызвали.

## В какой момент выводится предупреждение deprecated? 
Предупреждение будет выведено только в момент декодирования функции, и при экспорте этой устаревшей функции.

## Возможно ли сделать предупреждение для других ситуаций
Можно с использованием стороннего модуля https://deprecation.readthedocs.io/en/latest/

```python
def memorized(func):
 cache = {}
 @functools.wraps(func)
 def inner(*args, **kwargs):
     key = args + tuple(sorted(kwargs.items()))
     if key not in cache:
         cache[key] = func(*args, **kwargs)
     return cache[key]
 return inner
```

## Оптимизация memorized
Возможным вариантом оптимизации может быть хеширование аргументов, и хранение в словаре не tuple с аргументами, а их хеш.
Это может спасти от слишком большого выделения памяти, которое имеет место быть сейчас, но несет проблему коллизий

# С выбором
Разработка фрагмента веб-приложения, позволяющего фиксировать в журнале (текстовом файле) действия пользователя.
https://github.com/AnotherStudent/blogSample
