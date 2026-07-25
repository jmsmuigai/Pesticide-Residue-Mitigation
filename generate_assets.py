"""
SafePlate Kenya v2 Image Asset Generation Script
Invokes the Gemini API / Nano banana image generation agent to create 22 visual assets.
"""

import os
import shutil
import glob
from safeplate_platform.gemini_agent import SafePlateGeminiAgent

def generate_and_sync_assets():
    print("=== SafePlate Image Asset Pipeline ===")
    agent = SafePlateGeminiAgent()
    prompts = agent.execute_task_1_image_prompts()
    print(f"Generated {len(prompts)} image prompt manifests:")
    for p in prompts:
        print(f" - [{p['id']}]: {p['prompt'][:70]}...")

    os.makedirs("assets/images", exist_ok=True)
    images = glob.glob("assets/images/*.png")
    print(f"Current asset suite has {len(images)} active image files in assets/images/")
    return len(images)

if __name__ == "__main__":
    generate_and_sync_assets()
