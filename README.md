# FastAPI API Template 🚀

Welcome to the FastAPI Template project! This repository provides a simple yet powerful template for building APIs with Python using FastAPI. It's designed to be easy to set up and scale for your projects. 🌱

# Features ✨

- **FastAPI**: The core framework for building fast APIs with Python.
- **uv**: A package manager to manage dependencies and create a virtual environment.
- **Pydantic Validation**: Validation of request data using Pydantic models.
- **Swagger UI**: Built-in interactive API documentation with Swagger UI.

# Requirements 📋

- Python 3.12+ 🐍
- uv package manager 🔧

# Installation 🔧

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/fastapi-api-template.git
    cd fastapi-api-template
    ```

2. Install the dependencies using `uv`:

    If you haven't already installed `uv`, you can install it via pip:

    ```bash
    pip install uv
    ```

3. Create and sync the virtual environment:

    ```bash
    uv sync
    ```

4. Activate the virtual environment:

    On Linux/macOS:

    ```bash
    source .venv/bin/activate
    ```

5. Run the application:

    To start the API, run `main.py`:

    ```bash
    python main.py
    ```

    The API will be available at `http://localhost:8000`.

    - For API documentation, go to: `http://localhost:8000/docs` 📜
    - For ReDoc documentation: `http://localhost:8000/redoc` 📖

# Contributing 🤝

We welcome contributions to improve this project! Please fork the repository, create a branch, and submit a pull request.

- Make sure to follow the existing code style for consistency.

# License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.