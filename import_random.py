import streamlit as st

# Configuración básica de la página para móviles
st.set_page_config(page_title="30 de Julio", layout="centered")

# Título principal limpio y estilizado
st.markdown("<h1 style='text-align: center; font-weight: bold;'>30 de Julio</h1>", unsafe_html=True)
st.markdown("---")

# Nota introductoria en un bloque de texto limpio y elegante
st.markdown(
    "*Te he hecho este detalle aunque sé que es cutre y malísimo hecho, "
    "te lo he hecho porque nunca te olvidas de mí, me alegras los días y me has "
    "sacado risas, eres increíble la verdad y perdón por un detalle tan mierda.*"
)

st.write("")  # Espacio en blanco de separación

# Botón de acción principal adaptado al ancho de la pantalla del celular
if st.button("Mostrar Sorpresa", type="primary", use_container_width=True):
    
    st.markdown("---")
    
    # Subtítulo de la sección de la sorpresa
    st.markdown("<h3 style='text-align: center;'>30 de Julio - Especial para Ti</h3>", unsafe_html=True)
    
    # Mensaje de confirmación en un recuadro verde minimalista
    st.success("ACCESO CONCEDIDO")
    
    # Mensajes originales organizados con una tipografía clara y sin emojis
    st.markdown("""
    ### ¡Feliz día de la amistad chinita!
    *Eres la mejor amiga que se puede tener.*
    
    ---
    
    **No te puedes morir nunca** porque me tienes que mantener y 
    siempre que estés mal **puedes acudir a mí** porque me importas.
    """)
