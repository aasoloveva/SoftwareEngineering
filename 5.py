def fruits(**kwargs):
    for fruit, amount in kwargs.items():
        print(f"{fruit}: {amount}")

if __name__ == "__main__":
    fruits(apples = 1, oranges = 5, bananas = 2)
    fruits(**{"mandarins": 10, "pears": 2})