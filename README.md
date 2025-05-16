
# 🎬 Movie Recommendation System

This is a **content-based movie recommender system** built using machine learning and natural language processing techniques. It suggests top 5 similar movies based on a selected movie title. The application is deployed using **Streamlit** and available at:

👉 [Live App on Render](https://movie-recommend-1-i8ew.onrender.com/)

---

## 📂 Dataset

Two datasets from TMDb are used:

1. `tmdb_5000_movies.csv`
2. `tmdb_5000_credits.csv`

The datasets were merged on the `title` column and cleaned as part of the preprocessing pipeline.

---

## 🛠️ Feature Engineering

Key preprocessing steps include:

- Merging movie and credit datasets
- Removing duplicates
- Parsing `genres`, `keywords`, `cast`, and `crew` columns (JSON-like strings)
- Extracting:
  - Only the **genre names**
  - Top **3 cast members**
  - Only the **director** from crew
- Removing extra spaces
- Creating a new column `tags` combining overview, genres, keywords, cast, and crew
- Converting text to lowercase
- Applying **CountVectorizer**
- Performing **Porter Stemming**

---

## 📊 Recommendation Logic

- Calculated cosine similarity between movies using CountVectorized and stemmed `tags`.
- Stored similarity matrix as `similarity.pkl`.
- Movie titles stored in `movies_dict.pkl`.
- A recommendation function returns **top 5 most similar movies**.

---

## 🖼️ Movie Poster Retrieval

Movie posters are fetched dynamically using the [TMDb API](https://www.themoviedb.org/documentation/api). A sample function used:

```python
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    return "https://image.tmdb.org/t/p/w500/" + poster_path
```

> Note: This uses an API call, not web scraping.

---

## 🚀 Deployment

- Built the frontend using **Streamlit**
- Deployed on **Render**

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
pip install -r requirements.txt
streamlit run app.py
```

---

## 📚 Libraries Used

- pandas
- numpy
- sklearn
- nltk
- requests
- streamlit
- pickle

---

## 💡 Project Highlights

- Combines multiple feature extraction techniques.
- Demonstrates end-to-end pipeline: preprocessing → modeling → deployment.
- Real-time movie poster retrieval via API.
- Clean and intuitive UI for users.
