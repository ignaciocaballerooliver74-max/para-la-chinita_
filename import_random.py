import streamlit as st

# Título de la pestaña en el móvil
st.set_page_config(page_title="30 de Julio", page_icon="✨", layout="centered")

# Encabezado principal
st.title("🌟 30 de Julio")
st.markdown("---")

# Tarjeta elegante nativa para tu mensaje sincero
with st.chat_message("user", avatar="💡"):
    st.markdown(
        "***Te he hecho este detalle aunque sé que es cutre y malísimo hecho, "
        "te lo he hecho porque nunca te olvidas de mí, me alegras los días y me has "
        "sacado risas, eres increíble la verdad y perdón por un detalle tan mierda.***"
    )

st.write("") # Espacio de separación en la pantalla

# Botón interactivo grande para el móvil
if st.button("✨ Mostrar Sorpresa ✨", type="primary", use_container_width=True):
    
    st.markdown("---")
    
    # Cuadro destacado con el subtítulo
    st.warning("⚡ 30 de Julio - Especial para Ti")
    
    # Mensaje de éxito verde
    st.success("🔓 ACCESO CONCEDIDO")
    
    # Cuerpo de la sorpresa limpio y ordenado con markdown
    st.markdown("""
    ### 💕 ¡Feliz día de la amistad chinita!
    *Eres la mejor amiga que se puede tener.*
    
    ---
    
    🫩​ ***No te puedes morir nunca*** porque me tienes que mantener...
    
    ❤️ Y siempre que estés mal ***puedes acudir a mí*** porque me importas.
    """)
