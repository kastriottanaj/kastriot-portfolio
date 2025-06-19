import streamlit as st
from PIL import Image
import smtplib
from email.message import EmailMessage
import ssl

st.set_page_config(page_title="Kastriot Tanaj - Profile", layout="centered")
st.title("👨‍💻 Kastriot Tanaj")
st.subheader("SEO Specialist | Marketing Enthusiast | Python Developer")

st.markdown(
    "🔗 [Connect on LinkedIn](https://www.linkedin.com/in/kastriot-tanaj)")

st.header("About Me")
st.write("Hi, hello there, I am Kastriot Tanaj with 4 years and a half experience in SEO. Worked for a swiss company 🇨🇭 as an intern after two years in that company. I got really good with SEO, then I completed a lot of training for WordPress. I got into computer science university to learn more about coding, THE REASON: because I am a person who likes to combine things and make MAGIC HAPPENS 🪄. While understanding marketing in depth I am able to build websites and rank them for you. WHAT IS THE POINT OF BUILDING WEBSITES WHILE NO ONE SEES YOUR WEBSITE. Currently learning python 🐍 in depth to create more magic between SEO, AI and Programming. Lets have a coffee ☕️ or connect on LinkedIn.  ")

st.header("Skills 🎯")
st.write("Search Engine Optimization, Social Media Marketing, WordPress, Python, Django, JavaScript(React), MySQL, currently learning ML AND DATA SCIENCE")

st.subheader("Soft Skills")
st.write("I am a person who reallyyyy likes soft skills, communicating with people ideas straight to the point.")

st.subheader("Books 📚")
st.write("Why I added books, because reading books Is a skill to me, especially business books, marketing/sales books")

st.header("Projects")
st.markdown("""
- 🔧 GraNex Web App cooperated with Sibora Berisha.
- 🥋 Kickboxing Club Website
- 🏡 Gardening company based in Germany, Köln, build the website and helping the company with SEO. AT BAU.
- 🏨 Hotel Website and helped rank on Local Search. Name of the hotel based in Amsterdam: Faralda Crand Hotel
""")

st.header("Education")
st.markdown("🎓 Bachelor in Computer Science (In Progress)")

st.header("Certificates")
st.markdown("""
- Google Cloud Badge – AI and ML
- Complete Python Mastery | Codewithmosh
- Certificates from SEMrush | To increase my SEO skills
- And more, but if you wanna see my list of Certificates visit my LinkedIn Profile
""")

st.header("Competitions")
st.markdown("🏆 Participated in coding hackathons and AI competitions.")

# Gallery
st.header("Gallery")

try:
    profile_img = Image.open("kastriot.jpg")
    project_img1 = Image.open("sts.png")
    project_img2 = Image.open("atbau.png")
    project_img3 = Image.open("faralda.png")
    project_img4 = Image.open("imargroup.png")
    project_img5 = Image.open("granex.png")

    st.image(profile_img, caption="This is me!", width=200)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(project_img1, caption="I implemented SEO strategy for the STS company, while I managed to rank the company on the first page for important keywords", use_container_width=True)
    with col2:
        st.image(project_img2, caption="I made the website with wordpress and currently doing SEO to rank higher for the important keywords", use_container_width=True)
    with col3:
        st.image(project_img3, caption="Faralda Crane Hotel, currently doing Local SEO and optimizing GMB to increase leads, so more people book the hotel",
                 use_container_width=True)
    with col4:
        st.image(project_img4, caption="Imar Group, destribution company for cosmetics&beauty products",
                 use_container_width=True)
    with col5:
        st.image(project_img5, caption="GraNex company, distribution company, build the web app with Sibora Berisha, python/django used for backend, React for frontend", use_container_width=True)


except Exception as e:
    st.warning(f"Error loading images: {e}")

st.header("Wanna know me more, you can download my CV, to see my work")


with open("kastriot-tanaj-CV.pdf", "rb") as f:
    pdf_bytes = f.read()

st.download_button(
    label="📄 Download My CV",
    data=pdf_bytes,
    file_name="Kastriot_Tanaj_CV.pdf",
    mime="application/pdf"
)


st.header("📬 Contact Me")
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit = st.form_submit_button("Send")

    if submit:
        try:
            sender_email = "kastriot.sym@gmail.com"  # change to your email
            sender_password = "bsxx kwdc hnmt uuye"  # generate app password from Google
            receiver_email = "kastriot.sym@gmail.com"

            email_msg = EmailMessage()
            email_msg["Subject"] = f"Message from {name}"
            email_msg["From"] = sender_email
            email_msg["To"] = receiver_email
            email_msg.set_content(f"Name: {name}\nEmail: {email}\n\n{message}")

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, sender_password)
                server.send_message(email_msg)

            st.success("Your message has been sent!")
        except Exception as e:
            st.error(f"An error occurred: {e}")

st.markdown("---")
st.write("Thanks for visiting! 🙏")
