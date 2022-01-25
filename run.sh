cd /model/src/Deform_Conv
python setup.py build install
mkdir /results/gauss
python3 /model/src/main.py --test_only --save_results --pre_train /model/model/LGFN_x4.pt --dir_demo /dataset --video_name gauss --save_dir /results/gauss
mkdir /results/bicubic
python3 /model/src/main.py --test_only --save_results --pre_train /model/model/LGFN_x4.pt --dir_demo /dataset --video_name bicubic --save_dir /results/bicubic
