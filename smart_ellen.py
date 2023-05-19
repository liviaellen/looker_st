import streamlit as st
import openai

"""# Smart Ellen """
text_input = st.text_input('Ask me anything', "Write a paragraph about a guy named mike who moves to bali to study data analytics in a coding bootcamp who just celebrate his birthday")

#openai.api_key = os.getenv("OPENAI_API_KEY")



if st.button("Ask"):
    openai.api_key=st.secrets["API_KEY"]
    try:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text_input,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        if response['choices'][0].text == "":

            st.write("Sorry, I don't know that one.")
            st.write("Error message: ")
            st.write(response)
        else:
            st.write(response['choices'][0].text)
    except Exception as e:
        st.write(e.message)
        st.write(e.args)
