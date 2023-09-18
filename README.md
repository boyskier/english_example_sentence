# Vocabulary Example Sentence Generator

## Overview

This Python script automatically generates example sentences for given vocabulary words. The script uses the OpenAI GPT-3.5 Turbo model to create sentences. It reads and writes to a CSV file and updates it with the generated examples.

## System Requirements

- Windows OS
- Python 3.x
- Pandas library
- OpenAI Python package
- dotenv library

## Installation

1. Install Python 3.x: [Download](https://www.python.org/downloads/windows/)

2. Install required packages:
    ```bash
    pip install pandas openai python-dotenv
    ```

## Setup

1. Create an `.env` file and set your OpenAI API key as follows:
    ```
    OPEN_API_KEY=your-api-key-here
    ```

## Usage

1. Place your vocabulary list in a CSV file with columns: `'단어', '예문'`.

2. Run the script:
    ```bash
    python main.py
    ```

3. The script will update the CSV file with generated example sentences.

## Functions

- `generate_example_sentence(word, model)`: Generates example sentences for a given word.
- `try_five_times(func)`: A decorator that retries a function up to 5 times if it encounters an exception.
- `make_complete_vocab_list(input_path, output_path)`: Fills in example sentences for the vocabulary in the given CSV file.
