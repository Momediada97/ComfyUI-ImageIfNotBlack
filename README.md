# ComfyUI-ImageIfNotBlack

A lightweight custom node for ComfyUI that detects whether an input image is completely black.

## Features

- If the image contains any non-zero pixel → returns the original image and `"True"`
- If the image is fully black → returns an empty image and `"False"`
- Safe output (prevents pipeline crashes)
- No external dependencies

---

## Installation

Clone into your ComfyUI `custom_nodes` folder:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Momediada97/ComfyUI-ImageIfNotBlack.git
