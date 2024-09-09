# Тема 1. Работа с репозиториями
Отчет по Теме #1 выполнил(а):
- Соловьева Анна Антоновна
- ИВТ-22-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | - |
| Задание 2 | + | - |
| Задание 3 | + | - |
| Задание 4 | + | - |
| Задание 5 | + | - |
| Задание 6 | + | - |
| Задание 7 | + | - |
| Задание 8 | + | - |
| Задание 9 | + | - |
| Задание 10 | + | - |
| Задание 11 | + | - |
| Задание 12 | + | - |
| Задание 13 | + | - |
| Задание 14 | + | - |
| Задание 15 | + | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Установка Git

### Результат. 
![img1](https://github.com/aasoloveva/SoftwareEngineering/blob/93db64760879917540e84115775affd7d2df849d/img/screenshot_1.2_1.png)

## Выводы

После установки Git, можно проверить его версию через командную строку вводом команды git --version

## Лабораторная работа №2
### Установка имени пользователя и адреса электронной почты
### Результат
![img2](https://github.com/aasoloveva/SoftwareEngineering/blob/20482b5d003a6854b7be6ee74e3c712cede5029f/img/screenshot_1.2_2.png)
## Выводы
Имя пользователя и почту можно сменить при помощи команд git config --global user.name "..." и git config --global user.email "..." соответственно 

## Лабораторная работа №3
### Создание нового репозитория
![img3](https://github.com/aasoloveva/SoftwareEngineering/blob/1c95a8c7149dbea784f9847efae7b73e441f05b0/img/screenshot_1.2_3.png)
## Выводы
При помощи команды git init в соответствующей директории можно создать репозиторий
  
## Лабораторная работа №4
### Подготовка файлов
### Добавление одного файла
![img4-1](https://github.com/aasoloveva/SoftwareEngineering/blob/0cd1e8c0a92eb236252aa7c1f18f8840fb25bc74/img/screenshot_1.2_4.png)
### Проверка статуса
![img4-2](https://github.com/aasoloveva/SoftwareEngineering/blob/b1250a8d1fa69d885506872d6020b28b8b1d6bde/img/screenshot_1.2_5.png)
## Выводы
При помощи команды git add *название файла* можно добавить файл в репозиторий, а при помощи команды git status узнать статус репозитория и изменений в нем

## Лабораторная работа №5
### Создайте первый коммит, фиксируя текущее состояние файлов. Используйте команду git commit с флагом --m для добавления описания коммита
![img5-1](https://github.com/aasoloveva/SoftwareEngineering/blob/1c142cfe4367d78b777464e42477db558ddffdf5/img/screenshot_1.2_6.png)
### Для просмотра списка коммитов в хронологическом порядке используйте команду git log. Эта команда покажет вам информацию о каждом коммите, включая идентификатор коммита, автора, дату и время коммита, а также описание.
![img5-2](https://github.com/aasoloveva/SoftwareEngineering/blob/1c142cfe4367d78b777464e42477db558ddffdf5/img/screenshot_1.2_7.png)
### По умолчанию git log может показывать много коммитов. Вы можете ограничить количество выводимых коммитов, используя параметр --n, где n - это количество коммитов, которое вы хотите видеть
![img5-3](https://github.com/aasoloveva/SoftwareEngineering/blob/1c142cfe4367d78b777464e42477db558ddffdf5/img/screenshot_1.2_8.png)
### Если вы хотите более краткое представление каждого коммита, вы можете использовать параметр --oneline. Это выведет каждый коммит в одной строке, сокращенно отображая его идентификатор и описание
![img5-4](https://github.com/aasoloveva/SoftwareEngineering/blob/1c142cfe4367d78b777464e42477db558ddffdf5/img/screenshot_1.2_9.png)
### Для более наглядного представления истории коммитов, вы можете использовать команду git log с параметром -graph. Это покажет графическое дерево коммитов с ветвями и слияниями
![img5-5](https://github.com/aasoloveva/SoftwareEngineering/blob/535f8e5756ed76d34c0c771c6bb47c50456aaf0d/img/screenshot_1.2_10.png)

## Выводы
1. При помощи команды git commit с параметром -m можно добавить к коммиту комментарий
2. При помощи команды git log можно просмотреть историю коммитов, с параметром -n можно ограничить количество отображаемых коммитов, с параметром --oneline коммиты отображатся в одну строку, и при помощи параметра --graph можно просмотреть коммиты в виде графа

## Лабораторная работа №6
### Подключение к удаленному репозиторию
### Загрузка изменений на удаленный репозиторий
![img6-1](https://github.com/aasoloveva/SoftwareEngineering/blob/e9a2633f6ad967b275109dfec468827866602a2e/img/screenshot_1.2_13.png)
### Извлечение изменений с помощью git pull
![img6-2](https://github.com/aasoloveva/SoftwareEngineering/blob/cb2a0ffecbf92831eaab8676cd2b6325cf8ec2b1/img/screenshot_1.2_14.png)
### Добавление измненений в стэш
![img6-3](https://github.com/aasoloveva/SoftwareEngineering/blob/6456426e9a3047d03aaf1545a6c1ccbd2f60c269/img/screenshot_1.2_15.png)
### Возврат к сохраненным изменениям
![img6-4](https://github.com/aasoloveva/SoftwareEngineering/blob/b677c2bc7e96276fc107661cd6b12d02d0c6e664/img/screenshot_1.2_16.png)
## Выводы
- С помощью команды git remote add origin *ссылка* можно связать удаленный репозиторий с локальным
- С помощью команды git push изменения загружаются на удаленный репозиторий
- git pull позволяет извлечь изменения
- Команда git stash позволяет добавить изменения к стэш, а git stash apply или git stash pop позволяет вернуться к сохраненным в стэше изменениям

## Лабораторная работа №7
### Создание новой ветки. Выполните команду git branch с именем новой ветки, которую вы хотите создать
![img7-1](https://github.com/aasoloveva/SoftwareEngineering/blob/4d6af62e322f280f2de3ccccbe7735cfe11ce756/img/screenshot_1.2_17.png)
### Переключение на новую ветку
![img7-2](https://github.com/aasoloveva/SoftwareEngineering/blob/4d6af62e322f280f2de3ccccbe7735cfe11ce756/img/screenshot_1.2_18.png)
### Слияние веток
![img7-3](https://github.com/aasoloveva/SoftwareEngineering/blob/4d6af62e322f280f2de3ccccbe7735cfe11ce756/img/screenshot_1.2_19.png)
### Перебазирование веток
![img7-4](https://github.com/aasoloveva/SoftwareEngineering/blob/4d6af62e322f280f2de3ccccbe7735cfe11ce756/img/screenshot_1.2_20.png)
## Выводы
- git branch *название* создает новую ветку 
- git checkout *название* или git switch *название* позволяет переключиться на ветку
- git merge *название* сливает указанную ветку с текущей
- git rebase *название* позволяет перебазировать ветку в конец целевой ветки

## Лабораторная работа №8
### Применение фетч
![img8](https://github.com/aasoloveva/SoftwareEngineering/blob/91bbbe2845df02552afdf6bfe2ac619f8273dc49/img/screenshot_1.2_21.png)
## Выводы
fetch позволяет извлечь изменения из удаленного репозитория, но не влияет на вашу текущую рабочую ветку. Он позволяет синхронизироваться с удаленным репозиторием, просмотреть изменения в нем или подготовиться к слиянию.

## Лабораторная работа №9
### Удаление файла
![img9-1](https://github.com/aasoloveva/SoftwareEngineering/blob/2667834216d2d9ed8b1db0cce48e23a914cdd8a2/img/screenshot_1.2_22.png)
### Удаление локальной ветки
![img9-2](https://github.com/aasoloveva/SoftwareEngineering/blob/aba76e82823c4e990f3761f8520189b4c93a888b/img/screenshot_1.2_23.png)
### Удаление удаленной ветки
![img9-3](https://github.com/aasoloveva/SoftwareEngineering/blob/ba21fdec864e99f849e413e69a54c1fe3b32e4cc/img/screenshot_1.2_24.png)
## Выводы
- git rm *имя* удаляет файл, git remove --cached *имя* удаляет файл только из индекса
- git branch -d *название*, -D удаляет локальную ветку, безопасно и принудительно соответственно
- git push origin --delete *название* удаляет удаленную ветку
- rmdir удаляет директорию, что также удаляет и локальный репозиторий

## Лабораторная работа №10
### Отслеживание изменений в коммитах
![img10-1](https://github.com/aasoloveva/SoftwareEngineering/blob/7a9242f90c60f980cf2543eb539141e58a9a3884/img/screenshot_1.2_25.png)
![img10-2](https://github.com/aasoloveva/SoftwareEngineering/blob/c17a98f252161e0df7c1a596c3bc75fed33b3d7e/img/screenshot_1.2_26.png)
## Выводы
git log позволяет посмотреть историю коммитов, а git diff сравнить 

## Лабораторная работа №11
### Возвращение файла к предыдущему состоянию
![img11](https://github.com/aasoloveva/SoftwareEngineering/blob/176a6ad41ddceabc54837c7a2629c65cd327fc55/img/screenshot_1.2_28.png)
## Выводы
git checkout можно использовать для возврата к предыдущим коммитам

## Лабораторная работа №12
### Сброс до предыдущего коммита
![img12](https://github.com/aasoloveva/SoftwareEngineering/blob/9f8f6340c7970d7d0ccd7489549e4c9058b5efcd/img/screenshot_1.2_29.png)
## Выводы
git reset --hard и git reset --soft используются для сброса до предыдущих коммитов

## Лабораторная работа №13
### Исправление последнего коммита
![img13-1](https://github.com/aasoloveva/SoftwareEngineering/blob/b1f87d046804cc5ba35adc6400a702d7a6c81499/img/screenshot_1.2_30.png)
### Исправление более раннего коммита
![img13-2](https://github.com/aasoloveva/SoftwareEngineering/blob/c8d7d41afdd943010824614d46c328e66f89bdb5/img/screenshot_1.2_31.png)
## Выводы
git commit --amend используется для редактикования описания коммита
git rebase -i HEAD~3 позволяет выбрать один из предыдущих коммитов, затем можно применить git commit --amend для его редактирования и закончить командой git rebase --continue

## Лабораторная работа №14
### Разрешение конфликтов при слиянии
![img14-1](https://github.com/aasoloveva/SoftwareEngineering/blob/394e1042cb649e3c3d69f57a93fbde77692578b0/img/screenshot_1.2_32.png)
![img14-2](https://github.com/aasoloveva/SoftwareEngineering/blob/394e1042cb649e3c3d69f57a93fbde77692578b0/img/screenshot_1.2_33.png)
![img14-3](https://github.com/aasoloveva/SoftwareEngineering/blob/394e1042cb649e3c3d69f57a93fbde77692578b0/img/screenshot_1.2_34.png)
![img14-4](https://github.com/aasoloveva/SoftwareEngineering/blob/394e1042cb649e3c3d69f57a93fbde77692578b0/img/screenshot_1.2_35.png)
## Выводы
При конфликте слияния git помечает конфликт внутри файла, необходимо открыть его и вручную выбрать необходимый вариант, после чего сохранить файл

## Лабораторная работа №15
### Настройка .gitignore
![img15-1](https://github.com/aasoloveva/SoftwareEngineering/blob/08e22256912338169e4fd4c058c619168789b575/img/screenshot_1.2_36.png)
![img15-2](https://github.com/aasoloveva/SoftwareEngineering/blob/08e22256912338169e4fd4c058c619168789b575/img/screenshot_1.2_37.png)
## Выводы
Файл .gitignore позволяет настроить файлы и директории, которые git будет игнорировать и не будет добавлять их в удаленный репозиторий

## Общие выводы по теме
- Развернутый вывод
