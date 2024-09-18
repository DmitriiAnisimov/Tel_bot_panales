# импортируем ответ пользователю
from settings.message import MESSAGES
from settings import config
import itertools
# импортируем класс-родитель
from handlers.handler import Handler


class HandlerAllText(Handler):
    """
    Класс обрабатывает события нажатия на кнопки
    """

    def __init__(self, bot):
        super().__init__(bot)
        # шаг в заказе
        self.step = 0
        self.selected_brand = None

    def pressed_btn_category(self, message):
        """
        Обработка события нажатия на кнопку 'Выбрать товар'. А точне
        это выбор категории товаров
        """
        self.bot.send_message(message.chat.id, "Каталог брендов подгузников",
                              reply_markup=self.keybords.remove_menu())
        self.bot.send_message(message.chat.id, "Сделайте свой выбор",
                              reply_markup=self.keybords.category_menu())

    def pressed_btn_size(self, message, product):
        """
        Обработка события нажатия на кнопку 'Выбрать товар'. А точне
        это выбор категории товаров
        """
        self.selected_brand = config.KEYBOARD[product]
        self.bot.send_message(message.chat.id, 'Выбран бренд ' +
                              config.KEYBOARD[product],
                              reply_markup=self.keybords.remove_menu())
        self.bot.send_message(message.chat.id,
                              "Сделайте выбор размера подгузников",
                              reply_markup=self.keybords.size_menu())

    def pressed_btn_info(self, message):
        """
        Обработка события нажатия на кнопку 'О магазине'
        """
        self.bot.send_message(message.chat.id, MESSAGES['trading_store'],
                              parse_mode="HTML",
                              reply_markup=self.keybords.info_menu())

    def pressed_btn_settings(self, message):
        """
        Обработка события н
        Обработка события нажатия на кнопку 'Настройки'
        """
        self.bot.send_message(message.chat.id, MESSAGES['settings'],
                              parse_mode="HTML",
                              reply_markup=self.keybords.settings_menu())

    def pressed_btn_back(self, message):
        """
        Обработка события нажатия на кнопку 'Назад'
        """
        self.bot.send_message(message.chat.id, "Вы вернулись назад",
                              reply_markup=self.keybords.start_menu())

    def pressed_btn_product(self, message, sz):
        """
        Обработка события нажатия на кнопку 'Выбрать товар'. А точнее
        это выбор товара из категории
        """
        self.bot.send_message(message.chat.id, f'Выбран бренд {self.selected_brand} и размер {config.KEYBOARD[sz]}', reply_markup=self.keybords.set_select_category(self.selected_brand, config.KEYBOARD[sz]))
        self.bot.send_message(message.chat.id, "Выведены все найденые товары в порядке возрастания цены за штуку", reply_markup=self.keybords.category_menu())

    def pressed_btn_tov(self, sz):
        """
        Обработка события нажатия на кнопку 'Выбрать товар'. А точнее
        это выбор товара из категории
        """
        self.bot.send_photo(sz.id, 'https://ardiaprod.vtexassets.com/arquivos/ids/297676-1600-auto?v=638494762525970000&width=1600&height=auto&aspect=true')
        #self.bot.send_message(message.chat.id, f'Выбран бренд {self.selected_brand} и размер {config.KEYBOARD[sz]}', reply_markup=self.keybords.set_select_category(self.selected_brand, config.KEYBOARD[sz]))
        #self.bot.send_message(message.chat.id, "Выведены все найденые товары в порядке возрастания цены за штуку", reply_markup=self.keybords.category_menu())

    def handle(self):
        # обработчик(декоратор) сообщений,size_name
        # который обрабатывает входящие текстовые сообщения от нажатия кнопок.
        @self.bot.message_handler(func=lambda message: True)

        def handle(message):
            # ********** меню ********** #
            self.log_action.log_action(message)

            if message.text == config.KEYBOARD['CHOOSE_GOODS']:
                self.pressed_btn_category(message)

            if message.text == config.KEYBOARD['INFO']:
                self.pressed_btn_info(message)

            if message.text == config.KEYBOARD['SETTINGS']:
                self.pressed_btn_settings(message)

            if message.text == config.KEYBOARD['<<']:
                self.pressed_btn_back(message)

            # ********** меню (БРЕНДОВ)******
            if message.text == config.KEYBOARD['BRAND_1']:
                self.pressed_btn_size(message, 'BRAND_1')

            if message.text == config.KEYBOARD['BRAND_2']:
                self.pressed_btn_size(message, 'BRAND_2')

            if message.text == config.KEYBOARD['BRAND_3']:
                self.pressed_btn_size(message, 'BRAND_3')

            if message.text == config.KEYBOARD['BRAND_4']:
                self.pressed_btn_size(message, 'BRAND_4')

            if message.text == config.KEYBOARD['BRAND_5']:
                self.pressed_btn_size(message, 'BRAND_5')

            if message.text == config.KEYBOARD['BRAND_6']:
                self.pressed_btn_size(message, 'BRAND_6')

            if message.text == config.KEYBOARD['BRAND_7']:
                self.pressed_btn_size(message, 'BRAND_7')

            if message.text == config.KEYBOARD['BRAND_ALL']:
                self.pressed_btn_size(message, 'BRAND_ALL')

            # ********** меню (размеров)******

            for brand, size in itertools.product([self.selected_brand],
                                                 ['RN',
                                                  'P',
                                                  'M',
                                                  'G',
                                                  'XG',
                                                  'XXG',
                                                  'XXXG']):
                if message.text == config.KEYBOARD[size]:
                    self.pressed_btn_product(message, size)
