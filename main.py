import streamlit as st
import pandas as pd
from pathlib import Path
import smtplib
from email.message import EmailMessage

smtp_server = 'smtp.gmail.com'
port = 465
sender_email = st.secrets["EMAIL_ADDRESS"]
password = st.secrets["EMAIL_PASSWORD"]

certificate_path = Path('certificate')

st.sidebar.title('Navigation')
section = st.sidebar.radio('Go to', ['About', 'Experience', 'Skills', 'Education', 'Certificates', 'Projects','Contact'])

skills = {
    'Python': 0.8,
    'Django': 0.5,
    'Streamlit': 0.9,
    'UI/UX': 0.9,
    'Figma': 0.9,
    'Html': 0.7,
    'Css': 0.8
}

col1, col2 = st.columns(2)

with col1:
    st.image('My_pic.JPG',  width=250)

with col2:
    st.title('Amir Mahdi Goodarzi')
    st.subheader('Programmer and UI / UX Designer')

    with st.container():
        st.markdown("""
        <div style='display:flex; gap: 15px;'>
            <a href='https://github.com/Rexlep' target='_blank'>
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 2C10.6868 2 9.38642 2.25866 8.17317 2.7612C6.95991 3.26375 5.85752 4.00035 4.92893 4.92893C3.05357 6.8043 2 9.34784 2 12C2 16.42 4.87 20.17 8.84 21.5C9.34 21.58 9.5 21.27 9.5 21V19.31C6.73 19.91 6.14 17.97 6.14 17.97C5.68 16.81 5.03 16.5 5.03 16.5C4.12 15.88 5.1 15.9 5.1 15.9C6.1 15.97 6.63 16.93 6.63 16.93C7.5 18.45 8.97 18 9.54 17.76C9.63 17.11 9.89 16.67 10.17 16.42C7.95 16.17 5.62 15.31 5.62 11.5C5.62 10.39 6 9.5 6.65 8.79C6.55 8.54 6.2 7.5 6.75 6.15C6.75 6.15 7.59 5.88 9.5 7.17C10.29 6.95 11.15 6.84 12 6.84C12.85 6.84 13.71 6.95 14.5 7.17C16.41 5.88 17.25 6.15 17.25 6.15C17.8 7.5 17.45 8.54 17.35 8.79C18 9.5 18.38 10.39 18.38 11.5C18.38 15.32 16.04 16.16 13.81 16.41C14.17 16.72 14.5 17.33 14.5 18.26V21C14.5 21.27 14.66 21.59 15.17 21.5C19.14 20.16 22 16.42 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7362 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2Z" fill="#595858"/>
                </svg>
            </a>
            <a href='https://www.linkedin.com/in/amir-gudarzi/' target='_blank'>
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M19 3C19.5304 3 20.0391 3.21071 20.4142 3.58579C20.7893 3.96086 21 4.46957 21 5V19C21 19.5304 20.7893 20.0391 20.4142 20.4142C20.0391 20.7893 19.5304 21 19 21H5C4.46957 21 3.96086 20.7893 3.58579 20.4142C3.21071 20.0391 3 19.5304 3 19V5C3 4.46957 3.21071 3.96086 3.58579 3.58579C3.96086 3.21071 4.46957 3 5 3H19ZM18.5 18.5V13.2C18.5 12.3354 18.1565 11.5062 17.5452 10.8948C16.9338 10.2835 16.1046 9.94 15.24 9.94C14.39 9.94 13.4 10.46 12.92 11.24V10.13H10.13V18.5H12.92V13.57C12.92 12.8 13.54 12.17 14.31 12.17C14.6813 12.17 15.0374 12.3175 15.2999 12.5801C15.5625 12.8426 15.71 13.1987 15.71 13.57V18.5H18.5ZM6.88 8.56C7.32556 8.56 7.75288 8.383 8.06794 8.06794C8.383 7.75288 8.56 7.32556 8.56 6.88C8.56 5.95 7.81 5.19 6.88 5.19C6.43178 5.19 6.00193 5.36805 5.68499 5.68499C5.36805 6.00193 5.19 6.43178 5.19 6.88C5.19 7.81 5.95 8.56 6.88 8.56ZM8.27 18.5V10.13H5.5V18.5H8.27Z" fill="#595858"/>
                </svg>
            </a>
        </div>
        """, unsafe_allow_html=True)

# About Section
if section == 'About':
    st.divider()
    st.markdown(f"""
    I'm a UI/UX designer and software developer with a strong focus on building practical, user-centered digital products. My background combines professional interface design with hands-on experience in developing automation systems, Python applications, and Django-based backends.

    Throughout my work, I’ve created multiple real-world projects, including custom desktop applications with CustomTkinter, data-driven tools, and full automation pipelines. I also have experience developing structured dashboards, workflow systems, and smart utilities designed to help businesses improve efficiency.
    
    Currently, I’m working on a fully professional automation platform, aiming to integrate clean design with robust backend engineering.
    
    In addition to development, I’m an active instructor. Over the past years, I’ve taught more than 1,000 students, helping them learn Python, UI/UX fundamentals, and real-world software development techniques. My teaching style is practical, direct, and focused on building real skills — not just theory.
    
    My goal is to continue bridging design and engineering by creating products that are both beautiful and powerful, while mentoring the next generation of developers and designers.
    """)


