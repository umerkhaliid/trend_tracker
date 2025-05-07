# data_processor/analyze.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.db import Session, Post
from collections import Counter
import pandas as pd

def get_analysis():
    session = Session()
    posts = session.query(Post).all()
    df = pd.DataFrame([{
        "timestamp": p.timestamp,
        "text": p.text,
        "likes": p.likes,
        "comments": p.comments
    } for p in posts])
    
    df['hour'] = df['timestamp'].dt.hour
    hourly_activity = df['hour'].value_counts().sort_index()

    all_words = ' '.join(df['text']).split()
    word_freq = Counter(all_words)

    return hourly_activity, word_freq
