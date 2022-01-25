import os
from pathlib import Path


with open('/model/run.sh', 'w') as f:
    f.write('cd /model/src/Deform_Conv\n')
    f.write('python setup.py build install\n')
    
    vids = os.listdir("/dataset")

    for vid in vids:
        f.write(f"mkdir /results/{vid}\n")
        f.write(f"python3 /model/src/main.py --test_only --save_results --pre_train /model/model/LGFN_x4.pt --dir_demo /dataset --video_name {vid} --save_dir /results/{vid}\n")
        
    
os.system('sh /model/run.sh')
