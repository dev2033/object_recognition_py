from pixellib.instance import instance_segmentation


def object_detection_on_an_image():
    segment_image = instance_segmentation()
    segment_image.load_model(
    "/home/danil/Documents/object_recognition/src/mask_rcnn_coco.h5"
    )

    # выборка по конкретному объекту
    # target_class = segment_image.select_target_classes(person=True)
    target_class = segment_image.select_target_classes()

    result = segment_image.segmentImage(
        # image_path="1city.jpg",
        image_path="2cars_people.jpeg",

        # рамки у объектов
        show_bboxes=True,

        # передаем тот объект, который хотим выделить
        # segment_target_classes=target_class,

        # вырезаем объект и сохраняем в отдельный файл
        extract_segmented_objects=True,
        save_extracted_objects=True,

        # выходное изображение
        output_image_name="output.jpg"
    )

    # считает колличество объектов
    print(result[0]["scores"])
    objects_count = len(result[0]["scores"])
    print(f"Найдено объектов: {objects_count}")



def main():
    object_detection_on_an_image()


if __name__ == '__main__':
    main()
