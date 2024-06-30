import streamlit as st
import pandas as pd

# Cargar el archivo de Excel
file_path = 'Presupuesto Corte Laser OK.xlsx'
data = pd.read_excel(file_path, sheet_name=None)

# Asumimos que la hoja principal es la primera
main_sheet_name = list(data.keys())[0]
df = data[main_sheet_name]

# Título de la app
st.title('Presupuesto para Corte y Grabado Láser')

# Seleccionar el tipo de trabajo
tipo_trabajo = st.selectbox('Selecciona el tipo de trabajo', df['Tipo de Trabajo'].unique())

# Filtrar los datos según la selección
filtered_df = df[df['Tipo de Trabajo'] == tipo_trabajo]

# Mostrar los datos filtrados
st.write(filtered_df)

# Calcular el presupuesto (ejemplo básico)
if not filtered_df.empty:
    st.subheader('Presupuesto Estimado')
    costo_total = filtered_df['Costo'].sum()
    st.write(f'El costo total estimado es: ${costo_total:.2f}')

# Guardar el archivo como Excel
@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

csv = convert_df(filtered_df)

st.download_button(
    label="Descargar Presupuesto como CSV",
    data=csv,
    file_name='presupuesto.csv',
    mime='text/csv',
)

# Ejecutar la app con: streamlit run app.py
