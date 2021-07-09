from pathlib import Path
import random, shutil

source = "../isolador_vidro _dataset_ad/train/good"
dest = "./isolador_vidro/train/good"

pathlist = Path(source).glob('**/*.jpg')
nof_samples = 200

rc = []
for k, path in enumerate(pathlist):
    if k < nof_samples:
        rc.append(str(path)) # because path is object not string
    else:
        i = random.randint(0, k)
        if i < nof_samples:
            rc[i] = str(path)

print(len(rc))

for r in rc:
    shutil.move(r,dest+'/'+r.split('/')[-1])