class ImageIfNotBlack:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("image_out", "status_text")
    FUNCTION = "check"
    CATEGORY = "utils"

    def check(self, image):
        has_white = image.max().item() > 0
        if has_white:
            return (image, "True")
        else:
            return (None, "False")


NODE_CLASS_MAPPINGS = {
    "ImageIfNotBlack": ImageIfNotBlack
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageIfNotBlack": "Image If Not Black"
}
