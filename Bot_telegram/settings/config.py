import os
# импортируем модуль emoji для отображения эмоджи
from emoji import emojize

# токен выдается при регистрации приложения
TOKEN = '7033934923:AAHiPF-E6e4slDamOoBOWM_enfaOLM3Cts4'
# название БД
NAME_DB = 'pampers.db'
# версия приложения
VERSION = '0.0.1'
# автор приложния
AUTHOR = 'Dmitrii Anisimov'

# Absolute path to the directory containing the database file
DB_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..',
                                         'database'))

# Path to the database file
DATABASE = 'sqlite:///' + os.path.join(DB_FOLDER, NAME_DB)
'..',
COUNT = 0

# кнопки управления
KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Выбрать бренд'),
    'INFO': emojize(':speech_balloon: О боте'),
    'SETTINGS': emojize('⚙️ Настройки'),
    'BRAND_1': emojize('Pampers'),
    'BRAND_2': emojize('Huggies'),
    'BRAND_3': emojize('Duffy'),
    'BRAND_4': emojize('Babysec'),
    'BRAND_5': emojize('Estrella'),
    'BRAND_6': emojize('Carrefour'),
    'BRAND_7': emojize('Other'),
    'BRAND_ALL': emojize('All'),
    'SEMIPRODUCT': emojize(':pizza: Полуфабрикаты'),
    'GROCERY': emojize(':bread: Бакалея'),
    'ICE_CREAM': emojize(':shaved_ice: Мороженое'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ ЗАКАЗ'),
    'X': emojize('❌'),
    'DOUWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLAY': '✅ Оформить заказ',
    'COPY': '©️',
    'RN': 'RN',
    'P': 'P',
    'M': 'M',
    'G': 'G',
    'XG': 'XG',
    'XXG': 'XXG',
    'XXXG': 'XXXG'
}

# id категорий продуктов
CATEGORY = {
    'BRAND_1': 1,
    'BRAND_2': 2,
    'BRAND_3': 3,
    'BRAND_4': 4,
    'BRAND_5': 5,
    'BRAND_6': 6,
    'BRAND_7': 7,
    'BRAND_ALL': 8
}

# названия команд
COMMANDS = {
    'START': "start",
    'HELP': "help",
}
