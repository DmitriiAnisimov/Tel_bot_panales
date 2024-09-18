# импортируем класс родитель
from handlers.handler import Handler
# импортируем сообщения пользователю
from settings.message import MESSAGES


class HandlerInlineQuery(Handler):
    """
    Класс обрабатывает входящие текстовые
    сообщения от нажатия на инлайн-кнопоки
    """

    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_product(self, call, code):
        """
        Обрабатывает входящие запросы на нажатие inline-кнопок товара
        """
        self.bot.answer_callback_query(
            call.id,
            text=MESSAGES['product_order'].format(
                self.BD.select_description(code),
                self.BD.select_store(code),
                self.BD.select_price(code),
                self.BD.select_unit_price(code)),
            show_alert=True)

    def handle(self):
        # обработчик(декоратор) запросов от нажатия на кнопки товара.
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            code = call.data
            if code.isdigit():
                code = int(code)

            self.pressed_btn_product(call, code)
