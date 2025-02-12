import streamlit as st

# st.title("Mari and Esteban's wedding")

def load_css(file_name):
    with open(file_name, "r") as f:
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

load_css("styles.css")

query_params = st.query_params

image_map = {
    "imageaoa" : "pics/AlbaOdiliaAlejandra.jpg",
    "imagear" : "pics/AlejaRashid.jpg",
    "imagealx" : "pics/Alex.jpg",
    "imageag" : "pics/AnaGalezo.jpg",
    "imagecg" : "pics/CamiloGil.jpg",
    "imageca" : "pics/Carolina.jpg",
    "imagecm" : "pics/Conrado.jpg",
    "imagedc" : "pics/DanielaCardona.jpg",
    "imagefc" : "pics/FamiliaCastro.jpg",
    "imagejl" : "pics/Juanes.jpg",
    "imagekg" : "pics/KatheGallego.jpg",
    "imagelz" : "pics/LauraZapata.jpg",
    "imagelr" : "pics/Leidy.jpg",
    "imagelg" : "pics/LuisaJuanGallo.jpg",
    "imagepj" : "pics/PaolaJuan.jpg",
    "imagemt" : "pics/Martín.jpg",
    "imageyb" : "pics/Yessica.jpg",
}

if "imageaoa" in query_params:
    image_path = image_map["imageaoa"]
elif "imagear" in query_params:
    image_path = image_map["imagear"]
elif "imagealx" in query_params:
    image_path = image_map["imagealx"]
elif "imageag" in query_params:
    image_path = image_map["imageag"]
elif "imagecg" in query_params:
    image_path = image_map["imagecg"]
elif "imageca" in query_params:
    image_path = image_map["imageca"]
elif "imagecm" in query_params:
    image_path = image_map["imagecm"]
elif "imagedc" in query_params:
    image_path = image_map["imagedc"]
elif "imagefc" in query_params:
    image_path = image_map["imagefc"]
elif "imagejl" in query_params:
    image_path = image_map["imagejl"]
elif "imagekg" in query_params:
    image_path = image_map["imagekg"]
elif "imagelz" in query_params:
    image_path = image_map["imagelz"]
elif "imagelr" in query_params:
    image_path = image_map["imagelr"]
elif "imagelg" in query_params:
    image_path = image_map["imagelg"]
elif "imagepj" in query_params:
    image_path = image_map["imagepj"]
elif "imagemt" in query_params:
    image_path = image_map["imagemt"]
elif "imageyb" in query_params:
    image_path = image_map["imageyb"]

# st.video('pics/invitacion 20%.mp4', loop = True, autoplay=True)
st.image("pics/invitacion 20%.gif")
st.image(image_path)
with st.expander("Ubicación"):
    st.title("Ubicación")
    location_map = '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3967.035675216696!2d-75.41892872627282!3d6.1259016276586316!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8e469fbde4169acb%3A0x704574a6c9fbb8b5!2sLa%20Jacinta%20Casa%20Boutique!5e0!3m2!1ses!2sco!4v1739253697287!5m2!1ses!2sco" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
    st.markdown(location_map, unsafe_allow_html=True)
with st.expander("Código de Vestimenta"):
    st.text("Tablero de Pinterest")
with st.expander("Confirmar asistencia"):
    st.text("Confirmar Asistencia")