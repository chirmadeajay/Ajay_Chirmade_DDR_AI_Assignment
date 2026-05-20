# AI DDR Report Generation Assignment

Candidate: Ajay Chirmade

## Project Summary

This project demonstrates an AI workflow that converts a site inspection report and a thermal report into a structured Main DDR, also known as a Detailed Diagnostic Report.

The company did not provide actual source inspection files, so this submission includes realistic sample input documents and a working demo pipeline that can be extended to similar reports.

## What Is Included

- Sample Inspection Report
- Sample Thermal Report
- Final DDR Report
- Streamlit demo app
- Python pipeline code
- Architecture explanation
- Loom video script
- Submission checklist
- Screenshot placeholders

## Live Demo

Live Demo:

- STREAMLIT URL:
https://ajay-chirmade-ddr-ai-assignment.streamlit.app/

- Loom Video:
https://www.loom.com/share/fc852adf5be64f2e8072224f1d64f840

- GitHub Repository:
https://github.com/chirmadeajay/Ajay_Chirmade_DDR_AI_Assignment

## Folder Structure

```text
Ajay_Chirmade_DDR_AI_Assignment
├── app.py
├── requirements.txt
├── README.md
├── sample_inputs
│   ├── Inspection_Report_Sample.docx
│   └── Thermal_Report_Sample.docx
├── outputs
│   └── Final_DDR_Report_Ajay_Chirmade.docx
├── src
│   ├── ddr_generator.py
│   └── report_writer.py
├── docs
│   ├── System_Architecture_Explanation.pdf
│   ├── Loom_Video_Script.md
│   └── Submission_Checklist.md
└── screenshots
```

## How To Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Workflow

```text
Input Reports
Text Extraction
Image Extraction
Observation Merging
Missing and Conflict Handling
Severity Assessment
DDR Report Generation
```

## Reliability Rules

```text
Do not invent facts
Mark unavailable information as Not Available
Mark missing images as Image Not Available
Mention conflicts clearly
Keep the final report client friendly
```

## Current Limitations

```text
The current demo uses sample deterministic extraction
Real scanned documents may require OCR
Image placement can be improved using automated image classification
Severity scoring can be improved using rule based and LLM based validation
```

## Future Improvements

```text
Add PyMuPDF based PDF image extraction
Add OCR for scanned reports
Add LangChain or LlamaIndex based extraction chain
Add vector database for document memory
Add FastAPI backend
Add Docker deployment
Add evaluation tests for report accuracy
```
