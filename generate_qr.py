######################
# QR Code Generator  #
#   generate_qr.py   #
#  Siddhartha Dubey  #
# GitHub:thesiddubey #
#    August 2024     #
######################

import qrcode
import qrcode.image.svg
from io import BytesIO
import os
from PIL import Image, ImageOps


def generate_qr_code(data, file_type):
    # Set the factory to create the image format based on file_type
    if file_type == 'SVG':
        factory = qrcode.image.svg.SvgImage
    else:
        factory = None  # Use default PNG format

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(image_factory=factory)

    # Add a black border around the QR code
    if file_type == 'SVG':
        # For SVG, no need to handle borders differently
        qr_code_data = img
    else:
        # Convert to PIL Image to add border
        if not isinstance(img, Image.Image):
            img = img.convert("RGB")
        bordered_img = ImageOps.expand(img, border=20, fill='black')  # Add black border
        buf = BytesIO()
        bordered_img.save(buf, format=file_type.upper())
        qr_code_data = buf.getvalue()

    return qr_code_data
    
# Test the QR code generation
def save_qr_code(data, file_type):
    qr_code_data = generate_qr_code(data, file_type)

    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Build the path to the 'Tests' directory within the same parent directory
    folder_path = os.path.join(current_dir, 'Tests')

    # Ensure the directory exists (this will not recreate if it already exists)
    os.makedirs(folder_path, exist_ok=True)

    # Full path where the QR code will be saved
    file_path = os.path.join(folder_path, f"{data.split('//')[-1].split('.')[0].replace('.', '_')}_qr_code.{file_type.lower()}")

    
    # Save the QR code
    with open(file_path, "wb") as f:
        f.write(qr_code_data)
    
    print(f"QR code saved to {file_path}")

# Example usage
if __name__ == "__main__":
    url = "https://wikipedia.org"
    file_type = "png"  # Choose between png, jpg, svg
    save_qr_code(url, file_type)
