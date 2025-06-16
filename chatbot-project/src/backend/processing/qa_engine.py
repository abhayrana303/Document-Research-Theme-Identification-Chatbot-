import os
import requests
from typing import List, Dict


class QAEngine:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.doc_counter = 0

    def _format_doc_id(self, doc) -> str:
        """Format document ID as DOC001, DOC002, etc."""
        if "id" in doc:
            return f"DOC{int(doc['id']):03d}"
        self.doc_counter += 1
        return f"DOC{self.doc_counter:03d}"
        
    def _extract_citation(self, answer_text: str) -> tuple[str, str]:
        """Extract citation from answer text and clean up the answer."""
        citation = "Page 1, Paragraph 1"  # Default citation
        
        # Look for citation patterns
        patterns = [
            r"(?i)(page\s+\d+,?\s*(?:paragraph|para|p)\s*\d+)",  # Page X, Paragraph Y
            r"(?i)(p\.\s*\d+,?\s*(?:paragraph|para|p)\s*\d+)",   # p. X, Paragraph Y
            r"(?i)(section\s+[\d.]+)",                           # Section X.Y
        ]
        
        for pattern in patterns:
            import re
            match = re.search(pattern, answer_text)
            if match:
                citation = match.group(1)
                # Remove the citation from the answer
                answer_text = re.sub(pattern, "", answer_text).strip()
                break
                
        # Clean up any trailing punctuation
        answer_text = answer_text.rstrip("., ")
        return answer_text, citation

    def process_question(self, question: str, documents: List[Dict]) -> tuple:
        answers = []
        for doc in documents:
            try:
                # Prepare context and prompt
                context = doc.get("text", "")
                prompt = f"""
                Based on the following context, answer the question. Your response must include a citation in the format 'Page X, Paragraph Y' at the end.
                
                Context: {context[:2000]}  # Limited to 2000 chars for API
                Question: {question}
                
                Format your response with a direct answer followed by a citation. Example:
                The company's revenue grew by 25% in Q2. (Page 3, Paragraph 2)
                """

                # Call Groq API
                response = requests.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                    },
                    json={
                        "model": "llama3-8b-8192",
                        "messages": [
                            {
                                "role": "system",
                                "content": "You are a precise document analysis assistant. Always provide answers with specific citations.",
                            },
                            {"role": "user", "content": prompt},
                        ],
                        "max_tokens": 512,
                        "temperature": 0.2,
                    },
                )

                if response.status_code == 200:
                    answer_text = response.json()["choices"][0]["message"]["content"]
                    # Extract citation and clean up answer
                    answer_text, citation = self._extract_citation(answer_text)
                    
                    # Format document ID
                    doc_id = self._format_doc_id(doc)
                    
                    answers.append({
                        "docId": doc_id,
                        "answer": answer_text,
                        "citation": citation
                    })
            except Exception as e:
                print(f"Error processing document {doc.get('id')}: {str(e)}")
                continue

        # Generate themes based on all answers if we have multiple answers
        themes = []
        if len(answers) > 1:
            # Call Groq API to generate themes
            themes_prompt = f"""
            Analyze these answers and identify key themes:
            
            {[a['answer'] for a in answers]}
            
            Generate 2-3 key themes that summarize the findings.
            """
            
            try:
                themes_response = requests.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                    },
                    json={
                        "model": "llama3-8b-8192",
                        "messages": [
                            {
                                "role": "system",
                                "content": "You are a theme analysis expert. Create concise, clear themes.",
                            },
                            {"role": "user", "content": themes_prompt},
                        ],
                        "max_tokens": 256,
                        "temperature": 0.3,
                    },
                )
                
                if themes_response.status_code == 200:
                    theme_text = themes_response.json()["choices"][0]["message"]["content"]
                    themes = [
                        {
                            "title": f"Theme {i+1}",
                            "summary": theme.strip()
                        }
                        for i, theme in enumerate(theme_text.split("\n"))
                        if theme.strip()
                    ]
            except Exception as e:
                print(f"Error generating themes: {str(e)}")

        return answers, themes