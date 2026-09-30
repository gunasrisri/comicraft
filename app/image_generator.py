import os
import re
from pathlib import Path


def generate_image(image_prompt, panel_number):
    safe_name = re.sub(r"[^a-zA-Z0-9_-]", "_", image_prompt[:50])

    output_dir = Path("static/panels")
    output_dir.mkdir(parents=True, exist_ok=True)

    image_path = output_dir / f"panel_{panel_number}_{safe_name}.txt"

    with open(image_path, "w", encoding="utf-8") as file:
        file.write(f"Image prompt: {image_prompt}")

    return f"/static/panels/{image_path.name}"