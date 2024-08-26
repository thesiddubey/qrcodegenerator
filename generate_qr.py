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


def generate_qr_code(data, file_type):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,  # Increased box size for higher resolution
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    # Convert the image to the desired file type
    buf = BytesIO()
    if file_type.lower() == 'png':
        img = qr.make_image(fill='black', back_color='white')
        img.save(buf, format='PNG', dpi=(300, 300))
    elif file_type.lower() == 'svg':
        factory = qrcode.image.svg.SvgImage
        code = qr.make_image(image_factory=factory)
        code.save(buf)
    else:
        raise ValueError("Unsupported file type")

    return buf.getvalue()

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