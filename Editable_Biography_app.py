import streamlit as st

# Title of the Biography page
st.title("Biography of John Luis Hernandez")

# Add an image
st.image("https://www.facebook.com/photo?fbid=1315875862908202&set=a.108824920279975", width=400)  # Replace with your image path or URL

# Add some text and subheadings
st.header("About Me")
st.write("""
Hello! My name is **John Luis J. Hernandez**, and I am 18 years old. I live in Brgy. Hayanggabon, Claver, Surigao Del Norte. I love dancing, going on nature trips, and playing online games.
""")

# Early Life
st.header("Early Life")
st.write("""
I was born in Fairview, Quezon City, and raised in Brgy. Hayanggabon, Claver, Surigao Del Norte, a small town where I developed a passion for dancing and playing online games from an early age. My interest in these activities started when I was 12 years old. By the time I turned 14, I started exploring nature trips, as I felt that dancing and gaming were becoming repetitive. Nature trips offered a refreshing change and allowed me to enjoy the outdoors.
""")

# Education
st.header("Education")
st.write("""
I graduated from Taganito National High School. High school was an exciting time for me, as it gave me the chance to dive deeper into subjects that fascinated me, while also challenging me to expand my knowledge in new areas. I realized that education isn't just about memorizing facts; it's about learning how to apply that knowledge in the real world.
""")

# Career
st.header("Career")
st.write("""
After graduating from high school, I enrolled at Surigao del Norte State University (SNSU) to pursue a degree in Computer Engineering. This marks the beginning of my journey toward a career in technology, where I hope to contribute to solving real-world problems using my skills and knowledge.
""")

# Hobbies and Interests
st.header("Hobbies and Interests")
st.write("""
When I'm not dancing or playing online games, I enjoy **watching movies**, going on **nature trips**, and **traveling**. Spending quality time with my family is also something I cherish deeply.
""")

# Contact Information
st.header("Contact Information")
st.write("You can reach me at:")
st.write("📞 **Contact Number**: +63 9706858504")  # Replace with your actual contact number
st.write("📧 **Email**: [johnluishernandez925@gmail.com](mailto:johnluishernandez925@gmail.com)")  # Replace with your Gmail

# Footer
st.markdown("---")
st.write("© 2024 John Luis J. Hernandez | All rights reserved")
