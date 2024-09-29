from datetime import datetime as dt
from datetime import timedelta as td

def main():
    print(
        f"Сегодня {dt.today().date()}.\nДень недели - {dt.today().isoweekday()}"
    )
    n = int(input("Введите количество дней: "))
    res = (dt.today() + td(days = n))
    print(
        f"Через {n} дней будет {res.date()}.\nДень недели - {res.isoweekday()}"
    )

if __name__ == "__main__":
    main()