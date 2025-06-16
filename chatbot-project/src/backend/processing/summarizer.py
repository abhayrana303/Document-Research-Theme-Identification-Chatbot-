class Summarizer:
    def __init__(self):
        pass

    def summarize(self, docs):
        # Simple summary: list filenames
        return "\n".join([doc["filename"] for doc in docs])