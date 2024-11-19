## AI Code Reviewer 🧑‍💻💬

**Objective** 

This project aims to develop a Python application that allows users to submit their Python code for review and receive feedback on potential bugs along with suggestions for fixes. The application should be user-friendly, and efficient, and provide accurate bug reports and fixed code snippets.


A Python application built using Streamlit and Generative AI to review Python code, identify bugs, suggest fixes, and improve performance. This tool provides an interactive code review experience with automatic bug reports and optimized code snippets.

![Screenshot (1489)](https://github.com/user-attachments/assets/5d8ce92b-f924-479f-ab2c-8a2e8c7e8d06)



## Features
- **Bug Report**: Automatically detects issues in Python code.
- **Fixed Code Snippets**: Provides suggestions and corrected code.
- **Explanation & Suggestions**: Offers explanations for errors and recommendations for code optimization.
- **Code Formatting**: Uses `autopep8` for automatic code formatting to follow PEP 8 standards.
- **Test Cases**: The tool is capable of reviewing code with various bugs, including logic errors, syntax issues, undefined variables, and runtime exceptions.

## Technologies Used
- **Python**: The core programming language for the application.
- **Streamlit**: Used for building the web interface.
- **Google Generative AI**: For analyzing code and generating reviews.
- **autopep8**: For automatic Python code formatting.
- **pytest**: To create test cases for the application.
  
## How to Use

1. **Upload Code File**: Click on "Upload Python Code File" and select your `.py` file, or simply paste your code into the text area.
2. **Generate Review**: Click on the "Generate Review" button to analyze the code.
3. **Review Results**: The review will display:
   - **Bug Report**: A summary of issues found in the code.
   - **Fixed Code Snippet**: Suggested code fixes.
   - **Explanation & Suggestions**: Additional improvements and explanations for the code.

## Example Code

Here’s an example of Python code that will be reviewed by the AI Code Reviewer:

```python
def greet(name):
    print("Hello, " + name)

greet("Alice")

``````````
## demo 

https://m2w6epek2n32glgsdbxxvp.streamlit.app/ 

![Screenshot (1492)](https://github.com/user-attachments/assets/50c99a2c-17ca-4a96-8219-78342ec1d0b9)

