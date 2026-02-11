class ImageIfNotBlack:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }

    # اول STRING بعد IMAGE
    RETURN_TYPES = ("STRING", "IMAGE")
    RETURN_NAMES = ("status_text", "image_out")
    FUNCTION = "check"
    CATEGORY = "utils"

    def check(self, image):
        has_white = image.max().item() > 0

        if has_white:
            return ("True", image)
        else:
            return ("False", None)


NODE_CLASS_MAPPINGS = {
    "ImageIfNotBlack": ImageIfNotBlack
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageIfNotBlack": "Image If Not Black"
}
