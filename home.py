from flask import Flask, render_template, redirect
app = Flask(__name__)

#############################
# Home page                 #
#############################

@app.route('/', methods=['GET', 'POST'])
def home():
  return render_template('index.html')
  
  
  
##############################
# App launcher               #
############################## 

if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=5050)

