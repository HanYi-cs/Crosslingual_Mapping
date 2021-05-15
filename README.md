# Crosslingual_Mapping
维基百科的下载地址
https://dumps.wikimedia.org/zhwiki/
https://dumps.wikimedia.org/jawiki/
从压缩包中解压出数据
python WikiExtractor.py -b 250M -o wiki_zh zhwiki-20210420-pages-articles-multistream.xml.bz2
python WikiExtractor.py -b 250M -o wiki_ja jawiki-20210420-pages-articles-multistream.xml.bz2
使用open.cc将繁体转换为简体
opencc -i wiki_03 -o zhwiki_jian_zh.txt -c t2s.json
