interface Document {
    id: string;
    title: string;
    content: string;
    citations: Citation[];
}

interface Citation {
    documentId: string;
    page: number;
    paragraph: number;
}

interface UserQuery {
    question: string;
    documentIds?: string[];
}

interface QAResponse {
    answer: string;
    citations: Citation[];
}

interface Theme {
    title: string;
    summary: string;
}

interface SummarizedResponse {
    themes: Theme[];
    citations: Citation[];
}