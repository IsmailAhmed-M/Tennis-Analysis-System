import streamlit as st
import tempfile
import os
from main import run_pipeline
from database import create_users_table
from auth import login_ui, signup_ui
from report import generate_pdf_report


create_users_table()

# Session state for user login
if 'username' not in st.session_state:
    st.session_state.username = None
if 'page' not in st.session_state:
    st.session_state.page = "login"

# Sidebar Navigation
st.sidebar.title("Navigation")
if st.session_state.username:
    st.sidebar.write(f"Logged in as **{st.session_state.username}**")
    if st.sidebar.button("Logout"):
        st.session_state.username = None
        st.session_state.page = "login"
else:
    st.sidebar.write("Not logged in")

# Main App Routing
if st.session_state.page == "login":
    st.title("🎾 Tennis Analysis System")

    tab1, tab2 = st.tabs(["Login", "Signup"])

    with tab1:
        user = login_ui()
        if user:
            st.session_state.username = user
            st.session_state.page = "home"
            st.rerun()

    with tab2:
        signup_ui()

elif st.session_state.page == "home":
    st.title("Welcome to the Tennis Analysis System! 🎾")


# File uploader
    uploaded_file = st.file_uploader("Upload a Tennis Video", type=["mp4", "avi", "mov"])

    if uploaded_file is not None:
        # Save uploaded video to a temporary file
        temp_input = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
        temp_input.write(uploaded_file.read())
        temp_input.close()

        st.video(temp_input.name)


        if st.button("🎥 Analyze Video "):
            st.write("⏳ Processing your video, this may take a few minutes...")

        # Run your full pipeline here
        output_path  = run_pipeline(temp_input.name)

        st.success("✅ Video analysis completed!")

        # Show output video
    
        # Option to download
        with open(output_path, "rb") as f:
            st.download_button("📥 Download Result Video", f, file_name="analyzed_tennis_video.mp4")

        if st.button("📄 Generate PDF Report"):
            pdf_path = generate_pdf_report(st.session_state.username)

            st.success("✅ PDF report has been successfully generated!")
            with open(pdf_path, "rb") as f:
                st.download_button("📥 Download PDF Report", f, file_name="tennis_report.pdf")