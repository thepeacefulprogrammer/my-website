import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="PeacefulProgrammer",
    page_icon="✨",
    layout="wide"
)

# Add a title and some text
st.title("PeacefulProgrammer")
st.subheader("Home of the Peaceful Programmer")
st.write("I am a AI Scientist and Software Developer that likes to stream my coding journey live on Twitch and Youtube.")

# Add social media links
st.markdown("---")
st.subheader("Find me online")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("[Twitch](https://twitch.tv/peacefulprogrammer)")
with col2:
    st.markdown("[YouTube](https://youtube.com/@thepeacefulprogrammer)")
with col3:
    st.markdown("[GitHub](https://github.com/thepeacefulprogrammer)")

# About section
st.markdown("---")
st.subheader("About Me")
st.write("""
I focus on AI research and software development, sharing my journey and knowledge with the community through live coding sessions.
My goal is to make complex topics accessible and build a supportive programming community.
""")

# Contact section
st.markdown("---")
st.subheader("Get in Touch")
st.write("Have a question or want to collaborate? Reach out to me on Twitch or Youtube.")

# Footer
st.markdown("---")
st.markdown("© 2025 PeacefulProgrammer. All rights reserved.") 