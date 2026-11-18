import streamlit as st
import mysql.connector

# Título de la aplicación web
st.title("🌟 Astronomía DB - Panel de Visitantes")
st.write("Bienvenido a la aplicación web conectada a nuestra base de datos MySQL.")

# Configuración de tu base de datos
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "31032006",
    "database": "astronomia_db"
}

try:
    # Conexión
    conexion = mysql.connector.connect(**db_config)
    if conexion.is_connected():
        st.success("¡Conexión exitosa a la base de datos astronomia_db!")
        
        # Consultar los datos
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM visitante;")
        resultados = cursor.fetchall()
        
        st.subheader("📋 Lista de Visitantes Registrados")
        
        # Mostrar los datos de forma limpia en la página web
        for fila in resultados:
            st.info(f"**ID:** {fila[0]} | **Nombre:** {fila[1]} | **Correo:** {fila[2]} | **Tipo:** {fila[3]}")

except mysql.connector.Error as error:
    st.error(f"Error al conectar con la base de datos: {error}")

finally:
    if 'conexion' in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()