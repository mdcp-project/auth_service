from sqlalchemy import Column, Integer, String
from db import Base

class Video(Base):
    __tablename__ = "video"

    id = Column(Integer, primary_key=True, index=True)
    cloudflare_video_id = Column(String, unique=True)
    title = Column(String)
    thumbnail = Column(String, nullable=True)
    
    def __repr__(self):
        return '<User {}: {}>'.format(self.id, self.title)
    
    def get_dict(self):
        return dict(id=self.id, title=self.title)