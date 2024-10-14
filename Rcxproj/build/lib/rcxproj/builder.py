import subprocess
import os

class RCXProjBuilder:
    def __init__(self, project_info):
        self.project_info = project_info

    def build(self):
        # Define the output directories
        build_dir = './build'
        bin_dir = './bin'
        
        # Create the build and bin directories if they do not exist
        os.makedirs(build_dir, exist_ok=True)
        os.makedirs(bin_dir, exist_ok=True)

        # Prepare the source files and output path
        sources = " ".join(self.project_info['sources'])
        output = os.path.join(bin_dir, "main.out")  # Use os.path.join for portability
        compile_command = f"g++ {sources} -o {output}"

        print("Compiling sources...")
        result = subprocess.run(compile_command, shell=True)

        if result.returncode == 0:
            print(f"Build successful! Output in {output}")
        else:
            print(f"Build failed with return code: {result.returncode}")
