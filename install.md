# Установка

TL;DR: Ничего не хочу устанавливать, что делать?

**Программируйте тут**:

- https://www.online-python.com/
- https://replit.com/languages/python3
- https://www.programiz.com/python-programming/online-compiler/
- https://colab.research.google.com/


> Веб интерпретаторы позволяют вам выполнять код прямо в браузере.
> Однако вам будет труднее/невозможно работать с нескольким файлами.
> Это потребуется в дальнейших модулях.
> Рассматривайте это как **временное решение**.


## Установка Python

Теперь перейдём к самой установке Python для вашей системы.
Вся уставновка сводится к прямой загрузке с сайта.
И последующего запуска исполныемого файла установщика.

**Ссылки для загрузки**:

- [Win/Linux/Mac](https://www.python.org/downloads/)
- [Для windows 7](https://www.python.org/downloads/release/python-350/)

> Обратите внимание что Win 7 уже объявлена не поддерживемой.
> Если версия 3.5 окажется слишкомй старой для выполнения,
> то воспользуйтесь **онлайн интерпретаторами** выше.

В состав базовой версии Python входят следующие компоненты:

- **IDLE** — простая среда разработки Python-программ;
- **документация** — инструкция по использованию Python;
- **стандартная модули** — набор функций, которые упрощают работу с числами,
  файлами, API сторонних сервисов и так далее;
- **пакетный менеджер PIP** — утилита для скачивания и установки модулей,
  фреймворков и других пакетов, расширяющих функциональность Python;
- **стандартный набор тестов** — чтобы проверять надёжность программы;
- **Python Launcher** — приложение для запуска программ с расширением `.py`.


### Установка на Windows 7/10/11

Скачайте установочный файл, нажав на жёлтую кнопку **Download Python**,
и запустите его.

Выберите путь установки и поставьте обе галочки:
во втором пункте мы указываем, что нужно добавить Python в переменную окружения
**PATH** — это позволит вызывать его из любой директории.

Затем выбираем «Установка для всех пользователей» (Install for all users),
нажимаем Install Now и разрешаем приложению вносить изменения:

![](/assets/img/image1.png)

Когда установка будет завершена, вы увидите следующее окно:

![](/assets/img/image2.png)

Чтобы убедиться в правильности установки Python выполниет следующие шаги:

- Нажмите `Win+R` и введите `cmd`.
  Или нажмите правой кнопкой мыши на иконку window в левом нижнем углу экрана и откройте `Window PowerShell`.
- Введите `py`, и нажмите ентер.

![](/assets/img/image3.png)


### Установка на Linux

На большинстве современных дистрибутивах GNU/linux уже утсановлен
python одной из свежих версий.
Проверить это вы сможете следующей командой.

```sh
python --version
```

Вывод этой команды можут быть прмиерно таким:

```
Python 3.11.8
```

Подобный вывод означает что python уже установлен и вы можете
приступить к следующему шагу - установка м настройка vscode.

В ином же случае вы можете установить python используя встроенные
пакетные менеджеры:

Устанавливайте пакет `python3`, если такавой не найден, то `python`.

**Debian-based** (Debian, Ubuntu, Mint, ...):

```sh
sudo apt install python3
```

**RedHat-based** (Fedora, ...):

```sh
sudo dnf install python3
```

**Arch-based** (Arch linux, Manjaro, ...)

```sh
sudo pacman -Syu python
```

После выполнения одной из указанных команд в зависимости от вашего
дистрибутива установка python на этом завершается,


### MacOS

Поскольку MacOS и Linux имеют общего предка, процесс установки будет похож.

С давних времён MacBook и iMac выпускались с предустановленным Python 2.7.
Однако начиная с версии 12.3 разработчики «яблочной» ОС отказались от
этой традиции.

Чтобы проверить, установлен ли Python, откройте командную строку и введите
следующую команду:

```sh
python --version
```

Вывод этой команды можут быть прмиерно таким:

![](/assets/img/image4.png)

Подобный вывод означает что python уже установлен и вы можете
приступить к следующему шагу - установка м настройка vscode.

Иначе же скачайте последную версию с
[официального сайта](https://www.python.org/downloads/).

![](/assets/img/image5.png)
![](/assets/img/image6.png)


## Установка VsCode

[VSCode](https://code.visualstudio.com/) - Мощная IDE для разработчиков.
Она поддерживает множество язык программирования,
инструменты для быстрого написания и тестировани вашего кода.
Также VSCode имеет встроенную поддержку git и GitHub.

Утсановка тут тоже достаточно простая.
Скачиваем установочный файл и выполняем слудующие шаги.

![](/assets/img/image7.png)
![](/assets/img/image8.png)
![](/assets/img/image9.png)

На этом установку можно считать завершённой.

### Для Arch-based

Если вы являетесь пользователем **Arch-based** дистрибутива, то
установка аналога VSCode сводится к одной команде.

```sh
sudo pacman -Syu code
```

данная версия является лишь отличается вырезанными компонентами
Microsoft, которые будет не так важны.


## Настройка VSCode

Теперь давайте установим все необходимые для работа плагины.

Слева найдите раздел расширений, у него вот такая иконка.

![](/assets/img/image10.png)

Самое главное что нам нужно будет установить - **Python**,
Это расширение добавит нам автодополнение, подсветку синтаксиса, отладку...

![](/assets/img/image11.png)

Следующие будет установка **русификатора**.

![](/assets/img/image12.png)

Ну и ещё можно установить **красивые иконочки** к файлам.

![](/assets/img/image13.png)


### Смена языка на Русский

> Хотя я бы рекомендовал использовать программу на английском языке.
> Это даст вам плюсик к навыкам английского.
> к тому же если вы будете искать решения проблем, то они вероятно
> будут как раз на английском языке.

Смена языка проходит достаточно просто.
Переходим в меню `View` -> `Command palette` (`Ctrl + Shift + P` или `F1`).
Начинаем вводить `configure disp`...
У вас должен появиться пункт `Configure Display Language`.
В выпадающем меню вы уже сможете выбрать нужный вам Русский язык.

![](/assets/img/image14.png)