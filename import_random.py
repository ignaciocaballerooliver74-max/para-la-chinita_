import streamlit as st

# Título de la pestaña en el navegador del celular
st.set_page_config(page_title="30 de Julio", layout="centered")

# Título principal idéntico a tu ventana original
st.title("30 de Julio")

# Texto sincero antes de revelar la sorpresa
st.write("Te he hecho este detalle aunque sé que es cutre y malísimo hecho, te lo he hecho porque nunca te olvidas de mí, me alegras los días y me has sacado risas, eres increíble la verdad y perdón por un detalle tan mierda.")

# El botón sorpresa tal cual lo programaste
if st.button("mostrar_sorpresa"):
    # Texto inicial dentro de la sorpresa
    st.write("30 de Julio - Especial para Ti")
    
    # Cuadro de texto con el formato y contenido exactos de tu código original
    st.code("""
🔓 ACCESO CONCEDIDO

¡Feliz día de la amistad chinita, eres la mejor amiga que se puede tener!

No te puedes morir nunca porque me tienes que mantener y 
siempre que estés mal puedes acudir a mí porque me importas.
""", language="")
