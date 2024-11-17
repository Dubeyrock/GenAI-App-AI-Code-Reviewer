import streamlit as st
import google.generativeai as genai
import time

# Configure API
genai.configure(api_key="AIzaSyAPPjQz0sJ800CX6hFdllcRxNUaldL4HIQ")

# Set system prompt for model
sys_prompt = '''You are a friendly and helpful code review assistant. You analyze Python code and provide:
                1. Bug Report
                2. Fixed Code Snippet
                3. Explanation & Suggestions
You are also able to answer code-related questions in a conversational, friendly manner.'''

# Initialize model
model = genai.GenerativeModel("models/gemini-1.5-flash", system_instruction=sys_prompt)

# UI Design
st.header(":blue[AI] Code Reviewer 🧑‍💻💬", divider=True)

# File Upload Option
uploaded_file = st.file_uploader("📁 Upload Python Code File", type=["py"])
if uploaded_file is not None:
    ex_code = uploaded_file.read().decode("utf-8")
else:
    ex_code = st.text_area(" 💻 Enter Python Code:", placeholder="Paste your code here...")

# Submit button for code review
if st.button(" 🔍 Generate Review"):
    st.divider()
    if ex_code:
        with st.spinner("Reviewing your code... Please wait!"):
            time.sleep(1)  # Simulate processing time
            response = model.generate_content(ex_code)

            # Display Code Review Results
            st.header("🕒💬 Code Review Results:")

            # Bug Report
            with st.expander("Bug Report"):
                bug_report = response.text.split('Fixed Code Snippet:')[0]
                st.markdown(f"** 🐞 Bug Report:**\n{bug_report}")

            # Fixed Code Snippet
            with st.expander("🔧 Fixed Code Snippet"):
                fixed_code = response.text.split('Fixed Code Snippet:')[1].split('Explanation and Suggestions:')[0]
                st.code(fixed_code, language='python')

            # Suggestions and Explanation
            with st.expander("💡 Suggestions & Explanation"):
                if 'Explanation and Suggestions:' in response.text:
                    suggestions = response.text.split('Explanation and Suggestions:')[1]
                else:
                    suggestions = "No suggestions or explanations available."
                st.markdown(f"**Suggestions:**\n{suggestions}")

# Query Box for User (Chatbot-like behavior)
st.divider()
st.subheader("❓ Ask a Query to the Chatbot:")

# Initialize chat history in session state if not already
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Display previous chat history (if any)
for message in st.session_state.chat_history:
    st.markdown(f"**{message['role']}:** {message['text']}")

# Query input box for user to ask a question
user_query = st.text_area("💬 Type your question here:", placeholder="Ask a question about your code...")

# Handle user query submission
if st.button("Submit Query"):
    if user_query:
        # Add user query to chat history
        st.session_state.chat_history.append({"role": "User", "text": user_query})

        with st.spinner("Generating chatbot response..."):
            time.sleep(1)  # Simulate processing time
            
            # Get chatbot response
            query_response = model.generate_content(user_query)
            
            # Add chatbot response to chat history
            st.session_state.chat_history.append({"role": "Bot", "text": query_response.text})

            # Display the response
            st.markdown(f"**Bot says:**\n{query_response.text}")

# Footer with credit
st.markdown("---")
st.caption("Built with ❤️ by **Shivam Dubey** | Powered by Generative AI | Built using Streamlit")
