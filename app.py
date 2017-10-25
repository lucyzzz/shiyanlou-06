# coding : utf-8
from flask import Flask ,render_template
import os
import json


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

@app.route('/')
def index():
    title_list = []
    for filename in os.listdir(): #迭代目录下的文件
        name ,ext =os.path.splitext(filename)  #获取文件后缀
        if ext == '.json':    #如果后缀为.json
            with open(filename) as file:
                dict = json.load(file)
                title_list.append(dict['title'])
    return render_template("index.html",title_list=title_list)

    # 显示文章名称的列表
    # 页面中需要显示 `/home/shiyanlou/files/` 目录下所有 json 文件中的 `title` 信息列表

@app.route('/files/<filename>')
def file(filename):
    default_suffix = '.json'
    filename = filename+default_suffix
    if not os.path.isfile(filename):
        return not_found(404)
    with open(filename) as file:
        return render_template("file.html",info=json.load(file).items())


if __name__ == "__main__":
    app.run(port=3000,debug=True)