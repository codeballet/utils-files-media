import os
import subprocess

def main():
    # Get info from user
    directory = input("Path for files: ")
    
    for filename in os.listdir(directory):
        # extract file prefix and suffix
        file_parts = filename.split('.')
        prefix = file_parts[0]

        subprocess.call(
            # 422 HQ
            # f"/usr/bin/ffmpeg -i {directory}/{filename} -c:v prores_ks -profile:v 3 -vendor apl0 -bits_per_mb 8000 -pix_fmt yuv422p10le -c:a copy {directory}/{prefix}.mov".split()
            
            # 422 Standard
            f"/usr/bin/ffmpeg -i {directory}/{filename} -c:v prores_ks -profile:v 2 -quant_mat 0 -vendor apl0 -pix_fmt yuv422p10le -c:a copy {directory}/{prefix}.mov".split()
            )


if __name__ == '__main__':
    main()
