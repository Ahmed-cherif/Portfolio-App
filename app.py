from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "A.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | AHMED CHERIF"
PAGE_ICON = ":wave:"
NAME = "AHMED CHERIF"
DESCRIPTION = """
Software Engineer  Embedded Software Engineer  Data scientist  École nationale de science d'informatique de Tunis ENSI
"""
EMAIL = "ahmed.cherif@ensi-uma.tn"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/ahmed-cherif-061b06148/",
    "GitHub": "https://github.com/Ahmed-cherif",

}
PROJECTS = {
    "🏆 Ask multiple pdfs": "https://github.com/Ahmed-cherif/Ask-multiple-pdfs",
    "🏆 gRPC Text Summarization": "https://github.com/Ahmed-cherif/gRPC-Text-Summarization-Demo",
    "🏆 Violence app detector ": "https://github.com/Ahmed-cherif/Violence_app_detector",
    "🏆 -Coronavirus-tracker-app-with-Spring-Boot-and-Java": "https://github.com/Ahmed-cherif/-Coronavirus-tracker-app-with-Spring-Boot-and-Java",
    "🏆 -Face-Sentiment-Detection-with-Raspberry-Pi ": "https://github.com/Ahmed-cherif/-Face-Sentiment-Detection-with-Raspberry-Pi",
    "🏆 Web-Direction-Detection-React-App ": "https://github.com/Ahmed-cherif/Web-Direction-Detection-React-App",
    "🏆 Sentiment-Analysis-Django-App ": "https://github.com/Ahmed-cherif/Sentiment-Analysis-Django-App",
    "🏆 -Vehicle-Detect-Count-APP ": "https://github.com/Ahmed-cherif/-Vehicle-Detect-Count-APP",
    "🏆 -Plant-Disease-Prediction-APP ": "https://github.com/Ahmed-cherif/-Plant-Disease-Prediction-APP",
    "🏆 Text-Extraction-From-Images-Application ": "https://github.com/Ahmed-cherif/Text-Extraction-From-Images-Application",
    "🏆 Design-and-development-project-PAN-Card-Tampering-Detection ": "https://github.com/Ahmed-cherif/Design-and-development-project-PAN-Card-Tampering-Detection",
    "🏆 Bird-species-flask-app ": "https://github.com/Ahmed-cherif/Bird-species-flask-app",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Education")
st.write('\n')
st.write(
    """
- ✔️ Preparatory Institute for Engineering Studies (ranked 61 among 1200 candidates) , IPEIS 2 years
- ✔️ National School of Computer Science Manouba, Tunisia engineering diploma 3 years
- ✔️ Baccalaureate Diploma in mathematical Science
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write('\n')
st.write(
    """
- 👩‍💻 Programming: Python, C, C++, JavaScript, Php, Mips, Java, Vhdl, R, Matlab

- 📊 Frameworks and Libraries: PyTorch, TensorFlow, Keras, Numpy, Pandas, NLTK, Opencv, Seaborn, Matplotlib, 
        FLASK,Stm32, Freertos, Rpc, Sql, Power Bi, Excel, Grpc, CI/CD, Docker, kubernetes, 
        Jenkins, Aws, Ansible, Git-Github , SSh

- 📚 Soft Skills:: Leadership, Event Management, Writing, Public Speaking, Time Management, 
        Communication

- 🗄️ Skills:: Computer Vision, Natural Language Processing, Deep Learning, Machine Learning, Langchain ,
        Time series forecasting, Reinforcement Learning, Embedded software, Software engineering
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Summer Internships")
st.write("---")
st.write('\n')
# --- JOB 1
st.write("🚧", "**Software Engineer | Fysali SAS Bio-incubateur Eurasanté France**")
st.write("Lille France")
st.write("19/7/2023 - 20/09/2023")
st.write(
    """
    Description: 
    
    Developed and managed a comprehensive database for a 
    cutting-edge Medical Text Classification Application, 
    leveraging advanced Natural Language Processing (NLP) techniques. 
    The application automatically categorizes medical texts
    into "Non-medical violence" and "Medical violence" categories, 
    providing rapid insights.
    It serves as a valuable tool for enhancing healthcare communication and awareness.

- ► Developing an application to prevent medical violence
- ► Successfully tested and implemented various NLP models to optimize text classification accuracy.
- ► Designed and maintained a well-organized database crucial for model training and evaluation.
- ► Collaborated in the creation of a user-friendly interface, ensuring accessibility to a wide audience.
- ► Contributed to the mission of improving healthcare transparency and understanding.
"""
)

st.write('\n')
# --- JOB 2
st.write("🚧", "**Data Scientist | **Centre de recherche en numérique de Sfax**")
st.write("Sfax ,Tunisia")
st.write("15/07/2021 - 30/09/2021")
st.write(
    """
    Description: 
    
    Sign Language Detection using ACTION RECOGNITION with Python

- ► The proposed internship project aims to develop a system that will recognize static sign 
gestures and convert them into corresponding
words.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Software Engineer | Mosofty**")
st.write("Tunis ,Tunisia")
st.write("01/07/2023 - 30/08/2023")
st.write(
    """
    Description: 

    During my summer internship, I worked on a project aimed at enhancing the 
    performance of the company's Optical Character Recognition (OCR) system. 
    My primary role involved developing an artificial intelligence 
    module to improve text recognition accuracy in scanned documents. 
    Additionally, I created an Excel-based database to train and evaluate the model, 
    resulting in a significant reduction in recognition errors.
    Also, I developed a Flask-based microservice to automatically extract 
    information from CVs. 
    The project aimed to streamline and expedite the recruitment process by 
    extracting data.
    In summary, I focused on improving the OCR system's performance and developed 
    a microservice to extract information from CVs, enhancing efficiency in the 
    recruitment process.

- ► Designed and developed an artificial intelligence module using Flask to enhance the OCR system's performance.
- ► Utilized the XGBoost algorithm and XMLRegressor for optimizing text recognition accuracy.
- ► Gathered and prepared relevant data from scanned documents for model training.
- ► Created and managed an Excel-based database for model training and evaluation.
- ► Conducted rigorous testing to assess the module's performance and accuracy.
- ► Thoroughly documented the implemented methods and achieved results.
- ► Designed and developed a Flask microservice for extracting information from CVs.
- ► Extracted structured data from CV documents in various formats.
"""
)

st.write('\n')
# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
st.write("")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
