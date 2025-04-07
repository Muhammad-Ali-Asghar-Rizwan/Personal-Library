import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Page Configuration ---
st.set_page_config(page_title="📚 Personal Library Manager", layout="centered")

# --- Custom CSS Styling ---
st.markdown("""
    <style>
        .main {
            background-color: #f4f4f4;
            padding: 20px;
            border-radius: 12px;
        }
        .reportview-container .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        h1, h2 {
            text-align: center;
            color: #2c3e50;
        }
        .stButton>button {
            background-color: #2ecc71;
            color: white;
            border-radius: 8px;
            padding: 0.5em 2em;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("📚 Personal Library Manager")

# --- Initialize Session State ---
if "books" not in st.session_state:
    st.session_state.books = []

# --- Book Entry Section ---
st.header("➕ Add a New Book")
with st.form("book_form"):
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input("Book Title")
        author = st.text_input("Author")
    with col2:
        pages = st.number_input("Total Pages", min_value=1, value=100)
        pages_read = st.number_input("Pages Read", min_value=0, max_value=pages, value=0)

    submitted = st.form_submit_button("Add Book")
    if submitted and title and author:
        st.session_state.books.append({
            "Title": title.strip(),
            "Author": author.strip(),
            "Pages": pages,
            "Pages Read": pages_read
        })
        st.success(f"📘 '{title}' by {author} added to your library!")

# --- Display Book List ---
if st.session_state.books:
    st.header("📚 Your Library")
    df = pd.DataFrame(st.session_state.books)
    st.dataframe(df, use_container_width=True)

    # --- Visual Stats ---
    st.header("📊 Reading Statistics")

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(df["Title"], df["Pages"], label="Total Pages", color="#2980b9")
    ax.bar(df["Title"], df["Pages Read"], label="Pages Read", color="#27ae60")
    ax.set_ylabel("Pages")
    ax.set_xlabel("Books")
    ax.set_title("Reading Progress")
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    st.pyplot(fig)
else:
    st.info("No books added yet. Use the form above to add one!")

# --- Footer ---
st.markdown("""
<hr>
<p style='text-align:center;'>Made with ❤️ by Ali Asghar | Powered by GIAIC</p>
""", unsafe_allow_html=True)