# Experience Section
elif section == 'Experience':
    st.header('Work Experience')

    with st.expander(f'Teaching | Top learn | December 2024'):
        st.write(f"""
        - Build 2 courses related to Figma & UI /UX.
        - Gain over 400 students in this platform.
        - Figma course with over ninety videos and thirty hours of duration
        """)
        st.markdown("""
        <a href='https://toplearn.com/c/6239' target='_blank'>Flex-box training by designing from a Figma file</a>\n
        <a href='https://toplearn.com/c/6251' target='_blank'>Comprehensive Figma Training Course: From Absolute Zero to Entering the Design Job Market</a>
        """, unsafe_allow_html=True)

    with st.expander(f'Teaching | Maktabkhooneh | Jan 2025'):
        st.write(f"""
        - Created 2 Programming course.
        - Gain more than 500 students.
        - Python course with over 150 videos and more than thirty hours of duration.
        """)
        st.markdown("""
        <a href='https://maktabkhooneh.org/course/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-pandas-%D9%85%D9%82%D8%AF%D9%85%D8%A7%D8%AA%DB%8C-mk12171/?v=1' target='_blank'>Basic Pandas Tutorial</a>\n
        <a href='https://maktabkhooneh.org/course/%D8%B7%D8%B1%D8%A7%D8%AD%DB%8C-%D8%B1%D8%A7%D8%A8%D8%B7-%DA%A9%D8%A7%D8%B1%D8%A8%D8%B1%DB%8C-%D9%85%D8%AF%D8%B1%D9%86-%D8%B2%D8%A8%D8%A7%D9%86-python-mk11957/?v=1' target='_blank'>Learning to design modern user interfaces with Python</a>\n
        <a href='https://maktabkhooneh.org/course/%D8%B7%D8%B1%D8%A7%D8%AD%DB%8C-%D8%B1%D8%A7%D8%A8%D8%B7-%DA%A9%D8%A7%D8%B1%D8%A8%D8%B1%DB%8C-%D9%85%D8%AF%D8%B1%D9%86-%D8%B2%D8%A8%D8%A7%D9%86-python-mk11957/?v=1' target='_blank'>Master class python 2026</a>
        """, unsafe_allow_html=True)

    with st.expander(f'Intern | Raman Learn | March 2023'):
        st.write(f"""
        - Worked as an Intern in Raman Learn for around 1 year in UI / UX here is some of the projects
        """)


# Skills section
elif section == 'Skills':
    st.header('Skills Overview')
    for skill, level in skills.items():
        st.write(f'{skill}  {level * 100} %')
        st.progress(level)
    df_skills = pd.DataFrame({
        'Skill': list(skills.keys()),
         'Proficiency': list(skills.values())
    })

    st.divider()

    st.bar_chart(df_skills.set_index('Skill'))


# Education section
elif section == 'Education':
    st.header('Education Experience')
    st.write('“High school diploma in Industrial Electricity with a final GPA of 18.”')
    st.write('"Admitted to Shahid Mohsen Mohajer University with a national rank of 90 in the Electrotechnics program"')


# Degree section
elif section == 'Certificates':

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.write('Python')
        st.image(f'{certificate_path}/python.png', width=350)

        st.divider()

        st.write('Introduce to ai')
        st.image(f'{certificate_path}/ai.png', width=350)

    with col2:
        st.write('Html')
        st.image(f'{certificate_path}/html.jpg', width=350)

        st.divider()

        st.write('UI/UX')
        st.image(f'{certificate_path}/uiux.jpg', width=350)


# Projects section
elif section == 'Projects':
    col1,col2 = st.columns(2)


# Contact section
elif section == 'Contact':
    st.header('Get in touch')

    col1,  col2 = st.columns(2)

    with col1:
        email = st.text_input('email')
        phone = st.text_input('phone')


    with col2:
        linkedin = st.text_input('Linkedin url')
        discord = st.text_input('Discord')

    message = st.text_area('message')

    if st.button('Send'):
        st.success("Thanks for reaching out, i'll be in contact soon")

        msg = EmailMessage()
        msg['subject'] = 'Contact from website'

        msg['From'] = sender_email
        msg['To'] = 'amirmahdi.gdrzi12@gmail.com'

        msg.add_alternative(f"""
            <h1>Hello from {email}</h1>
            <p><b>Phone:</b> {phone}</p>
            <p>{message}</p>
        """, subtype="html")

        with smtplib.SMTP_SSL(smtp_server, port) as server:
            server.login(sender_email, password)
            server.send_message(msg)