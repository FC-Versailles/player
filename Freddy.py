#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 11:19:33 2025

@author: fcvmathieu
"""

import streamlit as st
from PIL import Image

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
    "👤 Player Career | Young player ready for a new step": ("/Users/fcvmathieu/Desktop/Freddy/fiche.png","Freddy is a young talented forward player, right footed. His career path illustrate the potential and the development of Freddy. In 21/22 he played in 6th division, 22/23 he was transfered in USL Dunkerque in the 3rd Division. 23/24 USL Dunkerque jump in 2nd division and Freddy was in loan to Nimes in 3rd division. Freddy is ready to take a new step in his career"),
    "📍 Position played | Left winger & versatile forward": ("/Users/fcvmathieu/Desktop/Freddy/position.png", "Freddy is a forward player. His main position is left winger, he is able to play as second striker and right winger."),
    "⏳ Minutes played | A key player - 23/24 starting lineups": ("/Users/fcvmathieu/Desktop/Freddy/minutes_played.png", "This season Freddy is a key player for the team. Freddy took 22/23 lineups and more than 90% of the available minutes. For the first time of his career he took 2 yellows cards that bring to a missing match."),
    
    "🛡 Player profile | Wide threat - Explosive & Dribbler": ("/Users/fcvmathieu/Desktop/Freddy/leaugue_Comparison.png", " Freddy Mbemba is a high-intensity, direct winger with strong dribbling and goal-scoring instincts. His ability to take on defenders and progress the ball makes him an exciting attacking asset, but improving his crossing precision and playmaking could make him a more complete forward. 🚀"),
    "📈 Performance progression | More skills more impact": ("/Users/fcvmathieu/Desktop/Freddy/progression.png", "Freddy Mbemba has transitioned into a more effective goal-scorer and playmaker (xG assisted), as seen by his higher xG assisted and goal contribution stats. However, there is a slight trade-off in his dribbling and ball progression, suggesting either a tactical shift (e.g., playing higher up the pitch) or defensive adaptation from opponents."),
    "📊 Player comparision | Ernest Nuamah": ("/Users/fcvmathieu/Desktop/Freddy/radar.png", "Advanced radar stats showing strengths and weaknesses."),
    "⚽ Shot map | Top Performance 3.53xG for 6 Goals": ("/Users/fcvmathieu/Desktop/Freddy/Shot_map.png", "Freddy is a really efficient forward player."),
    " Physical Performance | High intensity & explosivness": ("/Users/fcvmathieu/Desktop/Freddy/physique.png", "**Endurance**: Covers significant distance per game (10,845m), showcasing strong stamina. **Speed**: Reaches a top speed of 32.5 km/h, indicating strong sprint capabilities. In term of **Intensity:** High acceleration/deceleration numbers (35 accelerations, 38 decelerations per game), proving his ability to make explosive movements and quick changes of direction. **Sprint Efforts**: 27 sprints per game, maintaining a good balance between high-intensity bursts and recovery. "),
    
    "🤕 Injury history": ("/Users/fcvmathieu/Desktop/Freddy/injuries.png", "Freddy is a robust player. He did not get any injury this year that bring 100% of availabity for training and match. He takes care about his body with some session with physio (massage & cares)"),
    "⚖️ Weight evolution": ("/Users/fcvmathieu/Desktop/Freddy/poids.png", "Monitoring the player's weight and body composition."),
    "😊 Happiness & Determination | Deep intrinsic motivation": ("/Users/fcvmathieu/Desktop/Freddy/Happiness.png", "His motivation runs deep, rooted in his childhood passion, with a constant desire to progress and reach the highest levels of football."),


}


# Display images with comments
for title, (path, comment) in images.items():
    st.subheader(title)
    image = Image.open(path)
    st.image(image, use_container_width=True)
    st.text_area("", comment, height=130)

