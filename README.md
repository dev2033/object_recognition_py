# Машинное обучение! Распознавание объектов!

***Для папки src:***

***Стек:***
1. Python3.9
2. pixellib
3. tensorflow (tensorflow-gpu)

Если хотите чтобы расчеты производились с видеокарты, то нужно устанавливать
tensorflow-gpu, если с процессора то tensorflow.

Ссылки на библиотеки:

1. <a href="https://www.tensorflow.org/">Tensorflow</a>

2. <a href="https://pixellib.readthedocs.io/en/latest/">pixellib</a>

Ссылка на готовую обученую 'сеть'(фильтры и маски выделения конкретных объектов):

https://github.com/matterport/Mask_RCNN/releases/

**Скачивать нужно версию 2.0**


Установка и запуск проекта:

1. Склонировать проект с GitHub:

    ```
    git clone https://github.com/dev2033/object_recognition_py.git
    ```

2. Установить зависимости:

    ```
    pip install -r requirements.txt

    pip install tensorflow-gpu (для видеокарт)

    pip install tensorflow (для процессоров)
    ```

3. Перейти в файл main.py и прописать путь до скачанной готовой обученной  сети(MASK)

4. Также указать пути и названия фотографий(одна входная другая выходная, то есть то что выйдет в итоге)



***Для папки face_recognition:***

```
sudo apt-get install libboost-all-dev libgtk-3-dev build-essential cmake
```

```
pip install -r requirements.txt
```
