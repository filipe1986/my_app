import scipy.stats
import streamlit as st
import time


st.header('Flipping a coin')

chart = st.line_chart([0.5])

def toss_coin(n): # function that emulates the coin toss
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size = n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no

        chart.add_rows([mean])
        time.sleep(0.05)
    
    return mean


# adding the slider and button to the program:
number_of_trials = st.slider('Number of try?', 1, 1000, 10)


start_button = st.button('Run')

if start_button:
    st.write(f'Executing the experiment with {number_of_trials} tryes.')




