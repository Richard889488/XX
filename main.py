from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    two = random.randrange(1,9,1)
    one = random.randrange(2,9,1)
    text = F'{one}X{two}='  # 假設要顯示的數字是42
    
    ans = one*two
    
    if request.method == 'POST':
        # 获取用户在输入框中输入的值
        input_text = request.form['input_text']
        # 在控制台上打印输入的值
        name = int(input_text)
        image_url = "ok.jpg"  # 图片的URL或文件路径
        
        print(input_text)
        if  ans==name  :
            return render_template('index.html', text=text,number="答對了")
        elif input_text == '18852311':
            return render_template('index.html', text=text,number="暗號成功，你是人")
        elif input_text == '09487':
            return render_template('index.html', text=text,number="別亂罵人，謝謝配合，請勿亂搞")
        elif input_text == '87':
            return render_template('index.html', text=text,number="趕快練習不需要罵我")

        else:
            number = F"正確答案:{ans}"
            return render_template('index.html', text=text,number=number,image_url=image_url)
        
            
        
        #print(F"答案是:{ans}")
        
            
    
    else:
        return render_template('index.html')
    
    

if __name__ == '__main__':
    app.run()

    
    