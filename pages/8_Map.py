###############################################################
# import python libraries
###############################################################
import streamlit as st
import streamlit.components.v1 as components

###############################################################
# page info 
###############################################################

st.set_page_config(
    page_title="Map - Demo class | 2024-03-22 HUMA5630 Digital Humanities",
    page_icon="🌞", 
    layout="wide",
    initial_sidebar_state="expanded", 
)


###############################################################
# code template
###############################################################


'''
# Embed Map
'''

codedemo = '''
components.html("""

    <paste the embed code here>

    """, 
    height=800)
'''

st.code(codedemo, language='python')

###############################################################
# Map 1 using StoryMaps
# https://storymaps.arcgis.com/
###############################################################


'''
# Method 1 - StoryMaps

1. Create and publish your storymap on **https://storymaps.arcgis.com/**
2. Click the 3 dot "More actions"
3. Click "Embed this story" and copy the embed code
'''

st.success("Sample below: https://storymaps.arcgis.com/stories/989d4cb218f94c8a983076e694ad3d25")

components.html("""

    <iframe src="https://storymaps.arcgis.com/stories/989d4cb218f94c8a983076e694ad3d25?cover=false" width="100%" height="1200" frameborder="0" allowfullscreen allow="geolocation"></iframe>

    """, 
    height=1200)

st.markdown("#")
st.markdown("#")

###############################################################
# Map 2 using knightlab's StoryMapJS
# https://storymap.knightlab.com/
###############################################################

'''
# Method 2 - knightlab's StoryMapJS

1. Create and publish your storymap on **https://storymap.knightlab.com/**
2. Click "Share" on the top right-hand corner
3. Copy the embed code
'''

st.success("Sample below: https://uploads.knightlab.com/storymapjs/682a13559f148980898532d0a3bf3427/test/index.html")

st.markdown("#")

mapURL = st.text_input('Your map URL', 'https://uploads.knightlab.com/storymapjs/682a13559f148980898532d0a3bf3427/test/index.html')
if st.button("Re-generate the embed code"):
    st.code(f"<iframe src='{mapURL}' width='100%' height='800' frameborder='0'></iframe>")
else:
    st.code(f"<iframe src='{mapURL}' width='100%' height='800' frameborder='0'></iframe>")


components.html("""

    <iframe src='https://uploads.knightlab.com/storymapjs/682a13559f148980898532d0a3bf3427/test/index.html' width='100%' height='800' frameborder='0'></iframe>

    """, 
    height=1200)
    
