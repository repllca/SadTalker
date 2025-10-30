import subprocess
import os

def run_inference(source_image: str, driven_audio: str) -> str:
    results_dir = "results"
    os.makedirs(results_dir, exist_ok=True)
    output_file = os.path.join(results_dir, f"{os.path.basename(source_image).split('.')[0]}_out.mp4")

    cmd = [
        "python3",
        "inference.py",
        "--source_image", source_image,
        "--driven_audio", driven_audio,
        "--result_dir", results_dir
    ]
    subprocess.run(cmd, check=True)
    return output_file
