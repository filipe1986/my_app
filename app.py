import streamlit as st

st.header('Flipping a coin')

# adding the slider and button to the program:

number_of_trials = st.slider('Number of try?', 1, 1000, 10)

start_button = st.button('Run')

if start_button:
    st.write(f'Executing the experiment with {number_of_trials} tryes.')



st.write('still not as app. We are working on it.')


