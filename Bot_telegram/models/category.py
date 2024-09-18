# компоненты библиотеки для описания структуры таблицы
from sqlalchemy import Column, String, Integer, Float

from data_base.dbcore import Base


class Category(Base):
    """
    Класс-модель для описания таблицы "Категория товара",
    основан на декларативном стиле SQLAlchemy
    """
    # название таблицы
    __tablename__ = 'pampers'

    # поля таблицы
    id = Column(Integer, primary_key=True)
    store = Column(String)
    date = Column(String)
    link = Column(String)
    description = Column(String)
    price = Column(Float)
    brand = Column(String)
    quantity = Column(Integer)
    size = Column(String)
    unit_price = Column(Integer)

    def __str__(self):
        return self.description
