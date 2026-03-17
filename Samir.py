#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:34:21 2026

@author: fcvmathieu
"""

import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import urllib.parse


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

image = load_image_from_github("pic.png")
if image:
    st.image(image, width=100)
# Title & Player Overview
st.title("Samir Benbrahim - 23 (FR)")
# Button linking to Transfermarkt profile
st.link_button("Transfermarkt Profile", "https://www.transfermarkt.fr/samir-ben-brahim/profil/spieler/1101862")

st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)

# Key Insights
st.header("🔍 Key Insights")
st.markdown(
    """
    **Samir Ben Brahim is a dynamic and creative wide player (Fullback / Winger) with a strong upward trajectory. His ability to destabilize defenses and his continuous progression through levels suggest he is approaching readiness for a higher competitive environment.**
    
    **Personality & mentality** 🧠📈
    - Late developer with strong resilience and progression mindset  
    - Adaptability across levels (N3 → N2 → National)  
    - Offensive initiative and willingness to take responsibility in final third  

    
    **Football Profile** 🎯
    - Dribbling & Carrying: Strong 1v1 ability, capable of eliminating opponents and progressing the ball  
    - Chance Creation: Proven assist potential (high output in previous seasons)  
    - Agility & Mobility: Explosive short-distance movements, low center of gravity  
    - Versatility: Can play winger (right/left), inverted profile or offensive midfielder  

    **Best suited for:** Samir fits teams that seek to create superiority on the wings, both in transition (carry, attack space) and in positional play (isolation 1v1, chance creation from wide areas). ⚡🏹
    """
)

# Define the WhatsApp number (include country code, no '+' sign)
whatsapp_number = "33771730001"  # Example: +33 for France

# Message to send
message = "Hello, I am interested in Freddy Mbemba. Can we discuss further?"

# Encode message for URL
encoded_message = urllib.parse.quote(message)

# WhatsApp URL
whatsapp_url = f"https://api.whatsapp.com/send?phone={whatsapp_number}&text={encoded_message}"

# Button to open WhatsApp chat
if st.button("📲 Contact Sport Director"):
    st.markdown(f'<a href="{whatsapp_url}" target="_blank">Send a whatsapp</a>', unsafe_allow_html=True)


st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)

# Vertical Display with Expanders
with st.expander("👤 Player Career | Young player ready for a new step"):
    image = load_image_from_github("fiche.png")
    if image:
        st.image(image, use_container_width=True)
    st.write(
    """
    **Samir Ben Brahim shows a clear and structured development pathway, characterized by continuous progression and adaptation at each level of the French pyramid. His trajectory is a strong indicator of learning capacity and growth potential.**
    
    **Career & Pathway** 📈
    - Linear progression: Regional → N3 → N2 → National  
    - Each step validated by performance before moving up  
    - No stagnation: constant exposure to higher demands and intensity  
    - Late developer profile, but with accelerated recent growth  

    **Key insights** 🔍
    - Demonstrates strong adaptability to new tactical and physical environments  
    - Learning curve is consistent → suggests high coachability  
    - Progression driven by performance, not by reputation or academy pathway  
    - Profile of a player who builds confidence and impact over time  

    **Projection & next steps** 🚀
    - Short term: Confirm impact at National level (increase G+A, consistency, decision-making in final third)  
    - Optimal next step: Top National club with promotion ambition or Ligue 2 rotation role  
    - Development focus:
        • Increase offensive output (goals + assists)  
        • Improve efficiency in key moments (final pass, finishing)  
        • Maintain ability to create imbalance at higher intensity levels  

    **Ceiling scenario**
    - If progression continues: Ligue 2 starter with creative winger profile  
    - Long-term upside depends on ability to translate volume into decisive actions  

    **Strategic insight**
    - His pathway suggests a “scalable player”: performance rises with level  
    - Key question is no longer adaptation → but impact at higher speed and pressure  
    """
)

with st.expander("📍 Position Played | From winger to fullback"):
    image = load_image_from_github("position.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Samir Ben Brahim demonstrates a high level of positional versatility, with the ability to operate effectively on both flanks and across different lines. He can play as a right or left winger, offering width, 1v1 ability, and creativity in advanced areas, but also as a wing-back or full-back, particularly on the right side, where he combines defensive involvement with forward projection. Overall, his ability to cover both sides and multiple vertical roles makes him a functional and adaptable wide player, capable of fitting different game models and match scenarios.")

with st.expander("⏳ Minutes played | A key player for FC Versailles starting lineups"):
    image = load_image_from_github("minutes_played.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Samir Ben Brahim is a key starter for FC Versailles, consistently selected in the starting XI. He regularly plays high minutes, often close to full matches, showing strong trust from the staff. His availability and consistency highlight his reliability across the season. He is clearly embedded in the team’s tactical structure rather than used as a rotation option. Overall, his minutes profile confirms his importance within the squad.")

with st.expander("🛡 Player Profile | Wide Threat - Progressor & Dribbler"):
    image = load_image_from_github("leaugue_Comparison.png")
    if image:
        st.image(image, use_container_width=True)
    st.write(
    """
    **Samir Ben Brahim profile fits a “Wide Threat – Progressor & Dribbler”, with a strong ability to carry the ball and destabilize defensive structures.**
    
    **Player Profile** ⚡
    - Elite **Dribbling & Carrying** (P90+): constant 1v1 threat, capable of eliminating opponents  
    - High **Dribble & Carry OBV** (P90): creates value through ball progression rather than passing  
    - Strong **Aggressive Actions & Pressures** (P70+): active player, involved in both offensive and defensive duels  
    - Good **xG Assisted** (P68): able to generate chances after progression phases  

    **Interpretation** 🔍
    - Primary strength: **ball progression through carries**, not through passing circuits (low Pass OBV)  
    - Profile of a **line breaker** who advances the team up the pitch and creates imbalance  
    - More impactful in **dynamic situations (transition, space to attack)** than in slow positional play  

    **Role in a team** 🎯
    - Wide winger or wing-back in systems that encourage **1v1 and verticality**  
    - Key asset to **attack disorganized blocks** and generate offensive momentum  
    - Complements more structured playmakers by adding **unpredictability and penetration**  

    **Summary**
    - A high-impact **progressor**, whose value comes from carrying, beating players, and creating danger through movement rather than distribution.
    """
)

with st.expander("⚽ Shot Map | Lack of Efficiency"):
    image = load_image_from_github("Shot_map.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Samir produce high xG value even if the conversation rate is not enought.")

with st.expander("📈 Performance Progression | Individual Development"):
    image = load_image_from_github("progression.png")
    if image:
        st.image(image, use_container_width=True)
    st.write(
    """
    **Samir Ben Brahim shows a clear evolution in his profile, moving from a high-volume, high-intensity winger to a more efficient and specialized progressor.**
    
    **Key progression insights** 📈
    - **Ball carrying impact ↑**: Dribble & Carry OBV jumps (53 → 90), confirming a shift toward a more decisive ball-progressor role  
    - **Efficiency ↑ / Waste ↓**: Turnovers significantly reduced (93 → 6), indicating better decision-making and ball security  
    - **Chance creation slightly ↓**: xG Assisted decreases (78 → 68), suggesting less involvement in final pass but more in earlier progression phases  
    - **Defensive activity ↓ but still solid**: Defensive actions and pressures drop from elite (97 / 94) to strong (70 / 75), likely due to a more offensive positioning  

    **Role transformation** 🔍
    - From a **high-energy, defensive winger** → to a more **offensive, possession-progressor profile**  
    - Less volume, more **quality and impact per action**  
    - Increased responsibility in **advancing the ball and breaking lines**  

    **Interpretation**
    - Samir is evolving toward a **modern wide progressor**, focused on creating advantage through carries rather than defensive intensity or passing  
    - His profile is becoming more **specialized and scalable to higher levels**, where efficiency and decision-making are key  

    **Key question for next step** 🚀
    - Can he **recombine volume + efficiency** to impact games consistently at a higher level (Ligue 2)?  
    """
)

with st.expander("👥 Player Comparison | Timothy Weah (Ligue 1)"):
    image = load_image_from_github("radar.png")
    if image:
        st.image(image, use_container_width=True)
    st.write(
    """
    **Comparison: Samir Ben Brahim vs Timothy Weah highlights two different interpretations of a modern wide player: a pure progressor vs a vertical runner.**
    
    **Common points** ⚖️
    - Both profiles generate value through **ball carrying (Dribble & Carry OBV ~P90)**  
    - Similar ability to **progress the ball and create offensive momentum**  
    - Capable of playing in **wide roles or wing-back systems**  

    **Key differences** 🔍
    - **Samir Ben Brahim**:
        • Elite **dribbling volume (P91)** → strong 1v1 eliminator  
        • Higher **defensive involvement (P70 / P75)** → more complete two-way profile  
        • Lower **pass contribution (Pass OBV P4)** → less involved in circulation  
        • Profile = **creator through imbalance and short-distance progression**
    
    - **Timothy Weah**:
        • Higher **deep progressions & carries volume (P71)** → more vertical runner  
        • Lower **dribbling frequency (P55)** → less 1v1 oriented  
        • More **efficient in structured progression and transitions**  
        • Profile = **explosive runner attacking space and depth**
    
    **Interpretation** 🧠
    - Samir = **ball-dominant winger**, creates advantage through dribbling and tight-space actions  
    - Weah = **off-ball threat**, creates advantage through runs, speed, and verticality  

    **Level gap insight** 📊
    - Despite playing in a lower league, Samir matches or exceeds Weah in:
        • Dribbling impact  
        • Carry value (OBV)  
    - The main gap lies in:
        • Volume at high intensity  
        • Ability to repeat actions in higher-tempo environments (Ligue 1)  

    **Projection** 🚀
    - Samir shows traits of a **Ligue 2 / Ligue 1 rotational winger**, especially in teams needing 1v1 creators  
    - To reach Weah’s level, key step is improving:
        • **off-ball running and depth threat**  
        • **consistency of impact at higher speed**
    """
)


with st.expander("🏋️ Physical Performance | High Intensity & Explosiveness"):
     image = load_image_from_github("physique.png")
     if image:
         st.image(image, use_container_width=True)
     st.write(
        "Samir Ben Brahim shows a strong physical profile aligned with an explosive wide player. "
        "He consistently reaches high maximum speeds (~32–34 km/h), confirming elite sprint capacity with low variability. "
        "His high-speed running (>25 km/h) highlights his ability to repeat intense efforts and impact transitions. "
        "Overall running intensity (m/min) remains stable, reflecting a solid aerobic base and match consistency. "
        "The main area for improvement is increasing the consistency of high-intensity volumes across games to sustain impact at a higher level."
     )

# with st.expander("🤕 Injury History | Robust Player"):
#     image = load_image_from_github("injuries.png")
#     if image:
#         st.image(image, use_container_width=True)
#     st.write("Freddy has maintained excellent availability with no major injuries this season. Freddy is a robust player. He did not get any injury this year that bring 100% of availabity for training and match. He takes care about his body with some session with physio (massage & cares).")

with st.expander("⚖️ Weight Evolution"):
    image = load_image_from_github("poids.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Monitoring body composition is key to performance optimization. He is currently working with a nutritionist")

with st.expander("🔥 Personnality & Motivation | high self determination"):
    image = load_image_from_github("Happiness.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Samir is highly motivated and dedicated to his football journey. His motivation runs deep, rooted in his childhood passion, with a constant desire to progress and reach the highest levels of football.")

with st.expander("📊 Game Report"):
    image = load_image_from_github("game_report.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Example of Game report, please contact Mathieu Feigean for more explanation or request.")






st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)

st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f8f9fa;
            padding: 10px;
            text-align: center;
            font-size: 14px;
            color: #333;
        }
    </style>
    <div class="footer">
        <p><strong>M.Feigean</strong> - Football Development</p>
    </div>
    """, unsafe_allow_html=True)