import streamlit as st
import os
import time
from PIL import Image
import io
import base64

# Set page configuration
st.set_page_config(
    page_title="DocuLegal - Indian Legal Document Scanner",
    page_icon="📑",
    layout="wide",
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #34495e;
        margin-bottom: 1rem;
    }
    .result-container {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    .status-processing {
        color: #3498db;
        font-weight: bold;
    }
    .status-complete {
        color: #2ecc71;
        font-weight: bold;
    }
    .entity-label {
        display: inline-block;
        padding: 3px 7px;
        border-radius: 4px;
        margin-right: 5px;
        font-size: 0.9rem;
    }
    .entity-name {
        background-color: #3498db;
        color: white;
    }
    .entity-date {
        background-color: #2ecc71;
        color: white;
    }
    .entity-location {
        background-color: #9b59b6;
        color: white;
    }
    .entity-case {
        background-color: #e74c3c;
        color: white;
    }
    .clause-container {
        background-color: #eaf2f8;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
        border-left: 3px solid #3498db;
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        color: #7f8c8d;
        font-size: 0.8rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f1f3f4;
        border-radius: 4px 4px 0px 0px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #e2e6ea;
        border-bottom: 2px solid #3498db;
    }
</style>
""", unsafe_allow_html=True)

# App header
st.markdown('<h1 class="main-header">📑 DocuLegal</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="sub-header">Indian Legal Document Scanner & Analyzer</h2>', unsafe_allow_html=True)

# Create sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/150x150.png?text=DocuLegal", width=150)
    st.markdown("### About DocuLegal")
    st.write("DocuLegal helps you scan, analyze, and extract key information from Indian legal documents.")
    
    st.markdown("### Supported Documents")
    st.markdown("""
    - Affidavits
    - Rental Agreements
    - Sale Deeds
    - Power of Attorney
    - Court Judgments
    - Legal Notices
    - NDAs
    """)
    
    st.markdown("### Processing Steps")
    st.markdown("""
    1. Document Upload
    2. OCR Processing
    3. Document Classification
    4. Entity Extraction
    5. Clause Identification
    """)
    
    st.markdown("### Team")
    st.caption("A project by Team LegalTech - 2025")

# Main content area
st.markdown("### Upload your legal document")

# Create tabs for different input methods
tabs = st.tabs(["File Upload", "Camera Capture", "Sample Documents"])

# File Upload Tab
with tabs[0]:
    uploaded_file = st.file_uploader("Choose a PDF or Image file", type=["pdf", "png", "jpg", "jpeg"], key="file_upload")
    
    col1, col2 = st.columns(2)
    with col1:
        doc_language = st.selectbox(
            "Document Language",
            ["English", "Hindi", "Tamil", "Telugu", "Marathi", "Gujarati", "Bengali"],
            index=0
        )
    with col2:
        doc_quality = st.select_slider(
            "Document Quality",
            options=["Low", "Medium", "High"],
            value="Medium"
        )

    process_button = st.button("Process Document", type="primary", disabled=uploaded_file is None)

# Camera Capture Tab
with tabs[1]:
    st.write("Take a picture of your document using your camera")
    camera_input = st.camera_input("Capture Document", key="camera")
    
    if camera_input:
        st.success("Document captured successfully!")
        
        col1, col2 = st.columns(2)
        with col1:
            cam_doc_language = st.selectbox(
                "Document Language",
                ["English", "Hindi", "Tamil", "Telugu", "Marathi", "Gujarati", "Bengali"],
                index=0,
                key="cam_lang"
            )
        with col2:
            cam_doc_quality = st.select_slider(
                "Document Quality",
                options=["Low", "Medium", "High"],
                value="Medium",
                key="cam_quality"
            )
            
        cam_process_button = st.button("Process Document", type="primary", key="cam_process")

# Sample Documents Tab
with tabs[2]:
    st.write("Select from pre-loaded sample documents for testing")
    
    sample_docs = {
        "Rental Agreement": "rental_agreement_sample.pdf",
        "Affidavit": "affidavit_sample.pdf",
        "Sale Deed": "sale_deed_sample.pdf",
        "Court Judgment": "judgment_sample.pdf",
        "Legal Notice": "legal_notice_sample.pdf"
    }
    
    selected_sample = st.selectbox("Select a sample document", list(sample_docs.keys()))
    st.write(f"Selected: {selected_sample}")
    
    # This would show a preview of the sample document in a real implementation
    st.image("https://via.placeholder.com/600x400.png?text=Sample+Document+Preview", caption=f"{selected_sample} Preview")
    
    sample_process_button = st.button("Process Sample Document", type="primary", key="sample_process")

# Process document function - this would connect to your backend in the actual implementation
def process_document(document, language, quality):
    # This is a placeholder for the actual processing that would be handled by the backend
    # In the real implementation, you would make API calls to your FastAPI backend
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Simulate processing steps
    steps = [
        "Preprocessing document...",
        "Performing OCR...",
        "Classifying document type...",
        "Extracting named entities...",
        "Identifying key clauses...",
        "Generating results..."
    ]
    
    for i, step in enumerate(steps):
        # Update status
        status_text.markdown(f"<p class='status-processing'>{step}</p>", unsafe_allow_html=True)
        progress_bar.progress((i + 1) / len(steps))
        time.sleep(1)  # Simulate processing time
    
    status_text.markdown("<p class='status-complete'>Processing complete!</p>", unsafe_allow_html=True)
    return True

# Handle button clicks for processing
if 'process_button' in locals() and process_button and uploaded_file is not None:
    processing_success = process_document(uploaded_file, doc_language, doc_quality)
    if processing_success:
        display_results(uploaded_file)
        
if 'cam_process_button' in locals() and cam_process_button and camera_input is not None:
    processing_success = process_document(camera_input, cam_doc_language, cam_doc_quality)
    if processing_success:
        display_results(camera_input)
        
if 'sample_process_button' in locals() and sample_process_button:
    processing_success = process_document(sample_docs[selected_sample], "English", "High")
    if processing_success:
        display_sample_results(selected_sample)

# Function to display results
def display_results(document):
    st.markdown("## Analysis Results", unsafe_allow_html=True)
    
    # Create tabs for different result sections
    result_tabs = st.tabs(["Overview", "Extracted Text", "Named Entities", "Key Clauses", "Document Image"])
    
    # Overview Tab
    with result_tabs[0]:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Document Information")
            st.markdown("""
            **Document Type:** Rental Agreement  
            **Confidence:** 94%  
            **Language:** English  
            **Pages:** 4  
            **Creation Date:** 03-Jan-2025  
            """)
        
        with col2:
            st.markdown("### Summary")
            st.markdown("""
            This is a residential rental agreement between **John Doe** (Landlord) and **Jane Smith** (Tenant) for property located at **123 Main St, Mumbai** for a period of **11 months** starting from **15-Jan-2025** with a monthly rent of **₹25,000**.
            """)
        
        st.markdown("### Key Points")
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("• Security deposit: ₹50,000")
            st.info("• Notice period: 2 months")
            st.info("• Rent due date: 5th of each month")
        
        with col2:
            st.info("• Lock-in period: 6 months")
            st.info("• Electricity charges extra")
            st.info("• No subletting allowed")
    
    # Extracted Text Tab
    with result_tabs[1]:
        st.markdown("### Full Extracted Text")
        st.text_area("", value="THIS RENTAL AGREEMENT is made on this 3rd day of January, 2025 between Mr. John Doe, S/o Late Mr. Robert Doe, resident of 456 Park Avenue, Mumbai (hereinafter called the 'LANDLORD') of the ONE PART AND Ms. Jane Smith, D/o Mr. William Smith, resident of 789 Ocean Drive, Delhi (hereinafter called the 'TENANT') of the OTHER PART.\n\nWHEREAS the Landlord is the absolute owner of the property situated at 123 Main St, Mumbai, consisting of 2 Bedroom Hall Kitchen (2BHK) with attached bathroom and car parking (hereinafter referred to as the 'PREMISES').\n\nAND WHEREAS the Tenant has approached the Landlord to let out the said Premises to the Tenant for residential purpose for a period of 11 months commencing from 15th January, 2025...", height=300)
        
        with st.expander("Show formatting options"):
            st.write("Text formatting options would be available here in the full implementation")
    
    # Named Entities Tab
    with result_tabs[2]:
        st.markdown("### Extracted Named Entities")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### People")
            st.markdown("""
            <span class='entity-label entity-name'>LANDLORD</span> John Doe  
            <span class='entity-label entity-name'>TENANT</span> Jane Smith  
            <span class='entity-label entity-name'>RELATED</span> Robert Doe (Landlord's father)  
            <span class='entity-label entity-name'>RELATED</span> William Smith (Tenant's father)
            """, unsafe_allow_html=True)
            
            st.markdown("#### Dates")
            st.markdown("""
            <span class='entity-label entity-date'>AGREEMENT DATE</span> 3rd January, 2025  
            <span class='entity-label entity-date'>START DATE</span> 15th January, 2025  
            <span class='entity-label entity-date'>END DATE</span> 14th December, 2025  
            <span class='entity-label entity-date'>PAYMENT DATE</span> 5th of each month
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("#### Locations")
            st.markdown("""
            <span class='entity-label entity-location'>PROPERTY</span> 123 Main St, Mumbai  
            <span class='entity-label entity-location'>LANDLORD ADDRESS</span> 456 Park Avenue, Mumbai  
            <span class='entity-label entity-location'>TENANT ADDRESS</span> 789 Ocean Drive, Delhi
            """, unsafe_allow_html=True)
            
            st.markdown("#### Monetary")
            st.markdown("""
            <span class='entity-label entity-case'>RENT</span> ₹25,000 per month  
            <span class='entity-label entity-case'>DEPOSIT</span> ₹50,000  
            <span class='entity-label entity-case'>PENALTY</span> ₹500 per day for late payment
            """, unsafe_allow_html=True)
    
    # Key Clauses Tab
    with result_tabs[3]:
        st.markdown("### Key Clauses Identified")
        
        with st.expander("Rent & Payment (Clause 3)", expanded=True):
            st.markdown("""
            <div class='clause-container'>
            The Tenant shall pay to the Landlord the monthly rent of ₹25,000/- (Rupees Twenty Five Thousand Only) in advance on or before the 5th day of every English calendar month. The rent shall be paid by bank transfer to the Landlord's account or by cheque. Delay in payment of rent beyond the due date shall attract a penalty of ₹500/- per day of delay.
            </div>
            """, unsafe_allow_html=True)
        
        with st.expander("Security Deposit (Clause 4)"):
            st.markdown("""
            <div class='clause-container'>
            The Tenant has paid to the Landlord a sum of ₹50,000/- (Rupees Fifty Thousand Only) as interest-free refundable security deposit. The security deposit will be refunded at the time of vacating the Premises after deducting any outstanding dues or charges for damages beyond normal wear and tear. The Landlord shall refund the security deposit within 7 days of the Tenant vacating the Premises.
            </div>
            """, unsafe_allow_html=True)
        
        with st.expander("Lock-in Period (Clause 6)"):
            st.markdown("""
            <div class='clause-container'>
            The Tenant agrees to a lock-in period of 6 months from the commencement of this Agreement. If the Tenant vacates the Premises before the expiry of the lock-in period, the Tenant shall be liable to pay the rent for the remaining lock-in period or forfeit the security deposit, at the Landlord's option.
            </div>
            """, unsafe_allow_html=True)
        
        with st.expander("Termination (Clause 9)"):
            st.markdown("""
            <div class='clause-container'>
            Either party may terminate this Agreement after the lock-in period by giving 2 months' written notice to the other party. In the event of any breach of the terms of this Agreement by the Tenant, the Landlord shall have the right to terminate this Agreement immediately and the Tenant shall vacate the Premises within 7 days of receiving such notice.
            </div>
            """, unsafe_allow_html=True)
        
        with st.expander("Maintenance (Clause 12)"):
            st.markdown("""
            <div class='clause-container'>
            The Landlord shall be responsible for major repairs. The Tenant shall be responsible for day-to-day maintenance and minor repairs costing less than ₹2,000/-. The Tenant shall maintain the Premises in good and tenantable condition.
            </div>
            """, unsafe_allow_html=True)
    
    # Document Image Tab
    with result_tabs[4]:
        st.markdown("### Original Document")
        # In a real implementation, this would display the actual uploaded document
        st.image("https://via.placeholder.com/800x1000.png?text=Document+Image", caption="Original Document")
        
        st.download_button(
            label="Download Processed Document",
            data=io.BytesIO(b"sample data").getvalue(),
            file_name="processed_document.pdf",
            mime="application/pdf"
        )

# Function to display sample results
def display_sample_results(sample_name):
    # This would display pre-defined results for sample documents
    st.markdown(f"## Analysis Results for {sample_name}", unsafe_allow_html=True)
    # The rest would be similar to display_results but with pre-defined content

# Add footer
st.markdown("""
<div class="footer">
    <p>DocuLegal | Indian Legal Document Scanner | Version 1.0</p>
    <p>© 2025 Team LegalTech | All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)

# Add an export option
if st.sidebar.button("Export Results"):
    st.sidebar.success("Results exported successfully!")
    st.sidebar.download_button(
        label="Download Full Report",
        data=io.BytesIO(b"sample report data").getvalue(),
        file_name="legal_document_analysis.pdf",
        mime="application/pdf"
    )

# Add help section in sidebar
with st.sidebar.expander("Need Help?"):
    st.write("If you need assistance, please contact support@doculegal.com")
    st.write("View our tutorial for step-by-step guidance.")
