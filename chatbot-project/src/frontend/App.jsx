import React, { useState } from 'react';
import ChatWindow from './components/ChatWindow';
import DocumentUploader from './components/DocumentUploader';
import './styles/main.css';

const App = () => {
    const [documents, setDocuments] = useState([]);
    const [questions, setQuestions] = useState([]);
    const [responses, setResponses] = useState([]);

    const fetchDocuments = async () => {
        try {
            const res = await fetch('/documents/');
            const data = await res.json();
            setDocuments(data);
        } catch (error) {
            console.error('Error fetching documents:', error);
        }
    };

    const handleDocumentUpload = () => {
        fetchDocuments();
    };

    const handleQuestionSubmit = async (question) => {
        try {
            const formData = new FormData();
            formData.append('question', question);
            // Add document IDs if you want to query specific documents
            documents.forEach(doc => formData.append('documentIds', doc.id));

            const response = await fetch('/ask/', {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                throw new Error('Failed to get answer');
            }

            const data = await response.json();
            setQuestions(prev => [...prev, question]);
            setResponses(prev => [...prev, data]); // Store the complete response with answers and themes
        } catch (error) {
            console.error('Error asking question:', error);
            // Show error to user
            setQuestions(prev => [...prev, question]);
            setResponses(prev => [...prev, { 
                answers: [{ 
                    docId: 'ERROR', 
                    answer: 'Failed to get answer from the server', 
                    citation: 'N/A' 
                }],
                themes: []
            }]);
        }
    };

    React.useEffect(() => {
        fetchDocuments();
    }, []);

    return (
        <div className="app">
            <h1>Document Chatbot</h1>
            <DocumentUploader onUpload={handleDocumentUpload} />
            <ChatWindow 
                questions={questions} 
                responses={responses}
            />
            <div className="question-input">
                <input
                    type="text"
                    placeholder="Ask a question..."
                    onKeyDown={(e) => {
                        if (e.key === 'Enter' && e.target.value.trim()) {
                            handleQuestionSubmit(e.target.value.trim());
                            e.target.value = '';
                        }
                    }}
                />
            </div>
        </div>
    );
};

export default App;