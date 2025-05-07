# data_processor/data_collector.py
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import random

def get_fake_posts():
    keywords = ["AI", "ChatGPT", "Elections", "Bitcoin", "Climate"]
    posts = []
    for i in range(20):
        post = {
            "text": f"Sample post about {random.choice(keywords)}",
            "timestamp": datetime.now(),
            "likes": random.randint(1, 1000),
            "comments": random.randint(0, 500)
        }
        posts.append(post)
    return posts
