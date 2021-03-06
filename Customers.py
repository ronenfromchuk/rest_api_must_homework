from db_config import Base
from sqlalchemy import Column, UniqueConstraint, BigInteger, Text, ForeignKey
from sqlalchemy.orm import backref, relationship

class Customers(Base):
    __tablename__ = 'customers'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    first_name = Column(Text(), nullable=False)
    last_name = Column(Text(), nullable=False)
    address = Column(Text(), nullable=False, unique=True)

    def __repr__(self):
        return f'customer id={self.id} first name={self.first_name} last name={self.last_name} address={self.address} phone number={self.phone_number} credit number={self.credit_card_number} user id={self.user_id}'

    def __str__(self):
        return f'customer id={self.id} first name={self.first_name} last name={self.last_name} address={self.address} phone number={self.phone_number} credit number={self.credit_card_number} user id={self.user_id}'