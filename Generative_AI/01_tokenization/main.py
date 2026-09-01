import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey there! My name is Naman Mishra"
tokens = enc.encode(text)

print("Tokens : ", tokens)

decode = enc.decode([25216, 1354, 0, 3673, 1308, 382, 478, 7601, 147276, 614,])
print("Decoded tokens: ", decode)

