# Loom Video Script

Hello, my name is Ajay Chirmade.

In this assignment, I built an AI based DDR report generation workflow.

The goal of the system is to read an Inspection Report and a Thermal Report, extract useful observations, merge duplicate or related findings, handle missing information, and generate a final client ready Detailed Diagnostic Report.

Because the original company source documents were not provided, I created realistic sample inspection and thermal reports to demonstrate the complete workflow.

The system separates the work into clear stages. First, the documents are ingested. Then text observations and relevant images are extracted. Next, related findings are merged area wise. After that, the system checks for missing details, assigns severity, and writes the final DDR report.

The final report includes a property issue summary, area wise observations, probable root causes, severity reasoning, recommended actions, additional notes, and missing or unclear information.

The main focus of this project is reliability. The system does not invent facts. If information is missing, it clearly writes Not Available. If an image is not available, it says Image Not Available.

The current version is a working demo with sample data. In a production version, I would improve it by adding OCR, stronger PDF image extraction, LLM based validation, vector search, FastAPI deployment, Docker support, and automated evaluation.

Thank you.
