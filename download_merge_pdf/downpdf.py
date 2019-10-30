"""
功能：下载指定url内的所有的pdf
语法：将含有pdf的url放到脚本后面执行就可以了
"""

from bs4 import BeautifulSoup as Soup
from PyPDF2 import PdfFileReader, PdfFileWriter
from sys import argv
import requests
import os
import glob

try:
    ##用于获取命令行参数，argv[0]是脚本的名称
    root_url = argv[1]
except:
    print("please input url behind the script!!")
    exit()


##获得含有所有a标签的一个列表
def getTagA(root_url):
    res = requests.get(root_url)
    soup = Soup(res.text, 'html.parser')
    temp = soup.find_all("a")
    return temp


##从所有a标签中找到含有pdf的，然后下载
def downPdf(root_url, list_a):
    number = 0
    ##如果网站url是以类似xx/index.php格式结尾，那么只取最后一个/之前的部分
    if not root_url.endswith("/"):
        index = root_url.rfind("/")
        root_url = root_url[:index + 1]
    for name in list_a:
        name02 = name.get("href")
        ##筛选出以.pdf结尾的a标签
        if name02.lower().endswith(".pdf"):
            print("name:", name.string)
            print("name02", name02)
            pdf_name = name02
            number += 1
            print("Download the %d pdf immdiately \n " % number, end='  ')
            print(pdf_name + 'xdowning.....\n')
            ##因为要下载的是二进制流文件，将strem参数置为True
            print("root url is: %s" % root_url)
            print(root_url + pdf_name)
            response = requests.get(root_url + pdf_name, stream="TRUE")
            with open(str(number) + ".pdf", 'b') as file:
                for data in response.iter_content():
                    file.write(data)


def merger(output_path, input_paths):
    pdf_writer = PdfFileWriter()
    for path in input_paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)


if __name__ == "__main__":
    downPdf(root_url, getTagA(root_url))
    paths = glob.glob("*.pdf")
    paths.sort()
    merger('pdf_merger.pdf', paths)