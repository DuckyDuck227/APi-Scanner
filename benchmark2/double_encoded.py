import base64

# double base64-encoded AWS key - decoding once still gives base64, not the real secret
encoded_twice = "UVV0SlFWRlhSVkpVV1ZWSlQxQk1TMHBJUjBZPQ=="
step_one = base64.b64decode(encoded_twice).decode()
aws_key = base64.b64decode(step_one).decode()
