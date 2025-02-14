import subprocess, shutil, os

def create_exe(file_path):
    """
    Create a packed executable from the Python script.
    """
    exe_path = pyinstaller(file_path)
    if exe_path:
        upx(exe_path)
        clean_up(file_path)
        return exe_path + ".exe"

def pyinstaller(file_path):
    """
    Create a standalone executable from the Python script using PyInstaller.
    """
    output_directory = "dist"
    try:
        subprocess.run(
            ["pyinstaller", "--onefile", "--noconsole", "--distpath", output_directory, file_path],
            check=True
        )
        exe_name = os.path.splitext(os.path.basename(file_path))[0]
        exe_path = os.path.join(output_directory, exe_name)
        if os.path.exists(exe_path):
            final_path = os.path.join(os.getcwd(), exe_name)
            shutil.move(exe_path, final_path)
            print(f"Executable moved to the current directory as '{exe_name}'.")
            return final_path
        else:
            print("Error: Generated executable not found.")
            return None
    except subprocess.CalledProcessError as e:
        print(f"PyInstaller failed with error: {e}")
        return None

def upx(exe_path):
    """
    Pack the executable using UPX.
    TODO: use rPack
    """
    try:
        subprocess.run(["upx", "--best", "--lzma", exe_path], check=True)
        print(f"Executable compressed using UPX and saved as '{exe_path}'.")
    except subprocess.CalledProcessError as e:
        print(f"UPX compression failed with error: {e}")

def clean_up(file_path):
    """
    Clean up temporary files and directories created during the build process.
    """
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    spec_file = f"{base_name}.spec"
    
    if os.path.exists("build"):
        shutil.rmtree("build")
    
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    
    if os.path.exists(spec_file):
        os.remove(spec_file)
    file_path = file_path[:-3]
    shutil.move(file_path, file_path + ".exe")
    print("Cleanup completed successfully.")
