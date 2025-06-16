import React from 'react';

const ChatWindow = ({ questions, responses }) => (
  <div className="chat-window">
    <div className="messages">
      {questions.map((question, idx) => (
        <div key={idx} className="qa-section">
          <div className="question">
            <strong>Q: {question}</strong>
          </div>
          <table className="answer-table">
            <thead>
              <tr>
                <th>Document ID</th>
                <th>Answer</th>
                <th>Citation</th>
              </tr>
            </thead>
            <tbody>
              {responses[idx]?.answers?.map((answer, ansIdx) => (
                <tr key={ansIdx}>
                  <td>{answer.docId}</td>
                  <td>{answer.answer}</td>
                  <td>{answer.citation}</td>
                </tr>
              ))}
            </tbody>
          </table>
          {responses[idx]?.themes?.map((theme, themeIdx) => (
            <div key={themeIdx} className="theme-section">
              <h4>{theme.title}</h4>
              <p>{theme.summary}</p>
            </div>
          ))}
        </div>
      ))}
    </div>
  </div>
);

export default ChatWindow;