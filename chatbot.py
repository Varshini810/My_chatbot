import streamlit as st
import google.generativeal as genai

API_KEY=AIzaSyC1uffQAaILHADEwZwskhtqhvwAoVOSeBI"
genai.configure(api_key=API_KEY)
model=genai.GenerativeModel('geminin-1.5-flash')

if "chat" not in st.session_state:
  st.session_state.chat=model.start_chat(history=[])

st.title("chatbot - AI Assistant")
st.write("Welcome to the my chatbot! how can i help you?")

if "messages" not in st.session_state:
  st.session_state.messages=[]
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])
if prompt :=st.chat_input("Say something..."):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_messages("user"):
    st.markdown(prompt)
  response=st.session_state.chat.send_message(prompt)

  st.session_state.messages.append({"role": "assistant", "content": response.text})
  with st.chat_message("assistant"):
    st.markdown(response.text)
