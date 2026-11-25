# There is no static secret at all. The server sends a random challenge,
# this code signs it with a private key that itself never leaves a secure
# signing service, and only the signature (useless outside this one exchange)
# is ever visible. Nothing reusable exists to "find".
challenge = get_challenge_from_server()
signature = remote_signing_service.sign(challenge)  # private key never leaves the service
