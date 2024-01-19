
```markdown
# Python Resume ATS Tester

This Python script uses spaCy for natural language processing to analyze resumes and check for specific keywords and extracted skills. It provides a more advanced approach compared to basic ATS testers.

## Prerequisites

Make sure you have Python installed on your machine. Install the required libraries using the following command:

```bash
pip install docx2txt spacy
python -m spacy download en_core_web_sm
```

## Usage

1. Clone the repository or download the script file (`resume_ats_tester.py`).
2. Place your resume file (`sample_resume.docx` or other formats supported by `docx2txt`) in the same directory as the script.
3. Open a terminal in the script's directory.

Run the script with the following command:

```bash
python resume_ats_tester.py
```

The script will check for specific keywords and extract skills from the resume, providing detailed results.

## Customization

- Modify the `resume_file` variable to point to your specific resume file.
- Customize the `keywords_to_check` list based on the specific keywords or phrases you want to check for.

## Dependencies

- `docx2txt`: Library for extracting text from DOCX files.
- `spacy`: Natural language processing library for named entity recognition (NER).

```
