import streamlit as st
from backend import generate_combinations
from utils import GetMemberList

def Visible_mode(members):
    members = GetMemberList(members)
    giver, receiver = generate_combinations(members)
    table_formatting = {'Giver': giver,
                        'Receiver': receiver}
    st.table(table_formatting)

def Hidden_mode(members, email):
    st.write('☹️ Sorry, this mode is not available yet.')

st.set_page_config(page_title="Secret Santa", page_icon = "🎅🏻")
st.title('🎅🏻 Secret Santa 🎄')
st.write('This app will allow you to organize the splitting for the secret santa. This is an open-source project, therefore you can contribute visiting our [GitHub page](https://github.com/udicaprio/SecretSanta)')
members = st.text_input(label = 'Add the members name separated by comma (e.g.: Marco, Sivia, Sara)')

mode = st.radio('Mode', ['Visible mode', 'Hidden mode'],
                captions = ['The givers and receivers of the presents are visible to everyone',
                            'An email will be sent to the givers containing the name of their receiver'])

if st.button('Go!', type = 'primary'):
    if mode == 'Visible mode':
        Visible_mode(members)
    elif mode == 'Hidden mode':
        Hidden_mode(members, None)