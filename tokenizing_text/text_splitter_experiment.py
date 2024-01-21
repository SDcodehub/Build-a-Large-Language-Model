import re

text = "Hello, world. This, is a test."
result = re.split(r"(\s)", text)
print(result)

result = re.split(r"([,.]|\s)", text)
print(result)

result = [item.strip() for item in result if item.strip()]
print(result)

# handle other types of punctuation, such as question marks, quotation marks, and the double-dashes
text = "Hello, world. Is this-- a test?"
result = re.split(r'([,.?_!"()\']|--|\s)', text)
result = [item.strip() for item in result if item.strip()]
print(result)
