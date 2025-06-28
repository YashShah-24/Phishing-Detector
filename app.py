import streamlit as st
import re

# ---- Page config ----
st.set_page_config(page_title="PhishGuard", page_icon="🛡️", layout="centered")

# ---- Custom Styles ----
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
        }
        .title {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            color: #2c3e50;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 12px;
            color: #95a5a6;
        }
        .stButton > button {
            background-color: #0066cc;
            color: white;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# ---- Title and Description ----
st.markdown('<div class="title">🛡️ PhishGuard - Phishing URL Detector</div>', unsafe_allow_html=True)
st.markdown("### 🔗 Enter a URL to check if it's suspicious or safe.")
st.info("Note: This is a basic pattern-based detector for educational use only.")

# ---- User Input ----
url = st.text_input("🌐 Website URL")

# ---- Basic Phishing Detector ----
def is_phishing(url):
    if re.search(r"[0-9]{5,}", url):
        return True
    if re.search(r"(login|secure|update|verify)", url, re.IGNORECASE):
        return True
    if "-" in url:
        return True
    if url.count(".") > 3:
        return True
    return False

# ---- Button ----
if st.button("🔍 Check URL"):
    st.markdown("---")
    if is_phishing(url):
        st.error("⚠️ **Warning:** This website looks suspicious and may be a phishing site!")
        st.markdown("🚫 **Advice:** Avoid entering personal information on this site.")
    else:
        st.success("✅ This website looks safe.")
        st.markdown("🛡️ **Great!** No suspicious patterns found.")

# ---- Footer ----
st.markdown('<div class="footer">© 2025 PhishGuard. Built with ❤️ using Streamlit.</div>', unsafe_allow_html=True)