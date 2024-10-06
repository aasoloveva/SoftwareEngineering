runs = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7,
        16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]
runscopy = runs.copy()
print("Топ 3 лучших: ")
for i in range(3):
    print(f"{i + 1}. {runscopy.pop(runscopy.index(max(runscopy)))}")
print("Топ 3 худших: ")
for i in range(3):
    print(f"{i + 1}. {runscopy.pop(runscopy.index(min(runscopy)))}")
print(f"Все результаты начиная с 10: {runs[10::]}")