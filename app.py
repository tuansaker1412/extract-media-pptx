# copyright by tuansaker1412

import os
import shutil
import zipfile
import secrets

from distutils.dir_util import copy_tree

print("Drop file ppt or pptx in here:")
url_file = input().strip(' ').strip('\'')
print("Processing...")
base_url = os.path.abspath(os.curdir)

shutil.copy(url_file, base_url + '/tuansaker1412.zip')

with zipfile.ZipFile(base_url + '/tuansaker1412.zip', 'r') as zip_ref:
  zip_ref.extractall(base_url + '/tuansaker1412/')

os.remove(base_url + '/tuansaker1412.zip')

copy_tree(base_url + '/tuansaker1412/ppt/media/', base_url + '/media-' + secrets.token_hex(16) + '/')

shutil.rmtree(base_url + '/tuansaker1412/', ignore_errors=True)

print("Done!!!")
