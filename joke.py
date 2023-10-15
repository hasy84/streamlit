import streamlit as st
import requests

if "jokes" not in st.session_state:
    st.session_state["jokes"] = []

st.header("joke")
if st.button("何か面白い事を言ってください"):
    r = requests.get("https://official-joke-api.appspot.com/jokes/random")
    d = r.json()
    st.session_state.jokes.append({"role": "user", "content": d["setup"]})
    st.session_state.jokes.append({"role": "assistant", "content": d["punchline"]})

for joke in st.session_state.jokes:
    with st.chat_message(joke["role"]):
        st.write(joke["content"])
    # with st.chat_message("assistant"):
    #     st.write(joke["content"])



