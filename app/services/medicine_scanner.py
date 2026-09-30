import cv2
import pytesseract


# Tesseract location on Windows
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def scan_medicine(image_path: str):

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Could not read image")


    # Convert to grayscale
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )


    # Remove noise
    gray = cv2.GaussianBlur(
        gray,
        (3, 3),
        0
    )


    # Improve text
    threshold = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]


    # OCR
    text = pytesseract.image_to_string(
        threshold
    )


    return text.strip()