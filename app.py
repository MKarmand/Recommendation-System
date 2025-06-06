import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- Load dan Persiapkan Data ---
@st.cache_data
def load_data():
    df = pd.read_csv('data.csv')
    df['Genres'] = df['Genres'].fillna('')
    return df

@st.cache_resource
def build_similarity_matrix(df):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['Genres'])
    return cosine_similarity(tfidf_matrix, tfidf_matrix)

df = load_data()
cosine_sim = build_similarity_matrix(df)

# --- Fungsi Rekomendasi ---
def get_recommendations(title, cosine_sim=cosine_sim, df=df, top_n=5):
    indices = pd.Series(df.index, index=df['Title']).drop_duplicates()
    if title not in indices:
        return []
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    anime_indices = [i[0] for i in sim_scores]
    return df.iloc[anime_indices][['Title', 'Genres', 'Score']]

# --- UI Streamlit ---
st.title("🎌 Sistem Rekomendasi Anime")

anime_list = sorted(df['Title'].dropna().unique())
selected_anime = st.selectbox("Pilih Anime", anime_list)

top_k = st.slider("Jumlah Rekomendasi", min_value=1, max_value=20, value=5)

if st.button("Lihat Rekomendasi"):
    result = get_recommendations(selected_anime, top_n=top_k)
    if result.empty:
        st.warning("Anime tidak ditemukan atau tidak ada rekomendasi.")
    else:
        st.subheader(f"Rekomendasi untuk: {selected_anime}")
        for idx, row in result.iterrows():
            st.markdown(f"**🎬 {row['Title']}**  \n🎭 *Genre:* {row['Genres']}  \n⭐ *Score:* {row['Score']}")
            st.markdown("---")
