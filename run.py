import os

os.system("chmod -R 0777 /model")

with open('/model/config.sh', 'w') as g:
    g.write('cd /model\n')
    g.write("chmod 0777 LGFN.sh\n")
    g.write('./LGFN.sh\n')

os.system('chmod 0777 /model/config.sh')
os.system('/model/config.sh')

with open('/model/run.sh', 'w') as f:
    f.write("mkdir result\n")
    
    vids = os.listdir("/dataset")

    for vid in vids:
        f.write(f"python3 /model/src/main.py --test_only --save_results --pre_train /model/model/LGFN_x4.pt --dir_demo /dataset --video_name {vid} --save_dir /model/result\n")
        
    f.write("chmod -R 0777 /model\n")
    
os.system('chmod 0777 /model/run.sh')
os.system('/model/run.sh')
