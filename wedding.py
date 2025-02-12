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
    "imagejg" : "pics/juandagallo.jpg",
    "imagejl" : "pics/Juanes.jpg",
    "imagejj" : "pics/juanjohenao.jpg",
    "imagekg" : "pics/KatheGallego.jpg",
    "imagelz" : "pics/LauraZapata.jpg",
    "imagelr" : "pics/Leidy.jpg",
    "imagelm" : "pics/loremakeup.jpg",
    "imagelg" : "pics/luisagallina.jpg",
    "imagepj" : "pics/PaolaJuan.jpg",
    "imagemt" : "pics/Martín.jpg",
    "imageyb" : "pics/Yessica.jpg",
    "imageyr" : "pics/yuliethrobin.jpg",
}

image_path = next((image_map.get(key) for key in query_params if key in image_map), None)
print("image_path: ", image_path)

if image_path is not None:
    # st.video('pics/invitacion 20%.mp4', loop = True, autoplay=True)
    st.image("pics/invitacion 20%.gif")
    st.image(image_path)

    if image_path == "pics/juandagallo.jpg":
        with st.container(key="padrinos"):
            # st.divider()
            @st.dialog("Invitación")
            def padrino():
                st.warning("Gallo, por ocupar un lugar muy especial en nuestros corazones, queremos que seas nuestro padrino 🤵💓")
            # st.divider()
            padrino()
            st.warning("Gallo, por ocupar un lugar muy especial en nuestros corazones, queremos que seas nuestro padrino 🤵💓")
    elif image_path == "pics/DanielaCardona.jpg":
        with st.container(key="padrinos"):
            # st.divider()
            @st.dialog("Invitación")
            def madrina():
                st.warning("Daniela, por ocupar un lugar muy especial en nuestros corazones, queremos que seas nuestra madrina 👸💓")
            # st.divider()
            madrina()
            st.warning("Daniela, por ocupar un lugar muy especial en nuestros corazones, queremos que seas nuestra madrina 👸💓")

    with st.expander("Ubicación"):
        # st.text("Ubicación")
        location_map = '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3967.035675216696!2d-75.41892872627282!3d6.1259016276586316!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8e469fbde4169acb%3A0x704574a6c9fbb8b5!2sLa%20Jacinta%20Casa%20Boutique!5e0!3m2!1ses!2sco!4v1739253697287!5m2!1ses!2sco" width="100%" height="200px" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
        st.markdown(location_map, unsafe_allow_html=True)
        
    with st.expander("Código de Vestimenta"):
        # st.text("A continuación, encontrarás referencias de qué vestuario utilizar en la boda.")

        # URL del tablero de Pinterest (cambia esto con tu tablero)
        pinterest_url = "https://www.pinterest.com/zuliramcs/wedding-clothes/"

        image_url = "pics/pinterest.png"

        # HTML para hacer que la imagen sea un enlace clickeable
        # st.html("<img src='pics/pinterest.png'>")

        st.image("pics/pinterest.png", use_container_width=True)
        st.link_button("Ver más", url=pinterest_url)

        # # Botón para abrir el tablero
        # st.markdown(f"[👉 Ver el tablero en Pinterest]({pinterest_url})")

        
    # with st.expander("Confirmar asistencia"):
    #     st.text("Confirmar Asistencia")
else:
    st.title("Hay un error con tu link, por favor contacta a Esteban")