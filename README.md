# OCR

## Installation

1. Create virtual environment and activate it (Optional but recommended)
    ```
    # snippets for linux

    python3 -m venv env
    source env/bin/activate
    ```

2. Install **paddlepaddle**
    ```
    # If you have cuda9 or cuda10 installed on your machine, please run the following command to install
    python3 -m pip install paddlepaddle-gpu -i https://mirror.baidu.com/pypi/simple

    # If you only have cpu on your machine, please run the following command to install
    python3 -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
    ```

2. Install required packages
    ```
    pip3 install -r requirements.txt
    ```

3. Install **paddleocr**
    ```
    pip3 install paddleocr
    ```

## Caveats in the code

1. Regarding fonts in <***draw_ocr***> function:
    > Font paths must be provided to the function to properly work.  
    Fonts can be downloaded from [paddleocr_repo](https://github.com/PaddlePaddle/PaddleOCR/tree/release/2.1/doc/fonts)


