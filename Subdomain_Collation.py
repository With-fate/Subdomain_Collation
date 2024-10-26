import argparse
import glob
import os.path
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

logo =f"""{Fore.GREEN}
      .o8                    ooooooooo.                                                .   
     "888                    `888   `Y88.                                            .o8   
 .oooo888   .ooooo.           888   .d88'  .ooooo.  oo.ooooo.   .ooooo.   .oooo.   .o888oo 
d88' `888  d88' `88b          888ooo88P'  d88' `88b  888' `88b d88' `88b `P  )88b    888   
888   888  888ooo888 8888888  888`88b.    888ooo888  888   888 888ooo888  .oP"888    888   
888   888  888    .o          888  `88b.  888    .o  888   888 888    .o d8(  888    888 . 
`Y8bod88P" `Y8bod8P'         o888o  o888o `Y8bod8P'  888bod8P' `Y8bod8P' `Y888""8o   "888" 
                                                     888                                   
                                                    o888o                                  
                                                                                          
{Style.RESET_ALL}"""

print(logo)

def subdomain_collation(file_paths, output_file, np_flag):
    # 使用集合自动去重
    domains = set()
    print("正在整理...",end='')
    # 遍历所有文件路径
    for file_path in file_paths:
        with open(file_path, 'r') as f:
            # 逐行读取
            for line in f:
                # 去除每行前后的空白字符
                cleaned_line = line.strip()
                # 将每个文件中的子域名添加到集合中
                domains.update(cleaned_line.splitlines())

    print(f"\r{Fore.GREEN}--整理完成--{Style.RESET_ALL}")
    # 将去重的子域名写入输出文件
    if output_file and not np_flag:
        # 打印并输出
        with open(output_file, 'w') as f:
            for domain in sorted(domains):
                print(domain)
                f.write(domain + '\n')
        print(f"{Fore.GREEN}###按照要求打印并存入文件###{Style.RESET_ALL}")
    elif not output_file and not np_flag:
        # 只打印
        for domain in sorted(domains):
            print(domain)
        print(f"{Fore.GREEN}###按照要求只打印并没有存入文件###{Style.RESET_ALL}")
    elif output_file and np_flag:
        # 只输出
        with open(output_file, 'w') as f:
            for domain in sorted(domains):
                f.write(domain + '\n')
        print(f"{Fore.GREEN}###按照要求已经存入文件###{Style.RESET_ALL}")
    else:
        # 既不打印也不输出
        print(f"""{Fore.GREEN}
             .oooooo..o  o8o            oooo         .oooooo.  
            d8P'    `Y8  `"'            `888        dP'   `Y8b 
            Y88bo.      oooo   .ooooo.   888  oooo  88o   .d8P 
             `"Y8888o.  `888  d88' `"Y8  888 .8P'   `"' .d8P'  
                 `"Y88b  888  888        888888.       `88'    
            oo     .d8P  888  888   .o8  888 `88b.     .o.     
            8""88888P'  o888o `Y8bod8P' o888o o888o    Y8P     
                                                                                                           
                {Style.RESET_ALL}""")


def main():
    global np_flag
    parser = argparse.ArgumentParser(description='合并多个子域名文件并去重')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--files', nargs='+', help="子域名文件列表(!请确保文件与文件中的域名格式都相同，且每行只有一个域名!)")
    group.add_argument('-d', '--directory', help="包含子域名的目录(只会选中目录中的txt文件)")
    now = datetime.now()
    formatted_now = now.strftime("%Y-%m-%d_%H-%M-%S")
    parser.add_argument('-o', '--output', help="输出文件(默认输出在output目录下)", default='./output/'+formatted_now+'.txt')
    parser.add_argument('-no', '--no_output', action='store_true', help="只打印不输出")
    parser.add_argument('-np', '--no_print', action='store_true', help="只输出不打印")
    args = parser.parse_args()

    # 检查-d 是否提供了目录参数
    if args.directory:
        # 列出目录下的所有txt文件
        file_paths = glob.glob(os.path.join(args.directory, '*.txt'))
        if not file_paths:
            parser.error("目录中没有找到任何txt文件")
    else:
        # 使用提供的文件列表
        file_paths = args.files

    # 检查-no -np 是否打印||输出
    if not args.no_output and not args.no_print:
        # 打印且输出
        np_flag = False
        # 检查-o 输出路径，确保有效
        output_dir = os.path.dirname(args.output)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output = args.output
    elif args.no_output and not args.no_print:
        # 只打印
        np_flag = False
        output = []
    elif not args.no_output and  args.no_print:
        # 只输出
        np_flag = True
        # 检查-o 输出路径，确保有效
        output_dir = os.path.dirname(args.output)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output = args.output
    else:
        # 既不打印也不输出
        np_flag = True
        output = []

    # 调用处理文件
    subdomain_collation(file_paths, output, np_flag)


if __name__ == '__main__':
    main()
