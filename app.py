from flask import Flask, render_template, request
import random 
import string

app = Flask(__name__)

def get_random(length,checklist):
    length=int(length)
    special= '!$&?'
    uc= ''.join((random.choice(string.ascii_letters.upper()) for i in range(length)))
    lc= ''.join((random.choice(string.ascii_letters.lower()) for i in range(length)))
    num= ''.join((random.choice(string.digits) for i in range(length)))
    sym= ''.join((random.choice(special) for i in range(length)))
  
    
    if checklist==['1']:
        return ''.join((random.choice(string.ascii_letters.upper()) for i in range(length)))
    
    if checklist==['2']:
        return ''.join((random.choice(string.ascii_letters.lower()) for i in range(length)))
    
    if checklist==['3']:
        return ''.join((random.choice(string.digits.upper()) for i in range(length)))
    
    if checklist==['4']:
        return ''.join((random.choice(special) for i in range(length)))
    
    if checklist==['1','2']:
        allcharacters = uc+lc
        return ''.join((random.choice(allcharacters) for i in range(length)))
    
    if checklist==['1','3']:
        allcharacters = uc + num
        return ''.join((random.choice(allcharacters) for i in range(length)))
        
    
    if checklist==['1','4']:
        allcharacters = uc + sym
        return ''.join((random.choice(allcharacters) for i in range(length)))
    
    if checklist==['2','3']:
        allcharacters = lc + num
        return ''.join((random.choice(allcharacters) for i in range(length)))
            
     
    
    if checklist==['2','4']:
        allcharacters = lc + sym
        return ''.join((random.choice(allcharacters) for i in range(length)))

        
    if checklist==['3','4']:
        allcharacters = num+ sym
        return''.join((random.choice(allcharacters) for i in range(length)))
        

    if checklist==['1','2','3']:
        allcharacters = uc+lc+ num
        return ''.join((random.choice(allcharacters) for i in range(length)))
    
    
    if checklist==['1','2','4']:
        allcharacters = uc+lc+ sym
        return ''.join((random.choice(allcharacters) for i in range(length)))
      
    
    if checklist==['1','3','4']:
        allcharacters = uc+num+sym
        return''.join((random.choice(allcharacters) for i in range(length)))
        
    
    if checklist==['2','3','4']:
        allcharacters = lc+num+sym
        return join((random.choice(allcharacters) for i in range(length)))
    
    allcharacters = uc+lc+num+sym
    return ''.join((random.choice(allcharacters) for i in range(length)))
        

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method== 'POST':
        length=request.form.get('select_len')
        checklist=request.form.getlist('cb')
        if length=='Choose':
            pw= get_random(8,checklist)
        else:
            pw=get_random(length, checklist)
        return render_template('index.html', pw=pw)
    return render_template('index.html', pw='')


if __name__ == '__main__':
    app.run()