import streamlit as st
from streamlit.logger import get_logger
from wikiList import portmanteaus
import random

LOGGER = get_logger(__name__)


def run():

    st.header(':rainbow[Portmanteaus]')
    st.text('What happens when two words become one')
    st.markdown('*A game by Akihito Gorai*')
    st.divider()
    
    gamemodes = ['Roots', 'Branches', 'Fruits']
    st.radio('Select gamemode', gamemodes, key='mode')
    # st.write(st.session_state)
    st.divider()
    
    if 'topic' not in st.session_state:
        st.session_state["topic"] = random.choice(list(portmanteaus))
    if 'word' not in st.session_state:
        st.session_state["word"] = random.choice(list(portmanteaus[st.session_state['topic']]))
    
    def roots():
        reset_word_roots = st.button('New word')
        if reset_word_roots:
            st.session_state["topic"] = random.choice(list(portmanteaus))
            st.session_state["word"] = random.choice(list(portmanteaus[st.session_state['topic']]))
        root1 = portmanteaus[st.session_state["topic"]][st.session_state["word"]][0]
        root2 = portmanteaus[st.session_state["topic"]][st.session_state["word"]][1]
        root1L = root1.lower()
        root2L = root2.lower()
        st.title('Word: ' + ':green[' + st.session_state["word"] + ']')
        st.subheader('Topic: ' + ':green[' + st.session_state["topic"] + ']')
        st.title('Guess the root words')
    
        guess1 = st.text_input('First word').lower()
        guess2 = st.text_input('Second word').lower()
    
        submit_guesses = st.button('Submit your guesses')
        if submit_guesses:
            if guess1 is '' or guess2 is '':
                st.text('Please fill all text fields')
            else:
                if guess1 == root1L and guess2 == root2L:
                    st.title(':rainbow[Correct!]')
                    st.link_button(':blue[Definition and background]', f'https://en.wikipedia.org/wiki/{st.session_state["word"]}')
                else:
                    st.title('Incorrect')
                    if guess1 == root1L:
                        st.markdown(':orange[' + root1 + ']' + ' is correct')
                    else:
                        st.markdown(':red[' + guess1 + ']' + ' is incorrect')
    
                    if guess2 == root2L:
                        st.markdown(':orange[' + root2 + ']' + ' is correct')
                    else:
                        st.markdown(':red[' + guess2 + ']' + ' is incorrect')
    
        ans_reveal = st.button('Reveal the roots', key = 'ans_reveal')
        if st.session_state['ans_reveal']:
            st.markdown('The first root is: ' + ':orange[' + root1 + ']')
            st.markdown('The second root is: ' + ':orange[' + root2 + ']')
            st.link_button(':blue[Definition and background]', f'https://en.wikipedia.org/wiki/{st.session_state["word"]}')
    
    def branches():
        reset_word_roots = st.button('New word')
        if reset_word_roots:
            st.session_state["topic"] = random.choice(list(portmanteaus))
            st.session_state["word"] = random.choice(list(portmanteaus[st.session_state['topic']]))
        root1 = portmanteaus[st.session_state["topic"]][st.session_state["word"]][0]
        root2 = portmanteaus[st.session_state["topic"]][st.session_state["word"]][1]
        root1L = root1.lower()
        root2L = root2.lower()
        st.title('Roots: ' + ':green[' + root1 + ']' + ' and ' + ':green[' + root2 + ']')
        st.subheader('Topic: ' + ':green[' + st.session_state["topic"] + ']')
        st.title('Guess the portmanteau (combination of root words)')
        guess1 = st.text_input('').lower()
    
        if guess1 is '':
            print('waiting')
        else:
            if guess1 == st.session_state["word"].lower():
                st.title(':rainbow[Correct!]')
                st.link_button(':blue[Definition and background]', f'https://en.wikipedia.org/wiki/{st.session_state["word"]}')
            else:
                st.markdown(':red[Incorrect]')
        ans_reveal = st.button('Reveal the answer', key = 'ans_reveal')
        if st.session_state['ans_reveal']:
            st.title(':orange[' + st.session_state["word"] + ']')
            st.link_button(':blue[Definition and background]', f'https://en.wikipedia.org/wiki/{st.session_state["word"]}')
    
    def fruits():
        st.title(':green[Input your own words to form a new portmanteau!]')
        root1 = st.text_input('First word')
        root2 = st.text_input('Second word')
        if st.button('Generate Portmanteau'):
            if root1 != '' and root2 != '':
                index1 = random.randint(1,len(root1))
                index2 = random.randint(0,len(root2))
                lst1 = []
                lst2 = []
                for letter in root1:
                    lst1.append(letter)
                for letter in root2:
                    lst2.append(letter)
                
                half1 = ''.join(lst1[0:index1])
                half2 = ''.join(lst2[index2:len(root2)])
    
                st.title(':rainbow['+ half1+half2+ ']')
    
                # st.text(index1)
                # st.text(index2)
                
                # st.text(half1)
                # st.text(half2)
            else:
                st.text('Please fill all text fields')
    
    if st.session_state['mode'] == 'Roots':
        roots()
    
    if st.session_state['mode'] == 'Branches':
        branches()
    
    if st.session_state['mode'] == 'Fruits':
        fruits()

if __name__ == "__main__":
    run()
