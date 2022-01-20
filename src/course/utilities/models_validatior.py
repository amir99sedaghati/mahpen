valid_extensions = {
    # "zip" : [
    #     ".rar",
    #     ".zip",
    #     ".tar",
    # ] ,
    "video" : [
        ".mp4",
        ".mkv",
        ".mpeg",
        ".mpg",
        ".mov",
        "wmv",
        "avi",
    ] ,
    "img" : [
        ".jpg",
        ".png",
        ".jpeg",
        ".jfif",
        ".webp",
    ] ,
    # "pdf" :[
    #     ".pdf",
    # ] ,
}

def validate_video_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    if ext.lower() not in valid_extensions["video"] :
        raise ValidationError(f'unsupported file extension.\
            your file extension should one of {valid_extensions["video"]}')