import os, shutil, pathlib

orginal_dir = pathlib.Path("data")
new_base_dir = pathlib.Path("organic_vs_recycle_small")

def make_subset(subset_name, start_index, end_index):
    for category in ("O", "R"):
        dir = new_base_dir / subset_name / category
        os.makedirs(dir)
        fnames = [f"{category}_{i}.jpg" for i in range(start_index, end_index)]
        for fname in fnames:
            shutil.copyfile(src=orginal_dir / fname,
                            dst=dir / fname)

make_subset("train", 1000, 4000)
make_subset("validation", 4000, 6500)
make_subset("test", 6500, 8500)