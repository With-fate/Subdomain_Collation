# -
usage: Subdomain_Collation.py [-h] (-f FILES [FILES ...] | -d DIRECTORY) [-o OUTPUT] [-no] [-np]

合并多个子域名文件并去重

options:
  -h, --help            show this help message and exit
  -f FILES [FILES ...], --files FILES [FILES ...]
                        子域名文件列表(!请确保文件与文件中的域名格式都相同，且每行只有一个域名!)
  -d DIRECTORY, --directory DIRECTORY
                        包含子域名的目录(只会选中目录中的txt文件)
  -o OUTPUT, --output OUTPUT
                        输出文件(默认输出在output目录下)
  -no, --no_output      只打印不输出
  -np, --no_print       只输出不打印
