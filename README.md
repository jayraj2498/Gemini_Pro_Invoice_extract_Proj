# Gemini_Pro_Invoice_extract_Proj


## Description

The Gemini Image Demo is a Streamlit web application that utilizes Google's Gemini Pro Vision API to analyze and understand invoice images. Users can upload an image of an invoice, and the application will provide insights and answers based on the content of the uploaded image.

## Features

- Upload an image of an invoice in JPG, JPEG, or PNG format.
- Use Google's Gemini Pro Vision API to analyze the image.
- Display the analysis results and insights on the web page.

## Requirements

- Python 3.9+
- Anaconda or a virtual environment
- Google Gemini Pro Vision API key

## Setup

1. **Clone the repository:**

2. **Create a virtual environment:**

    Using Anaconda:

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the environment variables:**

    Create a `.env` file in the project root directory and add your Google Gemini Pro Vision API key:
    ```
    GOOGLE_API_KEY=your_google_api_key_here
    ```

## Usage

1. **Run the Streamlit application:**

    ```sh
    streamlit run app.py
    ```

2. **Open the application in your browser:**

    Go to `http://localhost:8501` to access the application.

3. **Upload an invoice image:**

    - Enter a prompt in the input box.
    - Upload an image in JPG, JPEG, or PNG format.
    - Click the "Tell me about the image" button to analyze the image.

## Troubleshooting

### Common Issues

1. **403 Forbidden Error:**

    - Ensure your Google API key is correct and has the necessary permissions.
    - Check for any rate limits imposed by the API and try again after some time.
    - Verify that the file size and format are within the accepted limits.

### Debugging Tips

- Check the console logs for any error messages.
- Use the network inspector in your browser's developer tools to inspect the failed request and see the response headers and error messages.


