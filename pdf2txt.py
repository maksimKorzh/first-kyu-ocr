###################################################
#
#  Script to generate screenshots from book pages
#
###################################################

import pytesseract
import pyautogui as pg

# Below logic automates PDF viewer's navigation
# and takes a screenshot of each page for later
# optical character recognition processing

# Content
content = ''

# Loop over the pages
for page in range(125):
  # Click on PDF viewer's 'next page' button
  pg.click(50,80)

  # Open the screenshot image
  screenshot = pg.screenshot()

  # Use Tesseract to extract text with the specified language
  text = pytesseract.image_to_string(screenshot, lang='rus')

  # Strip text
  text = text.strip()

  # Save page
  content += text

# Write book in TXT format
with open('first-kyu-rus.txt', 'w') as f:
  f.write(content)
