import streamlit as st

# Título de la pestaña en el móvil (sin emojis de caras)
st.set_page_config(page_title="30 de Julio", page_icon="✨", layout="centered")

# Encabezado principal
st.title("30 de Julio")
st.markdown("---")

# Tarjeta elegante nativa para tu mensaje sincero
with st.chat_message("user", avatar="💡"):
    st.markdown(
        "***Te he hecho este detalle aunque se que es cutre y malisimo hecho, de verdad perdon por "
        "un detalle tan mierda, pero te lo he hecho porque tu nunca te olvidas de mi. Me alegras "
        "demasiado los dias y siempre me has sacado risas cuando mas lo necesitaba, eres increible "
        "la verdad y queria hacer algo diferente para ti aunque no me de muy bien esto del codigo.***"
    )

st.write("") # Espacio de separación en la pantalla

# Botón interactivo grande para el móvil
if st.button("Mostrar Sorpresa", type="primary", use_container_width=True):
    
    st.markdown("---")
    
    # Cuadro destacado con el subtítulo
    st.warning("30 de Julio - Especial para Ti")
    
    # Mensaje de éxito verde
    st.success("ACCESO CONCEDIDO")
    
    # Cuerpo de la sorpresa limpio y ordenado con markdown (sin emojis de caras)
    st.markdown("""
    ### ¡Feliz dia de la amistad chinita!
    *Eres de verdad la mejor amiga que se puede tener en este mundo.*
    
    ---
    
    En serio, **no te puedes morir nunca** porque me tienes que mantener en el futuro y no se que haria sin ti jajaja. 
    
    Y ya sabes que **siempre que estes mal puedes acudir a mi** para lo que sea, a la hora que sea, porque me importas muchisimo. Gracias por estar siempre.
    """)
