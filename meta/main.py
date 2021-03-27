from fastapi import FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel
import uvicorn
import secrets
import datetime
import jwt
import pika
import json
from typing import List

from db import SessionLocal, engine
import models, schemas, constants

from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.post('/video')
def add_video(video: schemas.VideoBase, db: Session = Depends(get_db)):
    db_video = models.Video(
        cloudflare_video_id=video.cloudflare_video_id,
        title=video.title,
        thumbnail=video.thumbnail
    )
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video

@app.get('/videos/{video_id}', response_model=schemas.Video)
def get_video(video_id: int, db: Session = Depends(get_db)):
    db_video = db.query(models.Video).get(video_id)
    if not db_video:
        HTTPException(404, detail=f"Video with {video_id} not found")
    return db_video

@app.get("/videos", response_model=List[schemas.Video])
def get_videos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = db.query(models.Video).offset(skip).limit(limit).all()
    return items

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)