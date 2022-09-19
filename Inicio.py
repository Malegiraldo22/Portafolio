import streamlit as st
from PIL import Image
from pathlib import Path


# --- PATHS ---
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd
css_file = current_dir / 'static' / 'main.css'
resume_file = current_dir / 'files' / 'HVM.AlejandroGiraldo.pdf'
profile_pic = current_dir / 'images' / 'profile_pic.png'
cert_techlabs = current_dir / 'files' / 'CertTechLabs.pdf'
rec_letter = current_dir / 'files' / 'recommendationletter.pdf'

st.set_page_config(page_title='Alejandro Giraldo Riveros - CV')

# --- Carga de CSS y PDF ---
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open(resume_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()

col1, col2 = st.columns(2, gap='small')
with col1:
    image = Image.open('./images/profile-pic.png')
    st.image(image, width=230, output_format='PNG')
with col2:
    st.title('Alejandro Giraldo')
    st.subheader('Data Scientist')
    st.download_button(
        label='📄 Descargar CV',
        data=PDFbyte,
        file_name=resume_file.name,
        mime='application/octet-stream',
    )
    st.write('📫 magiraldo2224@gmail.com')

#--- SOCIAL LINKS ---
col3, col4, col5, col6 = st.columns(4, gap='small')
with col3:
    image = Image.open('./images/GitHub-Mark-32px.png')
    st.image(image, width=32)
    st.write("[Malegiraldo22](https://github.com/Malegiraldo22)")
with col6:
    image = Image.open('./images/LI-Logo.png')
    st.image(image, width=128)
    st.write("[magiraldo](https://www.linkedin.com/in/magiraldo/)")

# --- Experiencia ---
st.subheader('Experiencia y Calificaciones')
st.write(
    """
    - ✔️ 5 Años de experiencia como Ingeniero Ambiental
    - ✔️ 4 Años de experiencia extrayendo información útil de datos
    - ✔️ Fuerte experiencia práctica y conocimiento en Python
    - ✔️ Buena compresión de los principios estadísticos y sus respectivas aplicaciones
    - ✔️ Excelente jugador de equipo y muestra un fuerte sentido de iniciativa en las tareas a realizar
    """
)

# --- Skills ---
st.subheader("Habilidades duras")
st.write(
    """
- 👩‍💻 Programación: Python (Scikit-learn, Pandas), SQL, Java (Spring framework)
- 📊 Visualización de datos: PowerBi, Matplotlib, Plotly
- 📚 Modelamiento: Linear regression, decition trees, ensemble methods
- 🗄️ Bases de datos: MongoDB, MySQL
- 👩‍💻 Desarrollo Web: HTML5, CSS, Bootstrap
"""
)

# --- Proyectos ---
st.subheader('Proyectos')
st.write('💻 [Global Energy consumption and CO2](https://pgrupal13-proyectogrupal-inicio-3klytr.streamlitapp.com/)')
st.write("""
Proyecto grupal en Soy Henry. Se analizaron las emisiones de CO2 emitidas por diferentes países debido a su producción energética.
Se calcularon KPIs para mostrar el impacto de cada país y se desarrollaron diferentes modelos de machine learning para predecir y evaluar las emisiones de CO2 a futuro.
""")
st.write('---')
st.write('💻 [Análisis COVID-19 USA](https://malegiraldo22-analisis-covid-usa-dashboard-mha1tq.streamlitapp.com/)')
st.write("""
Proyecto individual en Soy Henry. Analicé los impactos del COVID-19 en los Estados Unidos usando datos provenientes de healthdata.gov. Implementé un dashboard en
Streamlit para mostrar los resultados
""")
st.write('---')
st.write('💻[Análisis Dólar en Argentina](https://github.com/Malegiraldo22/Dolar-Argentina/blob/master/Presentaci%C3%B3n.pdf)')
st.write("""
Proyecto individual en Soy Henry. Analicé datos del Banco Central de Argentina sobre la tasa de cambio del Dólar desde el
2002 comparando la tasa de cambio del Dólar Blue y Dólar oficial.
""")
st.write('---')
st.write('💻[Tu Huella](https://github.com/Malegiraldo22/HuellaCarbono)')
st.write("""
Desarrollé una página web, usando Java, Spring framework y MySQL para el backend y HTML, JavaScript, CSS y Bootstrap
para el frontend, en la que los usuarios pueden calcular la huella de carbono generada por sus hábitos de transporte
""")
st.write('---')
st.write('💻[Respirable](https://github.com/Malegiraldo22/Respirable)')
st.download_button(
        label='📄 Descargar Certificado',
        data=PDFbyte,
        file_name=cert_techlabs.name,
        mime='application/octet-stream',
    )
st.write("""
Proyecto final del Bootcamp #Codeathome de Techlabs. Construí un modelo Random Forest en Python usando la biblioteca Sci-kit Learn que predijo el índice de Calidad del Aire en
cinco ciudades(Bogotá, Barcelona, Münster, París, Stockholm y Stuttgart) con un error cuadrático medio de 5.63, 6.88, 8.10,
7.94, 13.77 y 7.50 para cada ciudad
""")


# --- Experiencia laboral ---
st.subheader('Experiencia Laboral')
st.write('Análista de datos | Ingeniero Ambiental')
st.write('Septiembre 2017 - Abril 2019')
st.write("""
- ✔️ Reduje el consumo de agua y energía en un 15% después de realizar un modelo de análisis de datos en una granja lechera
- ✔️ Desarrollé un plan de manejo ambiental en un condominio que redujo la cantidad de uso de agua en un 30% mediante la aplicación de estrategias de circulación de agua lluvia
- ✔️ Reduje el consumo de agua en un 25% en una plantación de flores utilizando estrategias de circulación de agua lluvia
- ✔️ Identifiqué los impactos y planifiqué un plan de manejo ambiental para la recuperación de áreas afectadas por incendios forestales en el municipio de Tenjo, Cundinamarca
- ✔️ Eduqué a las comunidades de bajos ingresos sobre la producción de fertilizantes orgánicos y la separación de residuos sólidos para crear 2 microempresas
""")

st.subheader('Logros')
st.write('🏆 Community Moderator | Dataquest')
st.download_button(
        label='📄 Descargar Carta recomendación',
        data=PDFbyte,
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