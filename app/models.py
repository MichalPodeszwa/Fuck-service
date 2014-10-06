from sqlalchemy import Integer, Text, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    fucks_given = Column(Integer)
    fucks_taken = Column(Integer)

    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.fucks_given = 0
        self.fucks_taken = 0


