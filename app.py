import streamlit as st
import pandas as pd
import numpy as np
import random

# Título
st.title("CombatCoach")

# Descripción
st.markdown("CombatCoach es tu compañero definitivo para el entrenamiento de boxeo y MMA. Nuestra aplicación te ofrece un plan de entrenamiento personalizado que se adapta a tu masa corporal y a tus intereses personales en el mundo de las artes marciales mixtas. Con CombatCoach, obtendrás un plan de entrenamiento diseñado específicamente para ti, lo que significa que puedes maximizar tus resultados y alcanzar tus metas de acondicionamiento físico de manera eficaz. Ya sea que seas un principiante o un luchador experimentado, CombatCoach tiene un plan perfecto para ti. ¡Prepárate para mejorar tus habilidades y alcanzar un nivel superior en el boxeo y MMA con CombatCoach!")


formulario = st.form
with formulario("Formulario"):
    # Agregamos un subtítulo al formulario
    st.subheader("Complete todos los campos")

    # Dividimos la interfaz en dos columnas
    col1, col2 = st.columns(2)

    # Recopilamos la entrada del usuario, incluyendo nombre, apellido, correo y contraseñas
    p_nombre = col1.text_input("Primer nombre")
    p_apellido = col2.text_input("Primer apellido")
    correo = st.text_input("Correo electrónico")
    edad = col1.text_input("Edad")+ " Años"
    peso = col2.text_input("Peso en KG")+ " KG"
    altura = col1.text_input("Altura en CM")+ " CM"
    # Proximamente ms opciones
    intereses = col2.selectbox("Selecciona tu interes en la aplicacion",["Boxeo","Muay thai"])
    acepta_politicas = st.checkbox(
        "Acepto las políticas de tratamiento de datos personales"
    )

    # Agregamos un botón de envío
    boton = st.form_submit_button("Registrarse")
    
politica_text = """
# Política de Tratamiento de Datos Personales

## 1. Introducción

Esta Política de Tratamiento de Datos Personales describe cómo CombatCoach recopila, utiliza, almacena y protege la información personal que proporcionas a través de nuestra aplicación. Esta Política se aplica a todos los usuarios de la Aplicación CombatCoach.

## 2. Información Personal que Recopilamos

Recopilamos información personal que tú proporcionas voluntariamente cuando utilizas la Aplicación de CombatCoach. Esta información puede incluir, entre otros:

- Nombre y apellidos.
- Dirección de correo electrónico.
- Información de la cuenta, como nombre de usuario y contraseña.
- Masa corporal.
- Intereses en la aplicación.

## 3. Uso de la Información Personal

Utilizamos la información personal que recopilamos para los siguientes propósitos:

- Proporcionar un plan de entrenamiento personalizado basado en tu masa corporal y tus intereses.
- Mejorar la experiencia del usuario en la Aplicación CombatCoach.
- Proteger la integridad y la seguridad de la Aplicación y de nuestros usuarios.

## 4. Consentimiento

Al utilizar la Aplicación CombatCoach, aceptas y consientes el tratamiento de tu información personal de acuerdo con esta Política de Tratamiento de Datos Personales.

## 5. Compartir Información Personal

No compartimos tu información personal con terceros sin tu consentimiento, excepto en los siguientes casos:

- Proveedores de servicios: Podemos compartir tu información con terceros que nos brindan servicios esenciales para la operación de la aplicación, como el cálculo de los planes de entrenamiento.
- Cumplimiento legal: Podemos divulgar tu información personal si estamos obligados por ley o si creemos de buena fe que dicha divulgación es necesaria para cumplir con una obligación legal, proteger nuestros derechos o garantizar la seguridad de nuestros usuarios.

## 6. Seguridad de Datos

Tomamos medidas razonables para proteger tu información personal contra pérdida, acceso no autorizado, divulgación, alteración o destrucción. Sin embargo, ten en cuenta que ninguna transmisión de datos en Internet o sistema de almacenamiento es completamente seguro.

## 7. Derechos del Titular de los Datos

Tienes derechos sobre tus datos personales, que incluyen:

- Corregir tus datos personales.

## 8. Cambios en la Política

Nos reservamos el derecho de actualizar o modificar esta Política en cualquier momento. Te notificaremos sobre los cambios a través de la Aplicación CombatCoach o por otros medios. El uso continuado de la Aplicación después de dichas modificaciones constituye tu aceptación de la Política revisada.

## 9. Contacto

Si tienes preguntas, inquietudes o solicitudes relacionadas con esta Política de Tratamiento de Datos Personales, contáctanos a través de dramirezla@unal.edu.co.

Fecha de entrada en vigor: Noviembre 8 del 2023
"""

# Mostrar la política de tratamiento de datos personales en Markdown
with st.expander("Ver Política de Tratamiento de Datos Personales"):
    st.markdown(politica_text)

if boton:
    datos_usuario = np.asarray([p_nombre, p_apellido, correo, edad, peso, altura, intereses])
    if p_nombre == "" or p_apellido == "" or correo == "" or edad == "" or peso == "" or altura == "" or intereses == "" or acepta_politicas == False:
        st.write("Complete todos los campos por favor")
    else: 
        st.write("Tus datos son los siguientes: ")
        st.write(datos_usuario)
    
# Calculadora de combinaciones
golpes_boxeo = ["jap","recto","cruzado izquierdo","cruzado derecho","uppercut izquierdo","uppercut derecho","cambio de guardia"]
golpes_muay_thai = golpes_boxeo + ["codazo izquierdo","codazo derecho","rodillaso izquierdo","rodillaso derecha","patada lower frontal","patada media frontal","patada alta frontal","patada lower trasera","parada media trasera","patada alta trasera"]

def generar_combinaciones(intereses, longitud):
    golpes_disponibles = golpes_boxeo if intereses == "boxeo" else golpes_muay_thai
    combinaciones = []

    if longitud < 1:
        return combinaciones

    def generar_combinacion(actual_combinacion, restantes):
        if len(actual_combinacion) == longitud:
            combinaciones.append(" - ".join(actual_combinacion))
            return

        for golpe in golpes_disponibles:
            if not actual_combinacion or actual_combinacion[-1] != golpe:
                generar_combinacion(actual_combinacion + [golpe], restantes - 1)

    generar_combinacion([], longitud)
    return combinaciones

st.title("Calculadora de Combinaciones de Golpes")

longitud = st.slider("Longitud de la combinación", 1, 5)

if st.button("Generar Combinación Aleatoria"):
    combinaciones = generar_combinaciones(intereses, longitud)
    if combinaciones:
        combinacion_aleatoria = random.choice(combinaciones)
        st.write(f"Combinación de {intereses} aleatoria de longitud {longitud}:")
        st.write(combinacion_aleatoria)
    else:
        st.write("No hay combinaciones disponibles para la longitud seleccionada.")
