import streamlit as st

# Title of the Biography page
st.title("Biography of John Doe")

# Add some text and subheadings
st.header("About Me")
st.write("""
Hello! My name is **John Doe**, and I am a passionate software developer. I specialize in web development, particularly using Python and Streamlit. I enjoy building web applications that solve real-world problems and help businesses grow.
""")

# Early Life
st.header("Early Life")
st.write("""
I was born and raised in Springfield, a small town where I developed a love for technology at an early age. My interest in computers and programming started when I was 12 years old, and by the time I turned 14, I began learning programming languages like Python and JavaScript.
""")

# Education
st.header("Education")
st.write("""
I earned my degree in **Computer Science** from XYZ University. During my studies, I focused on software development, algorithms, and data structures. I was also involved in various extracurricular activities, including coding competitions and hackathons, which helped me sharpen my skills.
""")

# Career
st.header("Career")
st.write("""
After graduating, I worked as a software developer at **ABC Tech**, where I contributed to several successful projects. Over the years, I have developed expertise in building scalable web applications, both front-end and back-end. I now work as a full-time web developer and enjoy every aspect of creating software.
""")

# Hobbies and Interests
st.header("Hobbies and Interests")
st.write("""
When I am not coding, I enjoy **photography**, **hiking**, and **traveling**. I also love reading about new technologies and experimenting with side projects. In addition, I contribute to **open-source projects** whenever I get the chance!
""")

# Footer (you can also add any contact info here)
st.markdown("---")
st.write("© 2024 John Doe | All rights reserved")
