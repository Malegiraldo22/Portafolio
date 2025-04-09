import streamlit as st
from PIL import Image
from pathlib import Path

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title='Alejandro Giraldo Riveros - CV', page_icon='📊', layout='wide')

# --- PATHS ---
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd
css_file = current_dir / 'static' / 'main.css'
resume_file = current_dir / 'files' / 'HVM.AlejandroGiraldo.pdf'
profile_pic = current_dir / 'images' / 'profile_pic.png'
cert_techlabs = current_dir / 'files' / 'CertTechLabs.pdf'
rec_letter = current_dir / 'files' / 'recommendationletter.pdf'


# --- Carga de CSS y PDF ---
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open(resume_file, 'rb') as pdf_file:
    CV = pdf_file.read()

with open(cert_techlabs, 'rb') as pdf_file:
    CERT = pdf_file.read()

with open(rec_letter, 'rb') as pdf_file:
    REC = pdf_file.read()

# --- ENCABEZADO ---
col1, col2 = st.columns([1, 2])
with col1:
    image = Image.open('./images/profile-pic.png')
    st.image(image, width=200, output_format='PNG')
with col2:
    st.title('Alejandro Giraldo')
    st.subheader('Data Scientist | Ingeniero Ambiental')
    st.write("Transformando datos en información práctica para un mundo mejor.")
    st.download_button(
        label='📄 Descargar CV',
        data=CV,
        file_name=resume_file.name,
        mime='application/octet-stream',
    )
    st.write('📫 magiraldo2224@gmail.com')
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-000?style=flat&logo=github&logoColor=white)](https://github.com/Malegiraldo22) "
                "[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/magiraldo)")


# --- SOBRE MÍ ---
st.markdown("---")
st.header("👋 Sobre mí")
st.write("""
         Soy un cientifíco de datos e ingeniero ambiental con más de 5 años de experiencia aplicando tecnología para resolver problemas reales.\n
         Tengo habilidades avanzadas en Python, SQL y visualización de datos. Me apasiona el aprendizaje continuo y la comunicación clara de los resultados
        """)

# --- MÉTRICAS RÁPIDAS ---
st.markdown("---")
col1, col2, col3 = st.columns(3)
col1.metric("Proyectos completados", "12+")
col2.metric("Años de experiencia", "5+")
col3.metric("Certificaciones técnicas", "6")

# --- STACK TÉCNICO ---
st.markdown("---")
st.header("🛠️Stack técnico")
cols = st.columns(4)
skills = [
    "Python", "SQL", "Pandas", "Numpy",
    "Scikit-learn", "Power BI", "MongoDB", "MySQL",
    "Spring Boot", "HTML/CSS", "Plotly", "Matplotlib"
]

for index, skill in enumerate(skills):
    cols[index % 4].markdown(f"- {skill}")

# --- PROYECTOS DESTACADOS ---
st.markdown("---")
st.header("🚀 Proyectos Destacados")

project_data = [
    {
        "title": "HaloBotTrainingData",
        "description": "Análisis de entrenamiento en Halo Infinite usando API de Gemini.",
        "link": "https://halobottrainingdata.streamlit.app/"
    },
    {
        "title": "Análisis COVID-19 USA",
        "description": "Dashboard interactivo sobre el impacto del COVID-19 en EE. UU.",
        "link": "https://malegiraldo22-analisis-covid-usa-dashboard-mha1tq.streamlitapp.com/"
    },
    {
        "title": "Tu Huella",
        "description": "Web app para calcular huella de carbono basada en hábitos de transporte.",
        "link": "https://github.com/Malegiraldo22/HuellaCarbono"
    },
    {
        "title": "Respirable",
        "description": "Modelo de predicción de calidad del aire en 6 ciudades usando Random Forest.",
        "link": "https://github.com/Malegiraldo22/Respirable"
    },
    {
        "title":"XBlueskybot",
        "description":"Bot que genera tweets usando la API de Gemini y los publica en X y Bluesky",
        "link": "https://github.com/Malegiraldo22/XBlueskybot"
    }
]

for project in project_data:
    st.subheader(f"💻 {project['title']}")
    st.write(project['description'])
    st.markdown(f"[🔗 ver proyecto]({project['link']})")
    st.write("---")

# --- EDUCACIÓN ---
st.header("🎓 Educación")
education_list = [
    "Data Scientist - Henry (2022)",
    "Full Stack Developer - Universidad Sergio Arboleda + MINTIC (2021)",
    "Data Science - Techlabs (2020)",
    "Data Science - Dataquest / Codecademy (2020)",
    "Ingeniería Ambiental - Universidad de La Salle (2010-2016)"
]

for edu in education_list:
    st.write(f"📘 {edu}")

# --- EXPERIENCIA LABORAL ---
st.markdown("---")
st.header("💼 Experiencia laboral")
experiences = {
    "NielsenIQ (2023)": [
        "Evaluación de ventas para empresas de retail en EE. UU. y Canadá usando SQL.",
        "Mantenimiento de dashboards y soporte analítico a clientes."
    ],
    "Alcaldía de Tenjo (2022 - 2023)": [
        "Lideré el seguimiento del Plan de Gestión de Residuos Sólidos (98% cumplimiento).",
        "Capacitación ambiental a comunidades y reciclaje (800+ personas beneficiadas)."
    ],
    "Gruppo MG (2017 - 2019)": [
        "Reduje el uso de agua en condominios y floricultura hasta en 30%.",
        "Desarrollé planes de manejo ambiental post-incendios forestales."
    ]
}

for job, details in experiences.items():
    with st.expander(f"🧑‍💼 {job}"):
        for d in details:
            st.write(f"- {d}")

st.subheader('Logros')
st.write('🏆 Community Moderator | Dataquest')
st.download_button(
        label='📄 Descargar Carta recomendación',
        data=REC,
        file_name=rec_letter.name,
        mime='application/octet-stream',
    )
st.write("""
Moderador de comunidad en el foro de ayuda de Dataquest desde Marzo de 2022. Realizando las siguientes contribuciones
- ✔️ Respondí más de 36 preguntas resultas de los alumnos, relacionadas con Data science, dando siempre explicaciones informativas, al grano, claras y exhaustivas de conceptos complejos usando un lenguaje sencillo y haciendo un seguimiento de esas preguntas
- ✔️ Revisé 8 proyectos guiados, compartidos por los alumnos y realicé comentarios constructivos y prácticos
- ✔️ Compartí recursos y documentación adicional junto a ejemplos ilustrativos para profundizar el aprendizaje
- ✔️ Proporcioné estímulo, motivación y participación productiva en las publicaciones compartidas por otros alumnos
""")


# --- PIE DE PÁGINA ---
st.markdown("---")
st.write("© 2024 Alejandro Giraldo — CV Digital en Streamlit")