# Python Project

This project is designed to create two text files containing arrays of odd and even numbers.

## Project Structure

```
python-project
├── src
│   ├── main.py          # Contains the main logic of the program
├── requirements.txt     # Lists the dependencies required for the project
├── .gitignore           # Specifies files and directories to be ignored by Git
├── README.md            # Documentation for the project
└── venv/                # Python virtual environment directory
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd python-project
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install dependencies**:
   If there are any dependencies listed in `requirements.txt`, install them using:
   ```
   pip install -r requirements.txt
   ```

## Running the Project

To run the program, execute the following command:
```
python src/main.py
```

This will generate two files: `odd.txt` containing odd numbers and `even.txt` containing even numbers.