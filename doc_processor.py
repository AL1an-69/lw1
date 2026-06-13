import os
from docx import Document

def get_text_from_docx(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    doc = Document(file_path)
    full_text = [para.text for para in doc.paragraphs]
    
    return '\n'.join(full_text)

def get_docx_files_from_directory(directory: str) -> list:
    files = []
    for filename in os.listdir(directory):
        if filename.endswith(".docx"):
            files.append(os.path.join(directory, filename))
    return files