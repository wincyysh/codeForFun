# PNG to Text Converter

A Python script that converts content from PNG images to text files using OCR (Optical Character Recognition). The script processes all PNG files in the current directory, extracts content using Tesseract OCR, and saves the results in individual text files.

## Features

- Handles PNG files with different case extensions (`.png`, `.PNG`)
- Extracts text from images using Tesseract OCR
- Generates filenames based on the first line of extracted text
- Handles hyphenated line breaks and formatting
- Automatically manages duplicate filenames
- Error handling for image processing and file operations

## Prerequisites

- Python 3.x
- Required Python packages:
  - pytesseract
  - Pillow (PIL)
- Tesseract OCR engine installed on your system

## Installation

1. Install the required Python packages:
```bash
pip install pytesseract Pillow
```

2. Install Tesseract OCR:
- For Windows: Download and install from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
- For macOS: `brew install tesseract`
- For Linux: `sudo apt-get install tesseract-ocr`

## Usage

1. Place your PNG files in the same directory as the script
2. Run the script:
```bash
python pngToTxt.py
```

The script will:
1. Find all PNG files in the current directory
2. Extract text from each image
3. Create text files named based on the first line of content
4. Save the processed text with proper formatting

## Functions

### `find_png_files()`
Finds all PNG files in the current directory, handling both lowercase and uppercase extensions.

### `name_files(text)`
Generates a filename from the first line of extracted text:
- Removes spaces
- Applies camel casing
- Removes special characters
- Retains only alphanumeric characters

### `scan_png(png)`
Processes a single PNG file:
- Opens the image
- Extracts text using OCR
- Handles hyphenation and line breaks
- Returns formatted text content

### `process_png_dir()`
Main function that:
- Processes all PNG files in the directory
- Generates unique filenames
- Saves extracted text to files
- Handles errors and provides progress feedback

## Error Handling

The script includes comprehensive error handling for:
- File opening and processing
- OCR text extraction
- File saving operations
- Duplicate filename management

## Output

- Creates text files named after the first line of content
- Automatically adds numbers to prevent overwriting existing files
- Provides console feedback on processing status and any errors

## Limitations

- Requires clear, readable text in images for optimal OCR results
- Processing speed depends on image size and complexity
- OCR accuracy depends on image quality and text clarity

## Contributing

Feel free to submit issues and enhancement requests