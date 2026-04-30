from flask import Flask, render_template

app = Flask(__name__)

# --- DATABASE (Unlimited Data Center) ---
# Yahan aap jitni chahe movies/series add kar sakte hain.
# Bas link, title aur category badalni hai.
content_database = [
    # --- NEW MOVIES ---
    {"id": "MWOshaxS6ig", "title": "जवान (Jawan)", "img": "https://image.tmdb.org/t/p/w500/jY9p69Cbt58E5I9K7S9p8u9Q3Gv.jpg", "cat": "movies"},
    {"id": "vqu4z34wENw", "title": "पठान (Pathaan)", "img": "https://image.tmdb.org/t/p/w500/m1By70o9p0X0S8pD9FvwwN9Z99W.jpg", "cat": "movies"},
    {"id": "Yo38v27C4v4", "title": "RRR (Hindi)", "img": "https://image.tmdb.org/t/p/w500/u90CcI80v63Z8p66pI6NAtS69sX.jpg", "cat": "movies"},
    {"id": "COv527zjd_0", "title": "Animal (Hindi)", "img": "https://image.tmdb.org/t/p/w500/hrm9j9atghm690osvghj9atghm6.jpg", "cat": "movies"},

    # --- WEB SERIES ---
    {"id": "ZNeGF-830_I", "title": "मिर्जापुर (Mirzapur)", "img": "https://image.tmdb.org/t/p/w500/7o9X83u8u7Z9u7u7Z9u7u7Z9u7u.jpg", "cat": "series"},
    {"id": "Exm_Y9Vf0XU", "title": "पंचायत (Panchayat)", "img": "https://image.tmdb.org/t/p/w500/6LpX8yS0S8pD9FvwwN9Z99W.jpg", "cat": "series"},
    {"id": "Z99_L0jG_l8", "title": "फर्जी (Farzi)", "img": "https://image.tmdb.org/t/p/w500/6LpX8yS0S8pD9FvwwN9Z99W.jpg", "cat": "series"},

    # --- OLD IS GOLD ---
    {"id": "r6L_E8P-jMA", "title": "शोले (Sholay)", "img": "https://m.media-amazon.com/images/M/MV5BNTgwYmYyMmItYmI5Mi00NGE0LWE1OTctMzE0YzUxNGE1NzFlXkEyXkFqcGdeQXVyNjN0MTgzMzU@._V1_FMjpg_UX1000_.jpg", "cat": "old"},
    {"id": "9bZkp7q19f0", "title": "मुगल-ए-आजम", "img": "https://m.media-amazon.com/images/M/MV5BMjA4OTg2MDEyNF5BMl5BanBnXkFtZTgwMzY2Mjc4OTE@._V1_.jpg", "cat": "old"}
]

@app.route('/')
def home():
    # Filter content by category to send to HTML
    movies = [i for i in content_database if i['cat'] == 'movies']
    series = [i for i in content_database if i['cat'] == 'series']
    old_gold = [i for i in content_database if i['cat'] == 'old']
    
    return render_template('index.html', 
                           movies=movies, 
                           series=series, 
                           old_gold=old_gold)

if __name__ == '__main__':
    app.run(debug=True)
