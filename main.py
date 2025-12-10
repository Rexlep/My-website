import streamlit as st
import pandas as pd
from pathlib import Path
import smtplib
from email.message import EmailMessage

# ========== CONFIG ==========
st.set_page_config(page_title="Amir Mahdi Goodarzi", page_icon="✨", layout="wide")

smtp_server = 'smtp.gmail.com'
port = 465
sender_email = st.secrets["EMAIL_ADDRESS"]
password = st.secrets["EMAIL_PASSWORD"]

certificate_path = Path("certificate")

# Sidebar
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", [
    "About", "Experience", "Skills", "Education", "Certificates", "Projects", "Contact"
])

# Skills Data
skills = {
    "Python": 0.8,
    "Django": 0.5,
    "Streamlit": 0.9,
    "UI/UX": 0.9,
    "Figma": 0.9,
    "HTML": 0.7,
    "CSS": 0.8
}

# ========== HEADER ==========
col1, col2 = st.columns([1, 2])

with col1:
    st.image("My_pic.JPG", width=230)

with col2:
    st.title("Amir Mahdi Goodarzi")
    st.write("Programmer • UI/UX Designer • Automation Developer")

    st.markdown("""
    <div style='display:flex; gap:20px; margin-top: 10px;'>
        <a href='https://github.com/Rexlep' target='_blank'>GitHub</a>
        <a href='https://www.linkedin.com/in/amir-gudarzi/' target='_blank'>LinkedIn</a>
    </div>
    """, unsafe_allow_html=True)

# ========== ABOUT ==========
if section == "About":
    st.header("About Me")
    st.write("""
    I'm a UI/UX designer and software developer...
    """)

# ========== EXPERIENCE ==========
elif section == "Experience":
    st.header("Work Experience")
    with st.expander("Teaching | Top Learn | 2024"):
        st.write("""
        - Built 2 courses...
        """)

# ========== SKILLS ==========
elif section == "Skills":
    st.header("Skills Overview")

    for skill, value in skills.items():
        st.write(f"**{skill} — {int(value*100)}%**")
        st.progress(value)

    df = pd.DataFrame({"Skill": list(skills.keys()), "Level": list(skills.values())})
    st.bar_chart(df.set_index("Skill"))

# ========== EDUCATION ==========
elif section == "Education":
    st.header("Education")
    st.write("""
    - High school diploma...
    """)

# ========== CERTIFICATES ==========
elif section == "Certificates":
    st.header("Certificates")

    col1, col2 = st.columns(2)

    with col1:
        st.image(certificate_path / "python.png", width=350)
        st.image(certificate_path / "ai.png", width=350)

    with col2:
        st.image(certificate_path / "html.jpg", width=350)
        st.image(certificate_path / "uiux.jpg", width=350)

# ========== CONTACT ==========
elif section == "Contact":
    st.header("Contact Me")

    col1, col2 = st.columns(2)

    with col1:
        email = st.text_input("Your Email")
        phone = st.text_input("Phone Number")

    with col2:
        linkedin = st.text_input("LinkedIn URL")
        discord = st.text_input("Discord")

    message = st.text_area("Message")

    if st.button("Send Message"):
        msg = EmailMessage()
        msg["Subject"] = "New Contact Form Submission"
        msg["From"] = sender_email
        msg["To"] = "amirmahdi.gdrzi@gmail.com"

        # HTML Email
        msg.add_alternative(f"""
        <html>
        <body>
            <h2>New Message from {email}</h2>
            <p><strong>Phone:</strong> {phone}</p>
            <p><strong>Message:</strong><br>{message}</p>
        </body>
        </html>
        """, subtype="html")

        with smtplib.SMTP_SSL(smtp_server, port) as server:
            server.login(sender_email, password)
            server.send_message(msg)

        st.success("Message sent successfully!")
