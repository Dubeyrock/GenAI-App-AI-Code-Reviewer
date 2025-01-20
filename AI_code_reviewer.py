# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Importing necessary libraries
import os
import streamlit as st
import google.generativeai as genai 
from streamlit_ace import st_ace  

# Configure GenAI API keys
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# System prompt
sys_prompt = """
You are an expert AI code reviewer integrated into a user-friendly Python application. Your role is to analyze Python code submitted by users and provide the following:

1. ## Bug Report: 
    - Identify potential bugs, syntax errors, and logical flaws in the code.
    - Explain the causes of any errors or bugs clearly.
    - Highlight common issues such as incorrect indentation, missing imports, variable shadowing, etc.
    - If possible, offer explanations of why certain patterns or practices are more reliable.

2. ## Fixed Code:
    - Return fixed or optimized code snippets alongside explanations of the changes made.
    - Suggest alternative approaches for optimizing code and improving performance (e.g., time complexity reduction, better use of built-in functions, etc.).
    - Ensure that the fixed code adheres to Pythonic principles (e.g., list comprehensions, idiomatic error handling, etc.).

3. ## User Guidance:
    - Provide concise, easy-to-understand feedback suitable for developers of varying experience levels.
    - Highlight best practices such as code readability, modularization, and reusability.
    - Offer suggestions on improving code structure, comments, and documentation for better maintainability.
    - Whenever applicable, provide links to relevant documentation or resources to help the user deepen their understanding.

Maintain a professional tone while keeping explanations simple and accessible. Focus on clarity, accuracy, efficiency, and improving the user's understanding of best coding practices. Strive to explain why certain fixes are made and how they enhance the overall functionality and efficiency of the code.
"""

# Function to get response from GenAI
def get_response(sys_prompt, code):
    response = model.generate_content([sys_prompt, code])
    return response.text

# Sidebar for navigation
st.sidebar.title("Navigation")
selected_option = st.sidebar.radio("Go to", ["Code Review", "About the Project"])

# Main content based on selected option in sidebar navigation 
if selected_option == "Code Review":
    # Title of the web app
    st.title(":page_facing_up: An AI Code Reviewer")

    # Subheader for code review
    st.markdown("""
        <style>
            .ace_editor {
                background-color: #002b36;  /* Dark blue background */
                color: #ffffff;  /* White text color */
            }
        </style>
    """, unsafe_allow_html=True)

    # Ace editor for code input
    code = st_ace(
        height=400,
        language='python',
        theme='twilight',  # Or any other theme you prefer
        placeholder='Enter your Python code here...',
        font_size=14,
        key='ace_editor',
        auto_update=True
    )


    # Generate button
    button = st.button("Review Code")

    if button:
        if not code.strip():
            st.error("Please enter some Python code to review.")
        else:
            with st.spinner("Analyzing your code..."):
                try:
                    response = get_response(sys_prompt, code)
                    st.header("Code Review")
                    st.markdown(response)
                except Exception as e:
                    st.error(f"An error occurred: {e}")

elif selected_option == "About the Project":
    # Title of the About section
    st.title("🌟 **About the Project**")

    # Project Overview
    st.markdown("---")
    st.subheader("🌟 Project Overview")
    st.markdown("""
    Welcome to the **AI-Powered Code Reviewer**!  
    This project is designed to simplify coding workflows by identifying bugs, optimizing code, 
    and guiding developers toward best practices with the power of **AI**.
    """)

    # Objective
    st.markdown("---")
    st.subheader("🎯 Objective")
    st.markdown("""
    The **AI Code Reviewer** leverages cutting-edge AI technology to help developers:  
    - 🤖 Identify potential bugs and errors in their Python code.  
    - 🛠️ Provide optimized solutions to improve code efficiency.  
    - 📚 Offer clear, accessible guidance for developers at all skill levels.
    """)

    # Features
    st.markdown("---")
    st.subheader("✨ Features")
    st.markdown("""
    - 🔍 **Bug Identification**: Detect syntax errors, logical flaws, and inefficiencies.  
    - 🔧 **Code Optimization**: Suggest fixes and improvements with detailed explanations.  
    - 🧑‍🏫 **Developer Assistance**: Deliver clear, actionable guidance for better coding.  
    - 🎨 **Interactive UI**: Built with **Streamlit** for a sleek, user-friendly experience.
    """)

    # Technologies Used
    st.markdown("---")
    st.subheader("🛠️ Technologies Used")
    st.markdown("""
    - 🐍 **Python**: Core programming language for implementation.  
    - 🌐 **Streamlit**: Framework for interactive web apps.  
    - 🤖 **Google Generative AI**: Advanced AI for code review.  
    - 🔒 **dotenv**: Ensures secure API key management.
    """)

    # Future Scope
    st.markdown("---")
    st.subheader("🚀 Future Scope")
    st.markdown("""
    - 🌎 **Support for Multiple Programming Languages**: Extend beyond Python for broader use.  
    - 📊 **Advanced Debugging Tools**: Add features like complexity analysis and performance insights.  
    - 🎨 **Enhanced UI Customization**: Improve user experience with better aesthetics and theming.
    """)

    # Closing Note
    st.markdown("---")
    st.markdown("""
    > ### **🎉 Thank you for exploring our project! Your feedback and support mean the world to me.** ✨  
    """)
