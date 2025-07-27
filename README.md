# Mort-E-Mail

This project is a Python-based application that generates and sends daily personalized emails containing weather forecasts, historical facts, and holiday information.

## Services

### `main.py`
This is the main script that orchestrates the entire process. It fetches data from various modules, generates a JSON response using a language model, builds an HTML email, and sends it.

### `prompt_functions.py`
This module contains functions to interact with the Gemini API. It sends prompts to the AI and returns the generated text. It also manages the conversation history.

### `weather.py`
This module fetches the 7-day weather forecast from the Open-Meteo API for a given latitude and longitude. It returns a dictionary containing today's and the week's weather information.

### `check_holidays.py`
This module checks for public holidays in India for a given date using the `holidays` library.

### `email_functions.py`
This module handles sending emails. It supports both plain text and HTML emails using `smtplib` and Gmail's SMTP server. It also includes a function to read a mailing list from `mailing_list.txt`.

### `image_generation.py`
This module uses the Gemini API to generate an image based on a given prompt and saves it to the `generated_images` folder.

### `mailing_list.txt`
This file contains the list of email addresses to which the emails will be sent. Each email address should be on a new line. This file is included in the `.gitignore` to ensure it remains private.


## How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/mort-e-mail.git
    cd mort-e-mail
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv myenv
    ```

3.  **Activate the virtual environment:**
    -   On Windows:
        ```bash
        myenv\Scripts\activate
        ```
    -   On macOS/Linux:
        ```bash
        source myenv/bin/activate
        ```

4.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: A `requirements.txt` file is not present in the repository. You will need to create one based on the imports in the Python files. The necessary libraries are `requests`, `google-generativeai`, `Pillow`, and `holidays`)*

5.  **Set up environment variables:**
    You need to set the following environment variables:
    -   `GEMINI_API_KEY`: Your API key for the Gemini API.
    -   `GMAIL_FROM_ADDRESS`: Your Gmail address for sending emails.
    -   `GMAIL_PASSWORD`: Your Gmail password or an app-specific password.

6.  **Run the main script:**
    ```bash
    python main.py
    ```
This will generate and send the email. You can also run `chat.py` for a simple chat session with the AI.