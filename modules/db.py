from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime, os
DB_PATH = os.environ.get('NAVI_DB','sqlite:///./navi_ai.db')
engine = create_engine(DB_PATH, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
class EventLog(Base):
    __tablename__ = 'event_logs'
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    type = Column(String(50))
    payload = Column(Text)
def init_db():
    Base.metadata.create_all(bind=engine)
def log_event(evt_type, payload):
    db = SessionLocal()
    e = EventLog(type=evt_type, payload=payload)
    db.add(e); db.commit(); db.close()
