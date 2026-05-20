import streamlit as st
from pathlib import Path
from src.ddr_generator import generate_ddr_from_sample_data
from src.report_writer import write_ddr_docx

st.set_page_config(page_title="AI DDR Report Generator", layout="wide")
st.title("AI DDR Report Generator")
st.write("Upload an Inspection Report and Thermal Report to generate a structured client-ready DDR.")

inspection_file = st.file_uploader("Upload Inspection Report", type=["pdf", "docx"])
thermal_file = st.file_uploader("Upload Thermal Report", type=["pdf", "docx"])

st.info("This demo uses a deterministic sample extraction pipeline. It can be connected to an LLM or OCR model for production use.")

if st.button("Generate DDR Report"):
    if not inspection_file or not thermal_file:
        st.warning("Please upload both files before generating the report.")
    else:
        ddr_data = generate_ddr_from_sample_data()
        output_path = Path("outputs/Generated_DDR_From_App.docx")
        output_path.parent.mkdir(exist_ok=True)
        write_ddr_docx(ddr_data, output_path)
        st.success("DDR report generated successfully.")
        with open(output_path, "rb") as f:
            st.download_button("Download DDR Report", f, file_name="Generated_DDR_Report.docx")
        st.json(ddr_data)
