import torch
from diffusers import StableDiffusionPipeline

model_id = "stable-diffusion-v1-5"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=True, torch_dtype=torch.float16,
                                               revision="fp16")
pipe = pipe.to(device)
prompt = "hawk, black wings, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, unreal engine 5, 8k"
pipe.enable_attention_slicing()
images = pipe(prompt).images
print(len(images))
for i, image in enumerate(images):
    image.save(f"output_{i}.png")