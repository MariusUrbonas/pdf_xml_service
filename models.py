# coding: utf-8
from sqlalchemy import Column, JSON, Integer, Text, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Report(Base):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True, server_default=text("nextval('reports_id_seq'::regclass)"))
    type = Column(Text)

    def __repr__(self):
        return '<id: {}> <content: {}>'.format(self.id, self.type)
