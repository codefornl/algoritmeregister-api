from sqlalchemy import Column, Integer, Unicode, Boolean
from sqlalchemy_i18n import (
    make_translatable,
    translation_base,
    Translatable,
)


make_translatable(options={'locales': ['fi', 'en']})


class Algorithm(Translatable, Base):
    __tablename__ = 'algorithms'
    __translatable__ = {'locales': ['fi', 'en']}

    locale = 'en'  # this defines the default locale

    id = Column(Integer, primary_key=True, autoincrement=True)
    public = Column(Boolean)
    # author = Column(Unicode(255))


class AlgorithmTranslation(translation_base(Algorithm)):
    __tablename__ = 'algorithm_translation'

    name = Column(Unicode(255))
    description = Column(UnicodeText)
