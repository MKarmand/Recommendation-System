import streamlit as st
import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- Judul Aplikasi ---
st.title("🎌 Anime Recommendation System")

# --- Lihat File yang Tersedia di Direktori ---
st.subheader("📂 File tersedia:")
st.write(os.listdir())  # Debug: Melihat file yang tersedia

# --- Fungsi Load Data dengan Cache ---
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

# --- Fungsi Bangun Matriks Similaritas ---
@st.cache_resource
def build_similarity_matrix(genres):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(genres.fillna(''))  # Tangani NaN
    return cosine_similarity(tfidf_matrix, tfidf_matrix)

# --- Muat Data ---
try:
    df = load_data()
    st.write("✅ Data berhasil dimuat:")
    st.dataframe(df.head())
    cosine_sim = build_similarity_matrix(df['Genres'])
except Exception as e:
    st.error(f"❌ Gagal memuat data: {e}")
    st.stop()

# --- Fungsi Rekomendasi ---
def get_recommendations(title, top_n=5):
    indices = pd.Series(df.index, index=df['Title']).drop_duplicates()
    if title not in indices:
        return pd.DataFrame()
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    anime_indices = [i[0] for i in sim_scores]
    return df.iloc[anime_indices][['Title', 'Genres', 'Score']]

# --- UI Rekomendasi ---
st.subheader("🔍 Cari Rekomendasi Anime")

anime_list = sorted(df['Title'].dropna().unique())
selected_anime = st.selectbox("Pilih Anime", anime_list)
top_k = st.slider("Jumlah Rekomendasi", min_value=1, max_value=20, value=5)

if st.button("Lihat Rekomendasi"):
    results = get_recommendations(selected_anime, top_n=top_k)
    if results.empty:
        st.warning("⚠️ Anime tidak ditemukan atau tidak ada rekomendasi.")
    else:
        st.success(f"🎯 Rekomendasi untuk: {selected_anime}")
        for _, row in results.iterrows():
            st.markdown(f"""
            **🎬 {row['Title']}**  
            🎭 *Genre:* {row['Genres']}  
            ⭐ *Score:* {row['Score']}
            ---
            """)
