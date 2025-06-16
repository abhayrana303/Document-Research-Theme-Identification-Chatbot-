def format_citation(document_id, page, paragraph):
    return f"Document ID: {document_id}, Page: {page}, Paragraph: {paragraph}"

def generate_reference(document_id, title, author, year):
    return f"{author} ({year}). {title}. Document ID: {document_id}."

def extract_citation_info(citation):
    # Assuming citation is a string formatted as "Document ID: {id}, Page: {page}, Paragraph: {para}"
    parts = citation.split(", ")
    citation_info = {}
    for part in parts:
        key, value = part.split(": ")
        citation_info[key.strip()] = value.strip()
    return citation_info