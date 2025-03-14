from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey, create_engine
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    balance = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.datetime.now)

    # Relationship to Bets 
    bets = relationship('Bets', back_populates='user')

class Games(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date_time = Column(String, default=datetime.datetime.now, nullable=False)
    status = Column(String, default='scheduled')
    odds = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)

    # Relationship to Bets 
    bets = relationship('Bets', back_populates='game')

class Bets(Base):
    __tablename__ = 'bets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    game_id = Column(Integer, ForeignKey('games.id', ondelete="CASCADE"), nullable=False)
    amount = Column(Float, nullable=False)
    bet_type = Column(String, nullable=False)
    pay_out = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)

    # Relationships 
    user = relationship('User', back_populates='bets')
    game = relationship('Games', back_populates='bets')

# Database Connection
engine = create_engine("sqlite:///bets.db", echo=True)
SessionLocal = sessionmaker(bind=engine)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
