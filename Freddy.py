import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# GitHub repository where images are stored (raw URL format)
GITHUB_BASE_URL = "https://raw.githubusercontent.com/FC-Versailles/player/main/"

# Function to fetch images from GitHub
def load_image_from_github(filename):
    url = GITHUB_BASE_URL + filename
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        st.error(f"⚠️ Could not load image: {filename}")
        return None

# Title & Player Overview
st.title("Freddy Mbemba - 22y (FR)")
st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)

# Key Insights
st.header("🔍 Key Insights")
st.markdown(
    """
    **Freddy Mbemba is an explosive winger or direct attacking forward, based on his statistical profile.**
    
    - **Dribbling & Carrying:** Excellent (P86) 🏃‍♂️💨
    - **Touches in the Box:** Strong involvement (P63) ⚽
    - **Shot Efficiency:** Decent conversion (P70) 🎯
    - **Crossing & Playmaking:** Needs improvement (P69) 🎯
    - **Shooting Consistency:** Could improve (P46-P55) 🔄
    
    **Best suited for:** Transition-based or counter-attacking teams 🏹⚡
    """
)
st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)

# Vertical Display with Expanders
with st.expander("👤 Player Career | Young player ready for a new step"):
    image = load_image_from_github("fiche.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Freddy has progressed rapidly through divisions, demonstrating strong development potential.")

with st.expander("📈 Performance Progression"):
    image = load_image_from_github("progression.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Freddy's xG-assisted and goal contributions show his growth as an attacking force.")

with st.expander("📊 Player Comparison | Ernest Nuamah"):
    image = load_image_from_github("radar.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Advanced radar stats highlighting Freddy's strengths and areas for improvement.")

with st.expander("⚽ Shot Map | Efficiency"):
    image = load_image_from_github("Shot_map.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Freddy is an efficient goal scorer with a strong xG conversion rate.")

with st.expander("📍 Position Played | Left Winger & Versatile Forward"):
    image = load_image_from_github("position.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Freddy primarily plays as a left winger but is also comfortable as a second striker or right winger.")

with st.expander("🛡 Player Profile | Wide Threat - Explosive & Dribbler"):
    image = load_image_from_github("leaugue_Comparison.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Freddy excels in high-intensity attacking scenarios, with great dribbling skills and goal instincts.")

with st.expander("🏋️ Physical Performance | High Intensity & Explosiveness"):
    image = load_image_from_github("physique.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Freddy covers significant distance per game (10,845m) and reaches a top speed of 32.5 km/h.")

with st.expander("🤕 Injury History"):
    image = load_image_from_github("injuries.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Freddy has maintained excellent availability with no major injuries this season.")

with st.expander("⚖️ Weight Evolution"):
    image = load_image_from_github("poids.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Monitoring body composition is key to performance optimization.")

with st.expander("😊 Happiness & Determination"):
    image = load_image_from_github("Happiness.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Freddy is highly motivated and dedicated to his football journey.")

st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)
st.success("✅ Updated player profile with structured insights and better mobile-friendly display!")
