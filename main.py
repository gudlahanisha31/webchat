from ollama import chat
import streamlit as s 
s.title("My AI Bot: Synora")
name = "Hanisha"
s.write("Welcome,",name)
question  = s.text_input("Ask a question")
if s.button("Ask"):
    s.write("You asked:" , question)
    response = chat(model = "gemma3:1b",messages = [

        {
            "role": "system",
            "content": "you are a friendly tutor. you explain concepts in a simple way and provide examples to help the user understand."
        },
        {
            "role": "user",
            "content": question

        }
    ])
    answer = response.message.content
    s.write(answer)

#dropdown 
# options = ["C++" , "Java" , "Python"]
# choice = s.selectbox("Select your favourite language" , options)
# s.write(f"you selected {choice}")