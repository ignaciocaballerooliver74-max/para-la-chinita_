import streamlit as st

# Configuración técnica de la página
st.set_page_config(page_title="30 de Julio", layout="centered")

# Título de la aplicación estilizado en negro/blanco puro
st.markdown("<h1 style='text-align: center; font-weight: 700;'>30 de Julio</h1>", unsafe_html=True)
st.markdown("---")

# Nota introductoria en un bloque de texto destacado y limpio
st.info(
    "Te he hecho este detalle aunque sé que es cutre y malísimo hecho, "
    "te lo he hecho porque nunca te olvidas de mí, me alegras los días y me has "
    "sacado risas, eres increíble la verdad y perdón por un detalle tan mierda."
)

st.write("") # Espacio de diseño

# Botón de acción principal expandido para la pantalla del móvil
if st.button("Mostrar Sorpresa", type="primary", use_container_width=True):
    
    st.markdown("---")
    
    # Encabezado de la sección de la sorpresa
    st.markdown("<h3 style='text-align: center;'>30 de Julio - Especial para Ti</h3>", unsafe_html=True)
    
    # Mensaje de confirmación de acceso en un recuadro verde limpio
    st.success("ACCESO CONCEDIDO")
    
    # Mensajes originales con un formato de texto sofisticado y sin emojis
    st.markdown("""
    ### ¡Feliz día de la amistad chinita!
    *Eres la mejor amiga que se puede tener.*
    
    ***
    
    **No te puedes morir nunca** porque me tienes que mantener y 
    siempre que estés mal **puedes acudir a mí** porque me importas.
    """)
