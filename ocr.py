from paddleocr import PaddleOCR,draw_ocr
import cv2
from PIL import Image

def extract_text(img, ocr):
  """
  Returns list detected text with bbox, text and confidence value in following format:
  [bbox, (text,confidence), ....]
  """
  results = ocr.ocr(img, cls=True)
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

def get_annotated_img(img, boxes, txts, scores):
  """
  Draws bounding boxes on the image and detected texts
  """
  # if font path unset, problem in google-colab to execute
  # dont know whats the problem
  image = draw_ocr(img, boxes, txts, scores, font_path='/usr/share/fonts/truetype/humor-sans/Humor-Sans.ttf')
  pil_img = Image.fromarray(image)
  return pil_img

ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory

# Load image
img_path = 'test.jpeg'
img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

# Extract text
result = extract_text(img, ocr)

# Parse result
boxes, txts, scores = parse_result(result)

# Get annotated image
annotated_img = get_annotated_img(img, boxes, txts, scores)

# Display image
cv2.imshow('Annotated Image', annotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save image
cv2.imwrite('annotated_img.jpg', annotated_img)
