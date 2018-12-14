from blogSaveLog import Blogpost, Comment, beginLog, endLog
from time import sleep

beginLog('log.txt')
try:
	blogpost = Blogpost('Bill Gates', 'Unix sux!', 'bla bla bla! \nWindows rulez_!')

	blogpost.addComment(Comment('Linus Torvalds', 'You is stupid! Agrh!!'))

	blogpost.addComment(Comment('Денис Попов', 'Зато в линуксе не скучные обои!'))
finally:
	endLog()
