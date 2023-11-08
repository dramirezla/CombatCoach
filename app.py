import streamlit as st

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
    edad = col1.text_input("Edad")
    peso = col2.text_input("Peso en KG")
    altura = st.text_input("Peso en CM")
    # Proximamente ms opciones
    intereses = st.selectbox("Selecciona tu interes en la aplicacion",["Boxeo","Muay thai"])
    acepta_politicas = st.checkbox(
        "Acepto las políticas de tratamiento de datos personales"
    )

    # Agregamos un botón de envío
    st.form_submit_button("Registrarse")
    
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

Si tienes preguntas, inquietudes o solicitudes relacionadas con esta Política de Tratamiento de Datos Personales, contáctanos a través de [tu correo electrónico de contacto].

Fecha de entrada en vigor: Noviembre 8 del 2023
"""

# Mostrar la política de tratamiento de datos personales en Markdown
with st.expander("Ver Política de Tratamiento de Datos Personales"):
    st.markdown(politica_text)

st.write(intereses)
