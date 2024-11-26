import streamlit as st

# Title of the Biography page
st.title("Biography of John Luis Hernandez")

# Add an image as a circle using HTML and CSS
st.markdown("""
    <style>
        .circle-img {
            border-radius: 50%;
            width: 200px;
            height: 200px;
            object-fit: cover;
        }
    </style>
    <img src="https://scontent.fcgy2-2.fna.fbcdn.net/v/t39.30808-1/466729063_1315875869574868_5258799122525142086_n.jpg?stp=dst-jpg_s200x200&_nc_cat=101&ccb=1-7&_nc_sid=50d2ac&_nc_eui2=AeHgHAq4IfUQC7mQl2nceAQ7bndqOX6-4BBud2o5fr7gEPYgHepfPusRoyra32rfG1PioTOPMUyMlbbTyz1UFFRi&_nc_ohc=Gs9D8fk99XcQ7kNvgE12Bk9&_nc_zt=24&_nc_ht=scontent.fcgy2-2.fna&_nc_gid=AErGhae3C_KRvSL_bHgB_DT&oh=00_AYDPytbLBgBYCV_RJmdB1TsPddOKvJsijm5Jz6zT4Jqglw&oe=674B301E" class="circle-img">
""", unsafe_allow_html=True)

# About Me Section
st.header("About Me")
st.write("""
Hello! My name is **John Luis J. Hernandez**, and I am 18 years old. I live in Brgy. Hayanggabon, Claver, Surigao Del Norte. I have a variety of interests, including **dancing**, **nature trips**, and **online gaming**. I enjoy exploring new places, experiencing nature, and of course, gaming in my free time.
""")

# Early Life
st.header("Early Life")
st.write("""
I was born in Fairview, Quezon City, and raised in Brgy. Hayanggabon, Claver, Surigao Del Norte, a small town where I developed a passion for dancing and playing online games at an early age. My interest in these activities began when I was 12, and by age 14, I started exploring nature trips to add variety to my hobbies and enjoy the outdoors.
""")

# Education
st.header("Education")
st.write("""
I graduated from **Taganito National High School**. High school was a transformative period where I honed my interests and faced new academic challenges. I realized that education is about more than just memorization; it’s about applying knowledge to real-world situations.
""")

# Career
st.header("Career")
st.write("""
After high school, I decided to pursue my passion for technology and enrolled at **Surigao del Norte State University (SNSU)**. I’m currently working towards a degree in **Computer Engineering**, with hopes of making meaningful contributions to the tech field.
""")

# Hobbies and Interests
st.header("Hobbies and Interests")
st.write("""
When I'm not dancing or gaming, you can find me:
- **Watching movies** and documentaries
- Going on **nature trips** to explore the beauty of the outdoors
- **Traveling** to new destinations to experience different cultures

Spending quality time with my family is also very important to me.
""")

# Contact Information
st.header("Contact Information")
st.write("Feel free to get in touch:")
st.write("📞 **Contact Number**: +63 9706858504")  # Replace with your actual contact number
st.write("📧 **Email**: [johnluishernandez925@gmail.com](mailto:johnluishernandez925@gmail.com)")  # Replace with your Gmail

# Footer
st.markdown("---")
st.write("© 2024 John Luis J. Hernandez | All rights reserved")
