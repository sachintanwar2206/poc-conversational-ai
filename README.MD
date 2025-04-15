# Project: POC Conversational AI

This repository contains a proof of concept (POC) for building a conversational AI application using Python. The project demonstrates how to create APIs that can be utilized by conversational AI services like **ElevenLabs** and **VAPI** using **FastAPI** and **Supabase**.

## Features

- FastAPI endpoints designed to interact with **ElevenLabs** and **VAPI**.
- Database operations using **Supabase** for storing and retrieving data.
- Modular and scalable codebase.

## Prerequisites

- Python 3.8 or higher
- Virtual environment (optional but recommended)
- Supabase account and project

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sachintanwar2206/poc-conversational-ai.git
    cd poc-conversational-ai
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the .env file with your Supabase credentials:
    ```env
    SUPABASE_URL=<your-supabase-url>
    SUPABASE_KEY=<your-supabase-key>
    ```

## Usage

1. Run the application:
    ```bash
    uvicorn main:app --reload
    ```

2. Use the endpoints to interact with **ElevenLabs** and **VAPI**.

## Project Structure

```
poc-conversational-ai/
├── main.py               # Entry point of the application
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
└── README.md             # Project documentation
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [Supabase](https://supabase.com/)
- [ElevenLabs](https://elevenlabs.io/)
- [VAPI](https://vapi.ai/)
