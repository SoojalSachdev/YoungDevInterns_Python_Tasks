import streamlit as st

# Custom CSS for styling
def apply_custom_css():
        st.markdown(
            """
            <style>
            /* Dark mode styling */
            body {
                background-color: #000;
                color: #d33682;
            }
            .stTitle {
                color: #80caff;
            }
            .stSubtitle {
                color: #cccccc;
            }
            .css-1d391kg p {
                color: #f4f4f4;
            }
            </style>
            """, unsafe_allow_html=True
        )
    # Function to display about me section
def display_about_me():
    st.subheader("About Me")
    st.write("""
    I am a passionate Python Developer and Computer Science student with a strong foundation in programming and web development. My journey into the world of coding began in 2019 when I was in the 10th grade. Driven by curiosity, I moved to Karachi and completed a one-year diploma at Aptech, where I honed my skills in HTML5, CSS3, Bootstrap, JavaScript, C Language, C#, .NET, SQL, and Microsoft Office.

    Currently, I am pursuing a Bachelor of Computer Science at DHA Suffa University and have successfully completed my 4th semester. During my 2nd semester, I took on the role of IT Manager at Intellect Consultancy, where I managed tech-related activities, developed websites, and gained hands-on experience with WordPress. My expertise extends to e-commerce, where I am currently exploring Shopify, building and customizing user-friendly online stores.

    With a strong command over Java, Python, and C, I am dedicated to creating efficient and innovative solutions. I am excited to continue growing my skills and contributing to impactful projects in the tech industry.
    """)

# Function to display education information
def display_education():
    st.subheader("Education")
    st.write("**Bachelor of Computer Science**")
    st.write("DHA Suffa University – 2022 - 2026")
    st.write("Currently in 4th semester")

# Function to display work experience
def display_work_experience():
    st.subheader("Work Experience")
    st.write("""
    **IT Manager | Intellect Consultancy | Remote Job** (Aug 2023 - July 2024)
    - Managed all tech-related activities, ensured smooth operation, and set up systems to boost productivity.
    - Developed and managed websites:
        - [www.intellectacc.com](http://www.intellectacc.com/)
        - [takadaassetmanagement.com/gu](https://takadaassetmanagement.com/gu)
        - [scentdaze.com](https://scentdaze.com/)
    """)

    st.write("""
    **Python Developer Internship | YoungDev Interns | Remote Job** (Aug 2024 - Present)
    - Collaborating on real-world projects, leveraging industry-standard tools and best practices.
    - Creating and refining Python-based solutions in a dynamic remote work environment.
    - Building a diverse portfolio that showcases my technical expertise and problem-solving skills.
    - Gaining hands-on experience in a supportive, collaborative team environment.
    """)

# Function to display programming proficiency
def display_programming_proficiency():
    st.subheader("Programming Proficiency")
    st.write("- **Java**: Mastery in crafting robust, efficient applications (2023 - present)")
    st.write("- **Python**: Proficient in developing efficient applications (2022 - 2024)")
    st.write("- **C Language**: Expertise in creating low-level applications (2021 - 2023)")

# Function to display web development skills
def display_web_development_skills():
    st.subheader("Web Development Mastery")
    st.write("- **HTML**: Proficient in creating structured web content (2019 - present)")
    st.write("- **CSS**: Expertise in enhancing visual appeal (2019 - present)")
    st.write("- **Bootstrap**: Skillful in designing responsive websites (2020 - present)")
    st.write("- **JavaScript**: Command in building dynamic web applications (2020 - 2021)")

# Function to display Shopify experience
def display_shopify_experience():
    st.subheader("Shopify Experience")
    st.write("""
    - **Shopify (May 2024 - Present)**: Created and customized websites using Shopify.
    - 3 months of hands-on experience with the Shopify platform.
    - Built and designed user-friendly online stores, improved layouts, and added features.
    """)

# Function to display the contact information
def display_contact_info():
    st.subheader("Contact Information")
    st.write("**Phone**: +92 333 7301936")
    st.write("**Email**: soojalsachdev2@gmail.com")
    st.write("**LinkedIn**: [linkedin.com/in/soojal-kumar](https://www.linkedin.com/in/soojal-kumar/)")
    st.write("**Address**: 209 – Sahil promenade, block 3, Clifton, Karachi.")



# Main function to display the resume
def main():
    apply_custom_css()
    st.title("Soojal Kumar - Web Developer")
    display_about_me()
    display_programming_proficiency()
    display_web_development_skills()
    display_education()
    display_work_experience()
    display_shopify_experience()
    display_contact_info()

if __name__ == "__main__":
    main()
