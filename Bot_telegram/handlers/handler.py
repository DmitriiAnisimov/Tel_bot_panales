# импортируем библиотеку abc для реализации абстрактных классов
import abc
# импортируем разметку клавиатуры и клавиш
from markup.markup import Keyboards
# импортируем класс-менеджер для работы с библиотекой
from data_base.dbalchemy import DBManager
from log import ActionLogger


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, bot):
        # получаем объект бота
        self.bot = bot
        # инициализируем разметку кнопок
        self.keybords = Keyboards()
        # инициализируем менеджер для работы с БД
        self.BD = DBManager()

        self.log_action = ActionLogger('/home/dmitrii/Documents/Work/02_own_projects/02_parser/database/user_log.db')

    @abc.abstractmethod
    def handle(self):
        pass
