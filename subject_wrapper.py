import argparse
import subprocess

def main(args):
    # Paths to the scripts - adjust these as needed
    image_processing_script = 'image_processing.py'
    subject_set_upload_script = 'subject_set_upload.py'
    
    # Running the image processing script
    try:
        print("Running image processing...")
        subprocess.run(["python", image_processing_script, args.path_to_folder], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {image_processing_script}: {e}")
        return
    
    # Running the subject set upload script
    try:
        print("Running subject set upload...")
        subprocess.run(["python", subject_set_upload_script, args.path_to_folder, args.username, args.password, args.project_id], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {subject_set_upload_script}: {e}")
        return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run image processing and subject set uploading scripts in sequence.")
    parser.add_argument("path_to_folder", help="Path to the folder containing images to be processed.")
    parser.add_argument("username", help="Username for subject set upload script.")
    parser.add_argument("password", help="Password for subject set upload script.")
    parser.add_argument("project_id", help="Project ID for subject set upload script.")
    
    args = parser.parse_args()
    main(args)
