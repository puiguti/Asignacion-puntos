import streamlit as st
import random

st.set_page_config(page_title="Asignación de Puntos", layout="centered")

st.title("🎯 Asignación aleatoria de puntos")

# Entrada de nombres
names_input = st.text_area(
    "Escribe un nombre por línea",
    placeholder="Ejemplo:\nAna\nPedro\nMaría"
)

# Número de puntos
k = st.number_input("Número de puntos (k)", min_value=1, value=3, step=1)

# Botón para asignar
if st.button("Asignar"):
    names = [n.strip() for n in names_input.split("\n") if n.strip()]
    if not names:
        st.warning("⚠️ Debes ingresar al menos un nombre")
    else:
        assignments = {name: random.randint(1, k) for name in names}
        st.success("✅ Asignación completada")

        # Mostrar resultados
        for name, point in assignments.items():
            st.write(f"**{name}** → Punto {point}")

# Botón para reiniciar (recarga la app)
if st.button("Reiniciar"):
    st.experimental_rerun()