import streamlit as st

# Definición de la función para calcular el presupuesto
def calcular_presupuesto(material, ancho, alto, tiempo, margen_ganancia):
    costos_materiales = {
        'MDF 3 mm': 0.384615,
        'MDF 5,5 mm': 0.534188,
        'MDF 9 mm': 0.747863,
        'MDF Blanco': 0.641026,
        'Acrilico': 8.547009
    }
    costo_minuto = 722.916667
    costo_material = costos_materiales.get(material, 0) * (ancho * alto) / 10000
    costo_operacion = tiempo * costo_minuto
    costo_total = costo_material + costo_operacion
    precio_venta = costo_total * (1 + margen_ganancia)
    return {
        'Costo del Material': costo_material,
        'Costo de Operación': costo_operacion,
        'Costo Total': costo_total,
        'Precio de Venta': precio_venta
    }

st.title('App de Presupuesto para Corte y Grabado Láser')

# Selección del material
material = st.selectbox('Selecciona el material', ['MDF 3 mm', 'MDF 5,5 mm', 'MDF 9 mm', 'MDF Blanco', 'Acrilico'])

# Entrada de dimensiones y tiempo
ancho = st.number_input('Ancho (cm)', min_value=0.0, step=0.1)
alto = st.number_input('Alto (cm)', min_value=0.0, step=0.1)
tiempo = st.number_input('Tiempo (min)', min_value=0, step=1)

# Selección del margen de ganancia
margen_ganancia = st.selectbox('Margen de Ganancia', [0.3, 0.5, 1.0])

# Botón para calcular el presupuesto
if st.button('Calcular Presupuesto'):
    resultado = calcular_presupuesto(material, ancho, alto, tiempo, margen_ganancia)
    st.write('**Costo del Material:**', round(resultado['Costo del Material'], 2))
    st.write('**Costo de Operación:**', round(resultado['Costo de Operación'], 2))
    st.write('**Costo Total:**', round(resultado['Costo Total'], 2))
    st.write('**Precio de Venta:**', round(resultado['Precio de Venta'], 2))
