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
    if file_type.upper() == 'SVG':
        factory = qrcode.image.svg.SvgImage
    else:
        factory = None  # Use default for raster formats like PNG or JPG

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=0,  # No extra border from QR code generation
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white', image_factory=factory)

    # Skip conversion for SVG since it's not a raster image
    if file_type.upper() != 'SVG':
        # Convert to PIL Image if necessary
        if not isinstance(img, Image.Image):
            img = img.convert("RGB")

        # Add a black border around the QR code
        img_with_black_border = ImageOps.expand(img, border=2, fill='black')

        # Add a white border around the black border
        img_with_white_border = ImageOps.expand(img_with_black_border, border=2, fill='white')

        # Save the image based on file type
        buf = BytesIO()
        img_with_white_border.save(buf, format=file_type.upper())
        qr_code_data = buf.getvalue()
    else:
        # For SVG, no need for additional handling
        buf = BytesIO()
        img.save(buf)
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
