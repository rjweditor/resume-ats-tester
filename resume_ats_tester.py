import docx2txt
import spacy

def load_resume(filename):
    # Extract text from the resume
    return docx2txt.process(filename)

def test_resume(resume_text, keywords_to_check):
    # Load spaCy model for English
    nlp = spacy.load("en_core_web_sm")

    # Process the resume text using spaCy
    doc = nlp(resume_text)

    # Check if each keyword or phrase is present in the resume
    keyword_matches = {keyword: any(token.text.lower() == keyword.lower() for token in doc) for keyword in keywords_to_check}

    # Print the results
    print("Keyword Matches:")
    for keyword, matched in keyword_matches.items():
        print(f"{keyword}: {'Found' if matched else 'Not Found'}")

    # Extract skills using spaCy's Named Entity Recognition (NER)
    skills = [ent.text for ent in doc.ents if ent.label_ == "SKILL"]
    print("\nExtracted Skills:")
    for skill in skills:
        print(skill)

# Example usage
resume_file = 'sample_resume.docx'  # Replace with the path to your resume file
keywords_to_check = ["Python", "Machine Learning", "Data Science", "Teamwork", "Communication"]

resume_text = load_resume(resume_file)
test_resume(resume_text, keywords_to_check)
