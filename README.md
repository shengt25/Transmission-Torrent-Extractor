# Transmission-Torrent-Extractor
Extract torrent from transmission, with the original directory structure of the original tasks, makes re-adding tasks easier.  

Transmission种子提取器，用原任务的原目录结构存放，方便按照不同目录重新添加任务。

# What is this tool?

When you upgrade, re-install transmission or simply encountered some bugs. The tasks have to be emptied and add again.

Anyway, it's not easy because:

1. It's hard to find the original torrent files.  
2. The torrent files are there, but with random names. It's hard to recognize.  
3. The directory structure of download path is complex, while the torrent files are mixed together, which is inconvenient to add them into different directories in batch.  



This tool is to solve this problem. By matching the information of the torrent file and the resume file, it extracts the torrent file and saves it in a new place using the directory structure of the original task. 

Hope that helps you.



# How to use

1. Clone repository 
```
git clone https://github.com/shengt25/Transmission-Torrent-Extractor.git
```
2. Enter directory
```
cd Transmission-Torrent-Extractor
```
3. Run main.py via python3
```
python3 main.py
```

It will look for the default config directory of transmission, extract torrents to the `extract` folder along side the program. It will save them using the directory structure of the original task. Torrents that fail to match will be placed in the `extract/no_match` subdirectory.

If no config directory for transmission can be found, or you want to specify it manually, you need to:

1. Open `main.py` for editing
2. Set `manually = True`
3. Edit the `resume_file_path` and `torrent_file_path`
4. Run it again

(It can only find the default config directory for Linux version for now)

# Thanks
This program use bencode_open to process torrent and resume files.  
bencode_open is an open-source MIT-licensed library, refer to: https://github.com/imachug/bencode-open


# 这是做什么的？

由于Transmission升级、重装或者出了什么bug，想要把任务清空，全部重新添加一遍？

但是你遇到了这些问题：

1. 没有找到种子文件保存在哪

2. 找到了transmission保存的种子文件，但是名字不是原文件名了，难以辨认。

3. 任务的目录结构复杂，种子文件混在一起，不方便批量分类添加。



这个工具就是来解决这个问题的，他通过匹配torrent文件和resume文件的信息，使用原任务的目录结构，将种子文件提取出来，保存在一个新地方。希望有所帮助。



# 如何使用
1. 克隆项目
```
git clone https://github.com/shengt25/Transmission-Torrent-Extractor.git
```
2. 打开目录
```
cd Transmission-Torrent-Extractor
```
3. 使用python3运行main.py
```
python3 main.py
```
   

他会在transmission的默认配置目录寻找信息，提取到程序所在目录的`extract`文件夹，使用原任务的目录结构保存。未能匹配的种子将放在`extract/no_match`子目录内。

如果没有能找到transmission的目录，或你想手动指定目录，则需要：

1. 打开`main.py`
2. 标记`manually = True`
3. 手动修改`resume_file_path`和`torrent_file_path`
4. 再次运行即可

（目前只做了查找Linux版本的默认目录）

# 感谢
本程序使用了bencode_open处理torrent和resume文件。  
bencode_open使用了MIT-licensed，项目地址：https://github.com/imachug/bencode-open
