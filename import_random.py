import streamlit as st

# Configuración de la página
st.set_page_config(page_title="30 de Julio", page_icon="✨", layout="centered")

# --- DISEÑO Y ESTILO PERSONALIZADO (CSS) ---
st.markdown("""
    <style>
    /* Fondo con degradado suave y moderno para toda la aplicación */
    .stApp {
        background: linear-gradient(135deg, #1e1e2f 0%, #2d2d44 50%, #3d2d44 100%);
        color: #f0f2f6;
    }
    
    /* Estilo para los títulos principales */
    .titulo-principal {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-weight: 800;
        text-align: center;
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        padding-bottom: 10px;
    }
    
    /* Cuadro elegante para la dedicatoria inicial */
    .tarjeta-mensaje {
        background-color: rgba(255, 255, 255, 0.07);
        border-left: 5px solid #ff4b4b;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .tarjeta-mensaje p {
        font-size: 1.1rem;
        line-height: 1.6;
        font-style: italic;
        color: #e0e0fc;
    }
    
    /* Caja contenedora para la sorpresa final */
    .caja-sorpresa {
        background: rgba(255, 75, 75, 0.08);
        border: 1px solid rgba(255, 75, 75, 0.2);
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.3);
        margin-top: 20px;
        animation: fadeIn 0.5s ease-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10s); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_html=True)

# --- CONTENIDO DE LA PÁGINA ---

# Título de la aplicación
st.markdown("<h1 class='titulo-principal'>30 de Julio</h1>", unsafe_html=True)
st.markdown("<hr style='border-color: rgba(255,255,255,0.1);'>", unsafe_html=True)

# Tarjeta visual con tu mensaje sincero
st.markdown(
    "<div class='tarjeta-mensaje'>"
    "<p>Te he hecho este detalle aunque sé que es cutre y malísimo hecho, "
    "te lo he hecho porque nunca te olvidas de mí, me alegras los días y me has "
    "sacado risas, eres increíble la verdad y perdón por un detalle tan mierda.</p>"
    "</div>", 
    unsafe_html=True
)

st.write("") # Espacio de separación

# Botón interactivo ocupando el ancho del móvil
if st.button("✨ Mostrar Sorpresa ✨", type="primary", use_container_width=True):
    
    st.markdown("<hr style='border-color: rgba(255,255,255,0.1);'>", unsafe_html=True)
    
    # Bloque de la sorpresa estilizado
    st.markdown(
        "<div class='caja-sorpresa'>"
        "<h3 style='text-align: center; color: #ff6b6b; margin-top:0;'>30 de Julio - Especial para Ti</h3>"
        "<div style='background-color: #2e7d32; color: white; padding: 10px; border-radius: 5px; text-align: center; font-weight: bold; margin-bottom: 20px;'>"
        "🔓 ACCESO CONCEDIDO"
        "</div>"
        "<h4 style='color: #fff; margin-bottom: 15px;'>💕 ¡Feliz día de la amistad chinita!</h4>"
        "<p style='font-size: 1.1rem; color: #e0e0e0; font-style: italic;'>Eres la mejor amiga que se puede tener.</p>"
        "<hr style='border-color: rgba(255,255,255,0.15); margin: 15px 0;'>"
        "<p style='font-size: 1.1rem; color: #e0e0e0;'>🤭 <b>No te puedes morir nunca</b> porque me tienes que mantener...</p>"
        "<p style='font-size: 1.1rem; color: #e0e0e0; margin-top: 10px;'>❤️ Y siempre que estés mal <b>puedes acudir a mí</b> porque me importas.</p>"
        "</div>",
        unsafe_html=True
    )

