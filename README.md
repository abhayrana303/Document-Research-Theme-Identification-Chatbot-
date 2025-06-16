# Chatbot Project

This project is a web-based chatbot designed to ingest and process over 75 documents, allowing users to ask questions and extract answers with accurate citations. The chatbot also identifies and summarizes common themes across all documents.

## Project Structure

```
chatbot-project
├── src
│   ├── backend
│   │   ├── app.py                  # Main entry point for the backend application
│   │   ├── ingestion
│   │   │   └── document_ingestor.py # Handles document uploading and processing
│   │   ├── processing
│   │   │   ├── qa_engine.py         # Processes user queries and retrieves answers
│   │   │   └── summarizer.py        # Analyzes responses and identifies common themes
│   │   └── utils
│   │       └── citation_helper.py    # Utility functions for citation formatting
│   ├── frontend
│   │   ├── App.jsx                  # Main component for the frontend application
│   │   ├── components
│   │   │   ├── ChatWindow.jsx       # Displays conversation between user and chatbot
│   │   │   └── DocumentUploader.jsx  # Allows users to upload documents
│   │   └── styles
│   │       └── main.css             # Styles for the frontend application
│   └── types
│       └── index.d.ts               # TypeScript types and interfaces
├── public
│   └── index.html                   # Main HTML file for the frontend application
├── package.json                     # Configuration file for npm
├── requirements.txt                 # Python dependencies for the backend
├── tsconfig.json                    # TypeScript configuration file
└── README.md                        # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd chatbot-project
   ```

2. **Backend Setup:**
   - Navigate to the backend directory and install the required Python packages:
     ```
     pip install -r requirements.txt
     ```

3. **Frontend Setup:**
   - Navigate to the frontend directory and install the required npm packages:
     ```
     npm install
     ```

4. **Run the Backend:**
   - Start the backend server:
     ```
     python src/backend/app.py
     ```

5. **Run the Frontend:**
   - Start the frontend application:
     ```
     npm start
     ```

## Usage Guidelines

- Users can upload documents through the Document Uploader component.
- After uploading, users can ask questions in the Chat Window, and the chatbot will provide answers with citations.
- The chatbot will also summarize common themes from the ingested documents.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.
