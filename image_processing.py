
import argparse
import os
import tqdm


def get_all_dirs(p_path):
    list_of_dirs = []
    for x in os.scandir(p_path):
        if x.is_dir():
            list_of_dirs.append(x.path)
    return list_of_dirs


def get_files(dir):
    list_of_files = []
    for x in os.scandir(dir):
        if x.is_file() and (x.name.endswith('.jpg') or x.name.endswith('.png')):
            list_of_files.append((x.name, x.path))
    return list_of_files

def create_dir(dir):
    try:
        os.makedirs(dir)
    except OSError as o:
        print('error creating directory')
        print(o)

def convert_file(file, new_file):
    try:
        command = 'convert ' + file + ' -resize 950x950 -strip -auto-level ' + new_file
        os.system(command)
    except OSError as e:
        print('error converting file')
        print(e)


def main():
    parser = argparse.ArgumentParser(description='Process images in a specified folder.')
    parser.add_argument('path', type=str, help='Path to the folder containing images to be processed.')
    args = parser.parse_args()

    path = args.path

    #process all dirs
    dirs = get_all_dirs(path)
    for d in dirs:
        print('processing: ', d)
        create_dir(d + '/processed')
        files = get_files(d)
        for f in tqdm.tqdm(files):
            new_dir = d + '/processed'
            new_file = new_dir + '/' + f[0]
            convert_file(f[1], new_file)



if __name__ == '__main__':
    main()
