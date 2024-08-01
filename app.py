from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Ahmed Cherif.pdf"
profile_pic = current_dir / "assets" / "a.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | AHMED CHERIF"
PAGE_ICON = ":wave:"
NAME = "AHMED CHERIF"
DESCRIPTION = """
Software Engineer  Embedded Software Engineer  Data scientist  École nationale de science d'informatique de Tunis ENSI
"""
EMAIL = "ahmed.cherif@ensi-uma.tn"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/ahmed-cherif-%F0%9F%87%B5%F0%9F%87%B8-061b06148/",
    "GitHub": "https://github.com/Ahmed-cherif",

}
PROJECTS = {
    "🏆 Google Cloud Data Pipeline Analytics Project": "https://github.com/Ahmed-cherif/sales-data-pipeline-project",
    "🏆 Cricket Statistics Pipeline with Google Cloud Services": "https://github.com/Ahmed-cherif/cricket-stat-data-engineering-project",
    "🏆 TCP Chat Application": "https://github.com/Ahmed-cherif/Socket-Client",
    "🏆 Motion Detection System Using Raspberry Pi": "https://github.com/Ahmed-cherif/-Motion-Detection-System-Using-Raspberry-Pi",
    "🏆 Ask multiple pdfs using Longchain": "https://github.com/Ahmed-cherif/Ask-multiple-pdfs",
    "🏆 gRPC Text Summarization": "https://github.com/Ahmed-cherif/gRPC-Text-Summarization-Demo",
    "🏆 Application to prevent medical violence ": "https://github.com/Ahmed-cherif/Violence_app_detector",
    "🏆 Coronavirus tracker app with Spring Boot and Java": "https://github.com/Ahmed-cherif/-Coronavirus-tracker-app-with-Spring-Boot-and-Java",
    "🏆 Face Sentiment Detection with Raspberry Pi ": "https://github.com/Ahmed-cherif/-Face-Sentiment-Detection-with-Raspberry-Pi",
    "🏆 Sentiment Analysis Django App ": "https://github.com/Ahmed-cherif/Sentiment-Analysis-Django-App",
    "🏆 Vehicle Detect Count APP ": "https://github.com/Ahmed-cherif/-Vehicle-Detect-Count-APP",
    "🏆 Plant Disease Prediction APP ": "https://github.com/Ahmed-cherif/-Plant-Disease-Prediction-APP",
    "🏆 Text Extraction From Images Application ": "https://github.com/Ahmed-cherif/Text-Extraction-From-Images-Application",
    "🏆 Design and development of PAN Card Tampering detector ": "https://github.com/Ahmed-cherif/Design-and-development-project-PAN-Card-Tampering-Detection",
    "🏆 Bird species flask App ": "https://github.com/Ahmed-cherif/Bird-species-flask-app",
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
- ✔️ National School of Computer Science ENSI, Computer Science engineering diploma
- ✔️ Baccalaureate Diploma in mathematical Science
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write('\n')
st.write(
    """
- 👩‍💻 Programming: Python, C, C++, Mips, Java, VHDL, R

- 📊 Frameworks ,Tools and Libraries: PyTorch, TensorFlow, Keras, NumPy, Pandas, NLTK, OpenCV, Seaborn, Matplotlib, Flask, Streamlit, Yocto, SQL, NoSQL, Power Bi, Docker, Kubernetes, Docker Compose, GCP, Gitlab, TCP/IP, Networking, SPI, I2C, UART, Terraform, Spark, Hadoop, Micro-services, Script Shell, Kubeflow, Vertex AI, Gcp Bucket, Dataflow, Cloud Composer, Looker, Cloud function, Apache Airflow, BigQuery

- 📊 Cartes: STM32, Raspberry pi, Esp32, Arduino

- 📚 Soft Skills: Leadership, Project Management, Writing, Team Management, Communication, Coaching

- 🗄️ Skills: Computer Vision, Classification, Segmentation, Prediction, Natural Language Processing, Deep Learning, Machine Learning, Time series forecasting, Embedded Linux, Software Engineering, SCRUM

"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Summer Internships")
st.write("---")
st.write('\n')

st.write("🚧", "**• R&D Engineer | Sofrecom Tunisia**")
st.write("Sfax, Tunis")
st.write("05/2/2024 - 03/08/2024")
st.write(
    """
    Description: 
    
    I have developed an advanced real-time lip-reading system that translates visual speech cues into audible speech. This system processes
live video feeds to generate precise text predictions, which are then synthesized into speech, enhancing communication for individuals.

- ►Developed a novel real-time lip-reading system using CTC, TimeDistributed, 3DCNN and Bi-LSTM networks.
- ►Achieved high accuracy with a Character Error Rate (CER) of 8.15% and Character Accuracy (CA) of 91.85% on the GRID dataset.
- ►Implemented a deployment strategy using Flask to enable real-time lip reading through a web application.
- ►Achieved text predictions and synthesized speech by normalizing image data, using CTC decoding, correcting text with TextBlob.
- ►Integrated TensorFlow and MediaPipe to capture and process lip movements.
- ►Constructed the DATAV1 dataset with more than 600 files for initial model training and evaluation.
- ►Conducted a comprehensive analysis of deep learning model architectures for lip reading using the DATAV1 dataset.
- ►Explored and evaluated multiple architectures like ResBlock3D, Conv3D, Conv2D, TimeDistributed, attention mechanism, and LSTM.
- ►Identified the optimal architecture achieving a peak validation accuracy of 98.18%.
- ►Contributed insights into effective model selection for accurate lip-reading performance.
- ►Constructed the DataV2 dataset with more than 4000 files for enhanced model training and evaluation.
- ► Designed a new lip-reading model architecture incorporating 3D CNN, Bi-LSTM, TimeDistributed, and SoftMax layers.
- ► Developed a real-time lip-reading application with a video interface displaying synchronized subtitles and predictions.
- ► Implemented a chatbot using Voice flow and trained it with GPT-3.5 for user interaction and assistance
- ► Designed and implemented a Video Metting Page
- ► converting text to speech with Google Text-to-Speech (gTTS).
"""
)
st.write('\n')
# --- JOB 1
st.write("🚧", "**Software Engineer | Fysali SAS Bio-incubateur Eurasanté France**")
st.write("Lille, France")
st.write("19/7/2023 - 20/09/2023")
st.write(
    """
    Description: 
    
    Developed an application to prevent medical violence
    and managed a comprehensive database for a 
    cutting-edge Medical Text Classification Application, 
    leveraging advanced Natural Language Processing (NLP) techniques. 
    The application automatically categorizes medical texts
    into "Non-medical violence" and "Medical violence" categories, 
    providing rapid insights.
    It serves as a valuable tool for enhancing healthcare communication and awareness.

- ► Developing an application to prevent medical violence
- ► Successfully tested and implemented various NLP models to optimize the accuracy.
- ► Designed and maintained a well-organized database crucial for model training and evaluation.
- ► Collaborated in the creation of a user-friendly interface, ensuring accessibility to a wide audience.
- ► Contributed to the mission of improving healthcare transparency and understanding.
"""
)



# --- JOB 2
st.write('\n')
st.write("🚧", "**Software Engineer | Mosofty**")
st.write("Tunis, Tunisia")
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
# --- JOB 3
st.write("🚧", "Data Scientist | Centre de recherche en numérique de Sfax")
st.write("Sfax, Tunisia")
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
st.write('\n')
# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
st.write("")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
