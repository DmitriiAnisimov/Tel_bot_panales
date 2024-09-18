# импортируем специальные типы телеграм бота для создания элементов интерфейса
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
# импортируем настройки и утилиты
from settings import config
# импортируем класс-менеджер для работы с библиотекой
from data_base.dbalchemy import DBManager


class Keyboards:
    """
    Класс Keyboards предназначен для создания и разметки интерфейса бота
    """
    # инициализация разметки

    def __init__(self):
        self.markup = None
        # инициализируем менеджер для работы с БД
        self.BD = DBManager()

    def set_btn(self, name, step=0, quantity=0):
        """
        Создает и возвращает кнопку по входным параметрам
        """

        return KeyboardButton(config.KEYBOARD[name])

    def start_menu(self):
        """
        Создает разметку кнопок в основном меню и возвращает разметку
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('CHOOSE_GOODS')
        itm_btn_2 = self.set_btn('INFO')
        itm_btn_3 = self.set_btn('SETTINGS')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        self.markup.row(itm_btn_2, itm_btn_3)
        return self.markup

    def info_menu(self):
        """
        Создает разметку кнопок в меню 'О магазине'
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        return self.markup

    def settings_menu(self):
        """
        Создает разметку кнопок в меню 'Настройки'
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        return self.markup

    @staticmethod
    def remove_menu():
        """
        Удаляет меню
        """
        return ReplyKeyboardRemove()

    def category_menu(self):
        """
        Создает разметку кнопок в меню категорий товара и возвращает разметку
        """
        self.markup = ReplyKeyboardMarkup(True, True, row_width=4)
        self.markup.row(self.set_btn('BRAND_1'), self.set_btn('BRAND_2'),
                        self.set_btn('BRAND_3'))
        self.markup.row(self.set_btn('BRAND_4'), self.set_btn('BRAND_5'),
                        self.set_btn('BRAND_6'))
        self.markup.row(self.set_btn('BRAND_ALL'), self.set_btn('BRAND_7'))
        self.markup.row(self.set_btn('<<'))
        return self.markup

    def size_menu(self):
        """
        Создает разметку кнопок в размеров товара и возвращает разметку
        """
        self.markup = ReplyKeyboardMarkup(True, True, row_width= 4)
        self.markup.row(self.set_btn('RN'), self.set_btn('P'), self.set_btn('M'))
        self.markup.row(self.set_btn('G'), self.set_btn('XG'), self.set_btn('XXG'), self.set_btn('XXXG'))
        self.markup.row(self.set_btn('<<'))
        return self.markup

    @staticmethod
    def set_inline_btn(name):
        """
        Создает и возвращает инлайн-кнопку по входным параметрам
        """
        return InlineKeyboardButton(f'{name.description}', callback_data=str(name.id))

    def set_select_category(self, category, sz):
        """
        Создает разметку инлайн-кнопок в выбранной
        категории товара и возвращает разметку
        """
        self.markup = InlineKeyboardMarkup(row_width=4)
        # загружаем в названия инлайн-кнопок данные
        if category == 'All':
            for itm in self.BD.select_all_products(category, sz)[:20]:
                self.markup.add(self.set_inline_btn(itm))
                self.markup.add(InlineKeyboardButton(f'Цена за шт. ${itm.unit_price}. Перейти в магазин {itm.store}', url=itm.link))
                self.markup.add(InlineKeyboardButton(text='────────────────────', url=itm.link))
            return self.markup
        else:
            for itm in self.BD.select_all_products_category(category, sz)[:20]:
                self.markup.add(self.set_inline_btn(itm))
                self.markup.add(InlineKeyboardButton(f'Цена за шт. ${itm.unit_price}. Перейти в магазин {itm.store}', url=itm.link))
                self.markup.add(InlineKeyboardButton(text='────────────────────', url=itm.link))
            return self.markup
