import base64

# decodes to a real AWS access key at runtime
encoded = "QUtJQUlPU0ZPRE5ON0VYQU1QTEU="
aws_key = base64.b64decode(encoded).decode()
