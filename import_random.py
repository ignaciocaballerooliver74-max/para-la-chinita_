import streamlit as st

# Configuración del título de la pestaña
st.set_page_config(page_title="30 de Julio - Especial para Ti", layout="centered")

# Título de la aplicación en la pantalla
st.title("30 de Julio - Especial para Ti")

# Botón interactivo (Función del botón sorpresa)
if st.button("mostrar_sorpresa"):
    # Cuadro de información con tus mensajes originales exactos
    st.info("""
    🔓 ACCESO CONCEDIDO
    
    ¡Feliz día de la amistad chinita, eres la mejor amiga que se puede tener!\\n\\n
    No te puedes morir nunca porque me tienes que mantener y 
    siempre que estés mal puedes acudir a mí porque me importas. 💕
    """)
