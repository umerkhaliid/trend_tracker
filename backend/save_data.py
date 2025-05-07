# backend/save_data.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import Session, Post
from data_processor.data_collector import get_fake_posts

def save_posts():
    session = Session()
    posts = get_fake_posts()
    for post in posts:
        new_post = Post(**post)
        session.add(new_post)
    session.commit()
    session.close()

if __name__ == "__main__":
    save_posts()
