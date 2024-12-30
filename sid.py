import base64

with open("sidenc.py", "rb") as encoded_file:
    encoded_content = encoded_file.read()

decoded_content = base64.b64decode(encoded_content).decode("utf-16")

exec(decoded_content)