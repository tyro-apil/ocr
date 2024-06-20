from paddleocr import PaddleOCR, draw_ocr
from PIL import Image


def extract_text(img_path, ocr):
    """
    Returns list detected text with bbox, text and confidence value in following format:
    [bbox, (text,confidence), ....]
    """
    results = ocr.ocr(img_path, cls=True)
    result = results[0]
    return result


def parse_result(result):
    """
    Returns a tuple of bboxes_list, detected_text_list, confidence_list
    """
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    return boxes, txts, scores


def get_annotated_img(img_path, boxes, txts, scores):
    """
    Returns PIL image by drawing bounding boxes on the image and detected texts
    """
    img = Image.open(img_path).convert("RGB")
    im_show = draw_ocr(img, boxes, txts, scores, font_path="simfang.ttf")
    im_show = Image.fromarray(im_show)
    return im_show

# need to run only once to download and load model into memory
ocr = PaddleOCR(
    use_angle_cls=True, lang="en"
)  

# Load image
img_path = "test.jpeg"

# Extract text
result = extract_text(img_path, ocr)

# Parse result
boxes, txts, scores = parse_result(result)

# Get annotated image
annotated_img = get_annotated_img(img_path, boxes, txts, scores)

# Display image
annotated_img.show()

# Save image
annotated_img.save("annotated_img.jpg")
