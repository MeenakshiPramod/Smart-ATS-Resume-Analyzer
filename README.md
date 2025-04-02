# Smart-ATS-Resume-Analyzer

# Smart ATS Resume Analyzer

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-orange)](https://share.streamlit.io/your_streamlit_app_url)  (Replace with your Streamlit URL)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

This project is a Streamlit application that leverages the power of Google's Gemini 1.5 Flash model to analyze resumes against job descriptions. It helps job seekers improve their resumes by identifying missing keywords, calculating a job description match percentage, and generating a tailored profile summary.

## Table of Contents

- [Features](#features)
- [Screenshots/Videos](#screenshotsvideos)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)
- [Disclaimer](#disclaimer)

## Features

*   **Resume Upload:** Allows users to upload their resumes in PDF format.
*   **Job Description Input:** Provides a text area for users to paste the job description.
*   **Job Description Match Percentage:** Calculates the percentage of keywords and skills in the resume that match the job description.
*   **Missing Keyword Identification:** Identifies key skills and keywords missing from the resume based on the job description.
*   **Tailored Profile Summary:** Generates a concise and compelling professional summary tailored to the job description.
*   **User-Friendly Interface:**  Built with Streamlit for an intuitive and easy-to-use experience.
*   **Gemini 1.5 Flash Integration:**  Uses Google's advanced language model for accurate and insightful analysis.
*   **Regular Expression Parsing:** Uses regular expression to parse the response from Gemini model
*   **Clear Output Format:** Presents the analysis results in a clear and readable format.

## Screenshots/Videos


![SmartATS1](https://github.com/user-attachments/assets/e34e7ea2-9ae6-4698-939d-14cefdc37a39)

<img width="1279" alt="SmartATS2" src="https://github.com/user-attachments/assets/ff5e13f9-b655-456d-a036-9985f7e3f715" />

https://github.com/user-attachments/assets/a78d905e-7ce5-44a0-832b-85139d80a57b


## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your_username/smart-ats-resume-analyzer.git
    cd smart-ats-resume-analyzer
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Set up your environment variables:**

    *   Create a `.env` file in the root directory of the project.
    *   Add your Gemini API key to the `.env` file:

        ```
        API_KEY=YOUR_API_KEY
        ```

    *   Replace `YOUR_API_KEY` with your actual Gemini API key.  You can obtain an API key from the [Google AI Studio](https://makersuite.google.com/).

2.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    (Assuming your main script is called `app.py`. If it's called something else, change the command accordingly)

3.  **Access the application in your browser:**

    *   Open your web browser and go to the address displayed in the terminal (usually `http://localhost:8501`).

4.  **Use the application:**

    *   Paste the job description into the text area.
    *   Upload your resume in PDF format.
    *   Click the "Analyze" button.
    *   Review the analysis results displayed below.

## Environment Variables

The following environment variables are required to run the application:

*   `API_KEY`: Your Google Gemini API key.

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Push your changes to your forked repository.
5.  Submit a pull request to the main repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

*   This project utilizes the [Streamlit](https://streamlit.io/) framework for building the user interface.
*   The core analysis is powered by [Google's Gemini 1.5 Flash model](https://ai.google.dev/).
*   [PyPDF2](https://pypdf2.readthedocs.io/en/3.0.0/) is used for reading and extracting text from PDF files.
*   [python-dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables.

## Disclaimer

This application provides an analysis of your resume based on the provided job description.  It is intended to be a helpful tool for improving your resume, but it does not guarantee job interviews or employment.  The accuracy of the analysis depends on the quality of the job description and the Gemini model's capabilities.  Use this tool as a guide and always carefully review your resume before submitting it to potential employers.
