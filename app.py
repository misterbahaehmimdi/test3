from flask import Flask
app = Flask(__name__)
import wget
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/check/check')
def check():
    wget.download("https://testi123.pythonanywhere.com/static/datacheck.xlsx")
    data = pd.read_excel("datacheck.xlsx")
    jj=-1
    while not jj==data.shape[0]:
     jj=jj+1
     ii=-1
     if jj==data.shape[0]:
            break
     nm=data.at[jj,'name']
     print("-+-+-+",nm,"-+-+-+-+",data.at[jj,'name'])

     if not type(nm)==type(""):
         nm=str(nm)
     data2 = pd.read_excel("/home/testi123/mysite/static/data"+nm+".xlsx")
     rr=requests.get(data.at[jj,'url']).text
     while not ii==data2.shape[0]:
        ii=ii+1
        if ii==data2.shape[0]:
            break
        if data2.at[ii,'text'].replace("\n","#012") in rr.replace("\\n","#012").replace("\#012","#012"):
         data2.at[ii,'statut']=1
        else:
         data2.at[ii,'statut']=0

     data2.to_excel("/home/testi123/mysite/static/data"+nm+".xlsx",index=False)
    return "done"
