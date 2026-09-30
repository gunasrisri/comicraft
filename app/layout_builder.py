def build_comic_layout(outline, story, image_paths):
    layout = []

    for i, panel in enumerate(outline):
        layout.append({
            "panel": panel["panel"],
            "title": panel["title"],
            "scene": panel["scene"],
            "image_path": image_paths[i],
            "caption": story
        })

    return layout