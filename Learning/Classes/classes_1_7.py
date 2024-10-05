import sys
from string import ascii_lowercase, ascii_uppercase, digits


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__sp = Point(x1, y1)
        self.__ep = Point(x2, y2)

    def set_coords(self, sp: Point, ep: Point):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f"Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}")


sys.exit(999)

class Message:
    def __init__(self, text: str):
        self.text = text
        self.fl_like = False


class Viber:
    __all_msg = []
    @classmethod
    def add_message(cls, msg: Message):
        # добавление нового сообщения в список сообщений;
        cls.__all_msg.append(msg)

    @classmethod
    def remove_message(cls, msg: Message):
        # удаление    сообщения    из    списка;
        cls.__all_msg.remove(msg)
    #
    @classmethod
    def set_like(cls, msg: Message):
        # поставить / убрать    лайк    для    сообщения    msg(т.е.изменить    атрибут
        # fl_like    объекта    msg: если
        # лайка    нет    то    он    ставится, если    уже    есть, то    убирается);
        cls.__all_msg[cls.__all_msg.index(msg)].fl_like = True

    @classmethod
    def show_last_message(cls, num: int):
        # отображение    последних    сообщений;
        [print(msg.text) for msg in cls.__all_msg[~(num - 1):]]

    @classmethod
    def total_messages(cls):
        # возвращает    общее    число    сообщений.
        return len(cls.__all_msg)





msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.show_last_message(2)
Viber.set_like(msg)
print(Viber.total_messages())
Viber.remove_message(msg)
print(Viber.total_messages())
sys.exit(999)

class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False


class AppStore:
    __all_apps = []

    @classmethod
    def add_application(cls, app):
        # добавление нового приложения app в магазин;
        cls.__all_apps.append(app)

    @classmethod
    def remove_application(cls, app):
        # удаление приложения app из магазина;
        cls.__all_apps.remove(app)

    @classmethod
    def block_application(cls, app):
        # блокировка приложения app(устанавливает локальное свойство  blocked объекта app в значение True);
        app.blocked = True

    @classmethod
    def total_apps(cls):
        # возвращает общее число приложений в магазине.
        return len(cls.__all_apps)

store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.total_apps()
store.block_application(app_youtube)
store.remove_application(app_youtube)

sys.exit(999)
class Video:

    def __init__(self):
        self.name = None

    def create(self, name):
        self.name = name

    def play(self):
        print(f"воспроизведение видео {self.name}")


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        cls.videos[video_indx].play()


v1, v2 = Video(), Video()
v1.create("Python")
v2.create("Python ООП")
YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.play(0)
YouTube.play(1)

sys.exit(999)

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @classmethod
    def check_card_number(cls, number):
        card_number = number.split('-')
        if len(card_number) == 4:
            for part in card_number:
                if all(list(map(str.isnumeric, part))):
                    continue
                else:
                    return False
            return all(list(map(lambda z: len(z) == 4, card_number)))
        else:
            return False

    @classmethod
    def check_name(cls, name):
        card_name = name.split()
        if len(card_name) == 2:
            for part in card_name:
                if all(list(map(lambda y: y in cls.CHARS_FOR_NAME, part))):
                    continue
                else:
                    return False
            return True
        else:
            return False


is_number = CardCheck.check_card_number("1A34-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
print(is_name, is_number)

class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        if 3 <= len(name) <= 50 and all(list(map(lambda x: x in cls.CHARS, name))):
            return name
        else:
            raise ValueError("некорректное поле name")

    def __init__(self, name, size=10):
        self.name = self.check_name(name)
        self.size = size

    def get_html(self):
        return f"<p class='password'>Логин: <input type='{self.name}' size={self.size} />"


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        if 3 <= len(name) <= 50 and all(list(map(lambda x: x in cls.CHARS_CORRECT, name))):
            return name
        else:
            raise ValueError("некорректное поле name")

    def __init__(self, name, size=10):
        self.name = self.check_name(name)
        self.size = size

    def get_html(self):
        return f"<p class='password'>Пароль: <input type='{self.name}' size={self.size} />"


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


login = FormLogin(TextInput('vsevolod'), PasswordInput('12345'))
html = login.render_template()

print(html)
