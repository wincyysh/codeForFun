import pytesseract
from PIL import Image
import glob
import os

"""
Common issues:
- Files has different capitalization(e.g., ".PNG" instead of ".png")
- Find all PNG files regardless case
"""
def find_png_files():
  list_pngs = glob.glob("*.png") + glob.glob("*.PNG")
  return list_pngs

  # print(f"Current directory: {os.getcwd()}")
  # print(f"PNG files found: {png_files}")
  # Without f-string, you would need to do:
  # print("PNG files found: " + str(png_files))  
  # or
  # print("PNG files found: {}".format(png_files))

"""
Capture first line as filenames:
- Remove spaces
- Camel casing
- Remove special characters
- left only alphanumeric (letters or numbers)
"""

def name_files(text):
  first_line = text.split('\n')[0]
  words = first_line.split()
  camelCasing = ''.join(word[0].capitalize()+word[1:] for word in words)
  camelCasing = ''.join(c for c in camelCasing if c.isalnum())
  return camelCasing



def scan_png(png):
  try:
    png_open = Image.open(png)
    png_txt = pytesseract.image_to_string(png_open)
    png_txt = png_txt.replace('-\n', '')
    png_txt = png_txt.replace('- \n', '')
    
    png_lines = png_txt.split('\n')
    sentences = []
    for i, line in enumerate(png_lines):
      if i < len(png_lines)-1:
        if line and (not line.endswith('.')):
          line = line.strip() + ' '
          sentences.append(line)
        else:
          sentences.append(line+'\n')
      else:
        sentences.append(line)
    paragraphs = ''.join(sentences)
    paragraphs = paragraphs.replace('- ', '')
    return paragraphs
  
  except Exception as e:
    print(f"Error Processing {png}: {str(e)}")
    return None

def process_png_dir():
  png_files = find_png_files()

  if not png_files:
    print('No found!\n')
    return
  
  for png_path in png_files:
    each_png = scan_png(png_path)
    if each_png:
      filename = name_files(each_png)
      if not filename:
        filename = os.path.splitext(png_path)[0]
      output_file = f"{filename}.txt"
      counter = 1
      while os.path.exists(output_file):
        output_file = f"{filename}_{counter}.txt"
        counter += 1
      try:
        with open(output_file, 'w', encoding='utf-8') as f:
          f.write(each_png)
          print(f"Processed {png_path} -> {output_file}")
      except Exception as e:
        print(f"Error saving {output_file}: {str(e)}")
    else:
      print('No text from pngs\n')

if __name__ == "__main__":
    process_png_dir()