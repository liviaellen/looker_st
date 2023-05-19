import streamlit as st
import openai

"""# Smart Ellen "
text_input = st.text_input('Ask me anything', "Write a paragraph about a guy named mike who moves to bali to study data analytics in a coding bootcamp who just celebrate his birthday")

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key ="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"
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=text_input,
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

st.write(response['choices'][0].text)
