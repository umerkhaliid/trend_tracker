import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
import threading
import time
import schedule
import sys, os

# Allow imports from parent directories
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.db import Session, Post
from data_processor.data_collector import get_fake_posts

# ---------------- Scheduler Function ----------------
def collect_and_save_posts():
    print("Running scheduled job: collect_and_save_posts")
    session = Session()
    posts = get_fake_posts()
    for post in posts:
        new_post = Post(**post)
        session.add(new_post)
    session.commit()
    session.close()

def run_scheduler():
    schedule.every(2).minutes.do(collect_and_save_posts)
    while True:
        schedule.run_pending()
        time.sleep(1)

# ---------------- Dash App Setup ----------------
app = dash.Dash(__name__)
server = app.server  # for deployment

def fetch_posts_df():
    session = Session()
    posts = session.query(Post).all()
    data = [{
        'timestamp': post.timestamp,
        'content': post.content,
        'likes': post.likes,
        'shares': post.shares
    } for post in posts]
    session.close()
    return pd.DataFrame(data)

def generate_graph():
    df = fetch_posts_df()
    if df.empty:
        return html.P("No data available yet.")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)
    df_resampled = df.resample('1T').sum()
    fig = px.line(df_resampled, y=['likes', 'shares'], title='Engagement Over Time')
    return dcc.Graph(figure=fig)

app.layout = html.Div([
    html.H1("Trending Topics Dashboard"),
    generate_graph()
])

# ---------------- Start Scheduler Thread ----------------
scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
scheduler_thread.start()

if __name__ == '__main__':
    app.run(debug=True)


