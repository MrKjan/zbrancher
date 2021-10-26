# branch_name_former
Задача:

https://jira.company.com/jira/browse/TASK-11111, ‘Bug description’ => ‘feature/PROJECT_PREFIX/TASK-11111_Bug_description’
вот такой вход и выход)

Перед началом использования следует сделать файл исполняемым:
```bash
$ chmod +x main.py
```

Для удобства использования стоит сделать алиас к файлу:
```bash
$ echo "alias TODO" >> ~/.bashrc
```

Чтобы задать `PROJECT_PREFIX`, присвойте новое значение переменной `prefix` внутри файла `main.py`
