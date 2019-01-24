from flask import Flask,request,jsonify,make_response,send_from_directory
import os
import json

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def upload():
    if request.method=='POST':
        files = request.files.getlist("file2")
        filename=request.form['usr']
        print(filename)
        if not os.path.exists('File0Save/'+str(filename)):
             os.makedirs('File0Save/'+str(filename))
        basePath='File0Save/'+str(filename)
        for file in files:
            file_name = file.filename
            filePath=os.path.join(basePath, file_name)
            file.save(filePath)
    res = make_response(jsonify(basePath+'/'+file_name))
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'POST'
    res.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return res


@app.route('/dld/',methods=['GET','POST'])
def DownLoad():
    if request.method == 'POST':
        filename1 = request.form['mydata']
        print(filename1)
    filename ='1.txt'
    directory = 'File0Save/'
    filepath=directory+filename
    res = make_response(filepath)
    # res=make_response(jsonify(filename))
    # print(send_from_directory(directory, filename, as_attachment=True))
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'POST'
    res.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    print(res)
    return res
    # mydata=request.get_data().decode('utf-8')
    # data = json.loads(mydata)
    # res = make_response(jsonify(data))
    # res.headers['Access-Control-Allow-Origin'] = '*'
    # res.headers['Access-Control-Allow-Methods'] = 'POST'
    # res.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    # return res

@app.route('/table/',methods=['GET','POST'])
def tab():
    mydata=[
        {'bh': "201801", 'xh': "1", 'xm': "张1", 'zw': "三阿卡1"},
        {'bh': "201802", 'xh': "2", 'xm': "张2", 'zw': "三阿卡2"},
        {'bh': "201803", 'xh': "3", 'xm': "张3", 'zw': "三阿卡3"},
        {'bh': "201804", 'xh': "4", 'xm': "张4", 'zw': "三阿卡4"},
    ]
    res = make_response(jsonify(mydata))
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'POST'
    res.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return res

if __name__ == '__main__':
    app.run('127.0.0.1',8080)