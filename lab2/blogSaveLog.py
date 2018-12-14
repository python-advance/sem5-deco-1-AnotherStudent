from datetime import datetime

log = None
def beginLog(fileName):
    global log
    log = open(fileName, 'w')

def endLog():
    log.close()

#-----------------------------------------------
class BaseRecord:
    def __init__(self, username, text):
        self._username = username
        self._text = text
        self._datetime = datetime.today()

    def __str__(self):
        return '\nDo not use BaseRecord!\n'

    @property
    def username(self):
        return self._username

    @property
    def datetime(self):
        return self._datetime

    @property
    def text(self):
        return self._text

    @text.setter
    def setText(self, text):
        self._text = text

#-----------------------------------------------
class Comment(BaseRecord):
    def __init__(self, username, text):
        super().__init__(username, text)
        log.write(str(self))

    def __str__(self):
        return \
            '\nComment:' + \
            '\n  datetime: ' + str(self.datetime) + \
            '\n  username: ' + self.username + \
            '\n  text: \n---\n' + self.text + '\n---' + \
            '\n'
#-----------------------------------------------
class Blogpost(BaseRecord):
    def __init__(self, username, caption, text):
        super().__init__(username, text)
        self._caption = caption
        self._comments = []
        log.write(str(self))

    def __str__(self):
        return \
            '\nBlogpost:' + \
            '\n  datetime: ' + str(self.datetime) + \
            '\n  username: ' + self.username + \
            '\n  caption: ' + self.caption + \
            '\n  text: \n---\n' + self.text + '\n---' \
            '\n  has ' + str(len(self.comments)) + ' comments' + \
            '\n'

    @property
    def caption(self):
        return self._caption

    @caption.setter
    def setCaption(self, caption):
        self._caption = caption

    @property
    def comments(self):
        return self._comments

    def addComment(self, comment):
        self.comments.append(comment)

    def strComments(self):
        s = ''
        for i in self.comments:
            s = s + str(i)
        return s

    

        

