def generate_ddr_from_sample_data():
    """Return structured DDR data.

    In a production workflow, replace this deterministic sample extraction with:
    1. PDF or DOCX text extraction
    2. OCR for scanned reports
    3. Image extraction and tagging
    4. LLM based observation merging
    5. Validation rules for missing and conflicting information
    """
    return {
        "property_issue_summary": "Moisture intrusion, ceiling leakage, bathroom wall dampness, minor kitchen cracks, and electrical panel overheating were identified.",
        "area_wise_observations": [
            {
                "area": "Living Room Ceiling",
                "observation": "Water staining and thermal variation indicate possible retained moisture.",
                "severity": "Medium",
                "reasoning": "Moisture can spread and damage finishes if the source is not repaired."
            },
            {
                "area": "Bathroom Shared Wall",
                "observation": "Damp smell and moisture marks indicate possible hidden pipe leakage.",
                "severity": "Medium",
                "reasoning": "The exact moisture reading was not available, so further testing is required."
            },
            {
                "area": "Electrical Panel",
                "observation": "Thermal scan shows abnormal hotspot near breaker bank with 72 C maximum reading.",
                "severity": "High",
                "reasoning": "Electrical overheating may create safety and fire risk."
            }
        ],
        "probable_root_cause": "Possible plumbing leakage, weak waterproofing, retained moisture, and electrical load imbalance or loose connection.",
        "recommended_actions": [
            "Arrange immediate electrical inspection by a licensed electrician.",
            "Trace and repair leakage source before cosmetic repair.",
            "Use moisture meter testing and plumbing pressure testing.",
            "Monitor kitchen wall cracks and repair if movement increases."
        ],
        "missing_or_unclear_information": [
            "Exact plumbing layout: Not Available",
            "Age of electrical panel: Not Available",
            "Kitchen wall image: Image Not Available"
        ]
    }
