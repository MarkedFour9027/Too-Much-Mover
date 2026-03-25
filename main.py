import os
import shutil

def get_paths(src_dir):

    items = []
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            full = os.path.join(root, file)
            rel = os.path.relpath(full, src_dir)
            items.append((full, rel))
    return items

def move_files_alternately(src1, src2, tgt1, tgt2):
    files1 = get_paths(src1)
    files2 = get_paths(src2)

    print(f"Found {len(files1)} files in {src1}")
    print(f"Found {len(files2)} files in {src2}")

    os.makedirs(tgt1, exist_ok=True)
    os.makedirs(tgt2, exist_ok=True)

    while files1 or files2:
        if files1:
            src_full, rel_path = files1.pop(0)
            dst_full = os.path.join(tgt1, rel_path)
            os.makedirs(os.path.dirname(dst_full), exist_ok=True)

            base, ext = os.path.splitext(dst_full)
            counter = 1
            while os.path.exists(dst_full):
                dst_full = f"{base}_{counter}{ext}"
                counter += 1

            shutil.move(src_full, dst_full)
            print(f"Moved: {src_full} -> {dst_full}")

        if files2:
            src_full, rel_path = files2.pop(0)
            dst_full = os.path.join(tgt2, rel_path)
            os.makedirs(os.path.dirname(dst_full), exist_ok=True)

            base, ext = os.path.splitext(dst_full)
            counter = 1
            while os.path.exists(dst_full):
                dst_full = f"{base}_{counter}{ext}"
                counter += 1

            shutil.move(src_full, dst_full)
            print(f"Moved: {src_full} -> {dst_full}")

    print("\nAll files have been moved.")

if __name__ == "__main__":
    src_A = input("Source A : ")
    src_B = input("Spurce B : ")
    target_A = input("Target A : ")
    target_B = input("Target B : ")
    

    move_files_alternately(src_A, src_B, target_A, target_B)