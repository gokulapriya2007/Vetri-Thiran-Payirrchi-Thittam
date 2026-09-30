import os
from diffusers import StableDiffusionPipeline
def generate_images(prompt, panel_num=1):
    return generate_image(prompt, panel_num)

def generate_image(prompt: str, panel_num: int):
    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4"
    )

    image = pipe(prompt).images[0]

    os.makedirs("static/panels", exist_ok=True)

    image_path = f"static/panels/panel{panel_num}.png"
    image.save(image_path)

    return f"/static/panels/panel{panel_num}.png"

