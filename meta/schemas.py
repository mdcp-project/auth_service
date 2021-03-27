from pydantic import BaseModel

class VideoBase(BaseModel):
    cloudflare_video_id: str
    title: str
    thumbnail: str

class Video(VideoBase):
    id: int

    class Config:
        orm_mode = True