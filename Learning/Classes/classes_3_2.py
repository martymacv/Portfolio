import random
import sys
from string import ascii_lowercase, digits


class RenderDigit:
    def __call__(self, obj, *args, **kwargs):
        try:
            return int(obj)
        except:
            return


class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            return list(map(self.render, func(*args, **kwargs).split()))
        return wrapper


render = RenderDigit()
d1 = render("123")   # 123 (целое число)
d2 = render("45.54")   # None (не целое число)
d3 = render("-56")   # -56 (целое число)
d4 = render("12fg")  # None (не целое число)
d5 = render("abc")   # None (не целое число)


@InputValues(render=RenderDigit())
def input_dg():
    return input()


res = input_dg()
inp = InputValues(render=RenderDigit())(input)
print(res)

sys.exit()
class Handler:
    def __init__(self, methods):
        self.methods = methods

    def __call__(self, func):
        wrap = {
            'GET': self.get,
            'POST': self.post
        }

        def wrapper(request, *args, **kwargs):
            method = request.get('method', 'GET')
            if method in self.methods:
                return wrap[method](func, request)
        return wrapper

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def get(self, func, request, *args, **kwargs):  # для имитации обработки GET - запроса
        return f"GET: {func(request)}"

    def post(self, func, request, *args, **kwargs):  # для имитации обработки POST - запроса
        return f"POST: {func(request)}"


@Handler(methods=('GET', 'POST'))  # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "POST", "url": "contact.html"})
print(res)

sys.exit()


class HandlerGET:
    def __init__(self, func):
        self.func = func

    def __call__(self, request, *args, **kwargs):
        try:
            if request['method'] == 'GET':
                return f"{request['method']}: {self.func(request)}"
            else:
                return
        except KeyError:
            return f"GET: {self.func(request)}"


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "GET", "url": "contact.html"})


print(res)

sys.exit()
class RenderList:
    def __init__(self, type_list):
        if type_list in ('ul', 'ol'):
            self.type_list = type_list
        else:
            self.type_list = 'ul'

    def __call__(self, lst, *args, **kwargs):
        return f"<{self.type_list}>\n" + '\n'.join([f"<li>{menu}</li>" for menu in lst]) + f"\n</{self.type_list}>"


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)
sys.exit()
class DigitRetrieve:
    def __call__(self, number, *args, **kwargs):
        try:
            return int(number)
        except ValueError:
            return None


dg = DigitRetrieve()

d1 = dg("123")   # 123 (целое число)
d2 = dg("45.54")   # None (не целое число)
d3 = dg("-56")   # -56 (целое число)
d4 = dg("12fg")  # None (не целое число)
d5 = dg("abc")   # None (не целое число)
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)
sys.exit()
class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


# здесь прописывайте классы валидаторов: LengthValidator и CharsValidator
class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, string, *args, **kwargs):
        return self.min_length <= len(string) <= self.max_length


class CharsValidator:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string, *args, **kwargs):
        return set(string).issubset(set(self.chars))


lg = LoginForm("Вход на сайт", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
lg.post({"login": "root", "password": "panda"})
if lg.is_validate():
    print("Дальнейшая обработка данных формы")

sys.exit()
class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, filename: str, *args, **kwargs):
        return filename.endswith(tuple(map(lambda x: '.' + x, self.extensions)))


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]

sys.exit()
class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        return ''.join([random.choice(self.psw_chars) for _ in range(random.randint(self.min_length, self.max_length))])


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

rnd = RandomPassword(psw_chars, min_length, max_length)

psw = [rnd() for _ in range(3)]
lst_pass = [rnd() for _ in range(3)]
print(psw)