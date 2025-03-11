import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# GitHub repository where images are stored (raw URL format)
GITHUB_BASE_URL = "https://raw.githubusercontent.com/FC-Versailles/player/main/Freddy/"

# Title
st.title("Freddy Mbemba - 22y (FR)")

# Add a horizontal line to separate the header
st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)

st.header("🔍 KEY INSIGHTS")
st.markdown(
    """
    **Freddy Mbemba appears to be an explosive winger or direct attacking forward, based on his statistical radar profile and performance metrics.**

    - **Dribbling & Carrying Ability:** Excellent (P86) 🏃‍♂️💨
    - **Touches in the Box:** Strong involvement in attacking areas (P63) ⚽
    - **Shot Efficiency:** Decent goal conversion (P70) 🎯
    - **Crossing & Playmaking:** Needs improvement (P69) 🎯
    - **Shooting Consistency:** Could improve (P46-P55) 🔄

    **Best suited for:** Transition-based or counter-attacking teams 🏹⚡
    """
)

st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)

# Dictionary of images with titles and comments
images = {
    "👤 Player Career | Young player ready for a new step": ("fiche.png", "Freddy is a young talented forward player, right footed. His career path illustrates the potential and the development of Freddy. In 21/22 he played in 6th division, 22/23 he was transferred to USL Dunkerque in the 3rd Division. 23/24 USL Dunkerque jumped to 2nd division and Freddy was on loan to Nîmes in 3rd division. Freddy is ready to take a new step in his career."),
    "📍 Position played | Left winger & versatile forward": ("position.png", "Freddy is a forward player. His main position is left winger, but he can also play as second striker and right winger."),
    "⏳ Minutes played | A key player - 23/24 starting lineups": ("minutes_played.png", "This season Freddy is a key player for the team. He started in 22/23 lineups and played more than 90% of the available minutes. For the first time in his career, he received two yellow cards, leading to a suspension."),
    "🛡 Player profile | Wide threat - Explosive & Dribbler": ("leaugue_Comparison.png", "Freddy Mbemba is a high-intensity, direct winger with strong dribbling and goal-scoring instincts. His ability to take on defenders and progress the ball makes him an exciting attacking asset, but improving his crossing precision and playmaking could make him a more complete forward. 🚀"),
    "📈 Performance progression | More skills more impact": ("progression.png", "Freddy Mbemba has transitioned into a more effective goal-scorer and playmaker (xG assisted), as seen by his higher xG assisted and goal contribution stats. However, there is a slight trade-off in his dribbling and ball progression, suggesting either a tactical shift (e.g., playing higher up the pitch) or defensive adaptation from opponents."),
    "📊 Player comparison | Ernest Nuamah": ("radar.png", "Advanced radar stats showing strengths and weaknesses."),
    "⚽ Shot map | Top Performance 3.53xG for 6 Goals": ("Shot_map.png", "Freddy is a really efficient forward player."),
    "🏋️ Physical Performance | High intensity & explosiveness": ("physique.png", "**Endurance**: Covers significant distance per game (10,845m), showcasing strong stamina. **Speed**: Reaches a top speed of 32.5 km/h, indicating strong sprint capabilities. In terms of **Intensity:** High acceleration/deceleration numbers (35 accelerations, 38 decelerations per game), proving his ability to make explosive movements and quick changes of direction. **Sprint Efforts**: 27 sprints per game, maintaining a good balance between high-intensity bursts and recovery."),
    "🤕 Injury history": ("injuries.png", "Freddy is a robust player. He did not get any injury this year, ensuring 100% availability for training and matches. He takes care of his body with regular physiotherapy sessions (massage & care)."),
    "⚖️ Weight evolution": ("poids.png", "Monitoring the player's weight and body composition."),
    "😊 Happiness & Determination | Deep intrinsic motivation": ("Happiness.png", "His motivation runs deep, rooted in his childhood passion, with a constant desire to progress and reach the highest levels of football."),
}

# Function to fetch image from GitHub
def load_image_from_github(filename):
    url = GITHUB_BASE_URL + filename
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        st.error(f"⚠️ Could not load image: {filename}")
        return None

# Display images with comments
for title, (filename, comment) in images.items():
    st.subheader(title)
    image = load_image_from_github(filename)
    if image:
        st.image(image, use_container_width=True)
    st.text_area("", comment, height=130)

