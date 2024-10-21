lines = ["one", "two", "three"]
with open ("input.txt", "w") as f:
    for l in lines:
        f.write(f"Line {l}\n")