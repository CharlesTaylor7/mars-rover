from photos.models import Photo, Camera


def get_photos_with_raw_SQL(rover, camera, limit):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT
                photos_photo.img_src,
                photos_photo.earth_date
            FROM
                photos_photo
            INNER JOIN
                photos_camera ON photos_photo.camera_id = photos_camera.id
            INNER JOIN
                photos_rover ON photos_camera.rover_id = photos_rover.id
            WHERE
                photos_rover.name = %(rover)s
            AND
                photos_camera.name = %(camera)s
            ORDER BY
                photos_photo.earth_date ASC
            LIMIT
                %(limit)s;
        """,
            {"rover": rover, "camera": camera, "limit": limit},
        )
        return cursor.fetchall()


def get_photos_with_ORM(rover, camera, limit):
    return (
        Photo.objects.filter(camera__name=camera)
        .filter(camera__rover__name=rover)
        .order_by("earth_date")[:limit]
        .values_list("img_src", "earth_date")
    )
