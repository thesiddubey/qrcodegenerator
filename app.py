######################
# QR Code Generator  #
#       app.py       #
#  Siddhartha Dubey  #
# GitHub:thesiddubey #
#    August 2024     #
######################

import streamlit as st
from generate_qr import generate_qr_code  # Import the QR code generator function

# Set the page configuration
st.set_page_config(
    page_title="QR Code Generator",  # Title in the browser tab
    page_icon="https://raw.githubusercontent.com/thesiddubey/qrcodegenerator/master/a4bbd98d-cb67-4474-ad00-e1dad8d81b59.jpg",  # URL to the favicon
)

# Streamlit app
st.title("QR Code Generator")

# Input for the link
link = st.text_input("Enter the link you want to generate the QR code for:")

# Dropdown for file type selection (PNG and SVG)
file_type = st.selectbox("Select output file type:", ["PNG", "SVG"])

# Generate button
if st.button("Generate QR Code"):
    if link:
        try:
            qr_code = generate_qr_code(link, file_type)
            st.success("QR Code generated!")
            st.download_button(
                label="Download QR Code",
                data=qr_code,
                file_name=f"{link.split('//')[-1].split('.')[0].replace('.', '_')}_qr_code.{file_type.lower()}",
                mime=f"image/{file_type.lower()}" if file_type.lower() != 'svg' else 'image/svg+xml',
            )
        except ValueError as e:
            st.error(str(e))
    else:
        st.error("Please enter a valid link.")

# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;  /* Aligns footer to the left */
        padding: 10px;
        font-size: 14px;
        color: #4d4e4e;
        display: flex;
        align-items: center;
    }
    .footer a {
        color: #4d4e4e;
        text-decoration: none;
        display: flex;
        align-items: center;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    .footer img {
        width: 24px; /* Slightly larger */
        height: 24px; /* Slightly larger */
        margin-right: 10px; /* Space between logo and text */
    }
    </style>
    <div class="footer">
        <a href="https://github.com/thesiddubey" target="_blank">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub Logo">
            Made with ❤︎ by Siddhartha Dubey
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
