import argparse
import os
import tqdm
from panoptes_client import *


def get_all_dirs(p_path):
    list_of_dirs = []
    for x in os.scandir(p_path):
        if x.is_dir():
            list_of_dirs.append((x.path, x.name))
    return list_of_dirs


def get_files(dir, used_image_processing_notebook):
    list_of_files = []

    scanned_dir = dir
    if used_image_processing_notebook:
      scanned_dir = dir + '/processed'

    for x in os.scandir(scanned_dir):
        if x.is_file() and (x.name.endswith('.jpg') or x.name.endswith('.png')):
            list_of_files.append((x.name, x.path))
    return list_of_files


def create_subject_set(s_name, project_id):
  try:
    subject_set = SubjectSet()
    subject_set.links.project = project_id
    subject_set.display_name = s_name
    subject_set.name = s_name
    subject_set.save()
    return subject_set
  except Exception as e:
    print(e, 'Subject Set Already Exists')
    return None


def upload_subject(file, project_id):
  try:
    s = Subject()
    s.links.project = project_id
    s.add_location(file)
    s.metadata.update({'filename': file})
    s.save()
    return s
  except Exception as e:
    print(e, 'IN SAVE EXCEPTION')


def main():
  parser = argparse.ArgumentParser(description='Upload a subject set to a Zooniverse project.')
  parser.add_argument('path_to_folder', type=str, help='Path to the folder containing the subject images.')
  parser.add_argument('username', type=str, help='Your Zooniverse username.')
  parser.add_argument('password', type=str, help='Your Zooniverse password.')
  parser.add_argument('project_id', type=str, help='The ID of the Zooniverse project.')
  args = parser.parse_args()
  #this is where you will name your parent folder; in our example it would be 'AllMyTestSubjectSets/'
  p_path = args.path_to_folder

  #set this flag to false if you have not ran the image_processing notebook
  used_image_processing_notebook = True

  #inerst your username & password
  Panoptes.connect(username=args.username, password=args.password)

  #insert your project_id here as a number!
  project_id = int(args.project_id)

  project = Project.find(str(project_id))

  #process all dirs
  dirs = get_all_dirs(p_path)
  for d in dirs:
    print('processing: ', d[1])
    files = get_files(d[0], used_image_processing_notebook)
    sub_set = create_subject_set(d[1], project_id)
    project.reload()
    if sub_set != None:
      for f in tqdm.tqdm(files):
        new_subjects = []
        with Subject.async_saves():
          new_subjects.append(upload_subject(f[1], project_id))
        sub_set.add(new_subjects)


if __name__ == '__main__':
  main()
