import os
from pathlib import Path

os.system("chmod -R 0777 /model")

with open('/model/run.sh', 'w') as f:
    f.write("mkdir /model/result\n")

    f.write('cd /model/src/Deform_Conv\n')
    f.write('python setup.py build install\n')
    
    vids = os.listdir("/dataset")

    for vid in vids:
        Path(f"/model/results/{vid}").mkdir(parents=True, exist_ok=True)
        f.write(f"python3 /model/src/main.py --test_only --save_results --pre_train /model/model/LGFN_x4.pt --dir_demo /dataset --video_name {vid} --save_dir /model/result/{vid}\n")
        
    f.write("chmod -R 0777 /model\n")
    
os.system('chmod 0777 /model/run.sh')
os.system('sh /model/run.sh')
