# 7号词云：新时代中国特色社会主义（中国地图形状）

# 导入词云制作库wordcloud和中文分词库jieba
import jieba
import wordcloud

# 导入imageio库中的imread函数，并用这个函数读取本地图片，作为词云形状图片
import imageio
mk = imageio.imread("chinamap.png")

# 构建并配置词云对象w，注意要加scale参数，提高清晰度
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc',
                        mask=mk,
                        scale=15)

# 对来自外部文件的文本进行中文分词，得到string
f = open('毛概实践报告-潍科里面看小康.txt',encoding='utf-8')
txt = f.read()
txtlist = jieba.lcut(txt)
string = " ".join(txtlist)

# 将string变量传入w的generate()方法，给词云输入文字
w.generate(string)

# 将词云图片导出到当前文件夹
w.to_file('output7-chinamap.png')
