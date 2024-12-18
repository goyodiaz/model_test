import streamlit as st
from streamlit_modal import Modal

modal = Modal(key="confirmation_modal")
if st.button("Open Pop-up"):
    modal.open()

# Render the modal
if modal.is_open():
    with modal.container():
        st.write("Are you sure you want to proceed?")
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Yes"):
                st.success("You selected Yes!")
                modal.close()

        with col2:
            if st.button("No"):
                st.warning("You selected No!")
                modal.close()
