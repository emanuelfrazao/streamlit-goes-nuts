# modules
import streamlit as st
import pandas as pd

# page
st.title('flumsy')

# sidebar
with st.sidebar:
    st.title('This is a sidebar')
    st.text('This is a picture loaded from the web.')
    st.image('https://static.streamlit.io/examples/cat.jpg', width=300)

# main content
st.subheader('This is a subheader with a divider', divider='rainbow')
st.write('This is text.')
'This will also be shown.'
x = 'This will not be shown.'
x # except if you explicitly write it

st.markdown('## This is markdown.')
st.markdown('### This is also markdown.')
st.markdown("""
This is markdown with
- a list
- of items
""")

st.subheader('Queer text', divider='rainbow')
## code
with st.echo():
    x = "This is printed as code"

## party
st.success("This is a success!")
st.info("This is an info message.", icon='🫠')
st.error("Or else, failure! — hurray!")

st.subheader('Data', divider='rainbow')
def create_dataframe():
    print('creating dataframe...')
    return pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    })

df = create_dataframe()
st.write('This is a dataframe (being):')
st.table(df)

##### WIDGETS
st.subheader('Widgets and inputs', divider='rainbow')
st.radio('Here are some radio buttons', [1, 2, 3], help='This is a help text')
st.radio('Here are more, starting at second', 'abc', index=1, horizontal=True)
st.checkbox('Here is a checkbox')
st.selectbox('Here is a select box', [1, 2, 3])
st.multiselect('Here is a multiselect', [1, 2, 3])
st.slider('Here is a slider', 0, 10)
st.slider('Here is a range slider', 0, 10, (3, 7))
st.text_input('Here is a text input')
st.number_input('Here is a number input')
st.text_area('Here is a text area')
st.date_input('Here is a date input')
st.time_input('Here is a time input')
st.file_uploader('Here is a file uploader')
st.color_picker('Here is a color picker')
st.button('Here is a button')


##### STATE
st.subheader('Stateful, always', divider='rainbow')

count = 0
increment = st.button('Keep adding', key='bad_counter')
if increment:
    count += 1
st.write('Count = ', count)

st.text("Now properly:")
count_stateful = st.session_state.get('count', 0)
increment = st.button('Keep adding', key='good_counter')
if increment:
    count_stateful += 1
    st.session_state['count'] = count_stateful
st.write('Count = ', count_stateful)

st.text("Better yet:")
if 'nice_count' not in st.session_state:
    st.session_state.nice_count = 0

def increment_counter():
    st.session_state.nice_count += 1
st.button('Keep adding', on_click=increment_counter)
st.write('Count = ', st.session_state.nice_count)

##### CONDITIONAL ACTIONS
st.subheader('Conditional actions', divider='rainbow')

st.checkbox('Show me the goods', key='checkbox')
if st.session_state.checkbox:
    st.write('Checkbox is checked')


if 'show_after' not in st.session_state:
    st.session_state.show_after = False

def show_after():
    st.session_state.show_after = True
    
st.button('Show me the goods', on_click=show_after)

if st.session_state.show_after:
    st.write('You have seen this after clicking the button.')
    
if 'show_or_not' not in st.session_state:
    st.session_state.show_or_not = False
def show_or_not():
    st.session_state.show_or_not = not st.session_state.show_or_not
st.button('Hit me again', on_click=show_or_not)
if st.session_state.show_or_not:
    st.write('Hello')
else:
    st.write('Goodbye')
    

    
