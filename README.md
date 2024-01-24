# Transmission-Torrent-Extractor
Extract torrent from transmission, with the original directory structure of the original tasks, makes re-adding tasks easier.  

Transmission种子提取器，用原任务的原目录结构存放，方便按照不同目录重新添加任务。

# What is this tool?

When you want to delete and re-add all the tasks in transmission (due to upgrading, re-install, etc.)
It's not easy because you might:  
1. lost the original torrent files  
2. find torrent files are with random names  
3. the torrent files are mixed together everywhere  

Then you can use this tool to extract torrent file with one click! It reads from transmission's internal data and save the files into to new folder, with the structure of the task folder. 

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

当你想清空trnsmission的所有任务，然后重新添加时，(由于升级，重装，等问题)
你可能会发现：
1. 种子文件已经删除
2. 种子文件名难以辨认
3. 种子文件混在一起，不方便批量分类添加。

那么，这个工具就是来解决这个问题的，他通过匹配torrent文件和resume文件的信息，使用原任务的目录结构，将种子文件提取出来，全部保存在新的文件夹中。希望有所帮助。



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
