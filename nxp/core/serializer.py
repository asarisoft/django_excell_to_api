
def serialize_settings(data):
    return {
        "id": data.id,
        "name": data.name,
        "text_value": data.text_value,
        "img_value": data.img_value.url if data.img_value else "",
    }
