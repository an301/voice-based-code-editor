from flask import Flask,render_template,request,redirect
import speech_recognition as sr
import subprocess
app = Flask(__name__)

symbols_text={'open parentheses':'(',
              'close parentheses':')',
              'open parenthesis':'(',
              'close parenthesis':')',
              'opened parentheses':'(',
              'closed parentheses':')',
              'open square bracket':'[',
              'close square bracket':']',
              'open curly bracket':'{',
              'close curly bracket':'}',
              'open flower bracket':'{',
              'close flower bracket':'}',
              'comma':',',
              'semi colon':';',
              'semicolon':';',
              'colon':':',
              'double quote':'"',
              'single quote':"'",
              'greater than':'>',
              'less than':'<',
              'dot':'.',
              'period':'.',
              'forward slash':'/',
              'back space':'\b',
              'backspace':'\b',
              'new line':'\n',
              'newline':'\n',
              'question mark':'?',
              'asterisk':'*',
              'ampersand':'&',
              'percent':'%',
              'modulo':'%',
              'mod':'%',
              'percentage':'%',
              'hashtag':'#',
              'hash':'#',
              'exclamation':'!',
              'space':' ',
              'tab':'\t',
              'equals':'=',
              'equal':'=',
              'plus':'+',
              'minus':'-',
              'multiply':'*',
              'times':'*',
              'divide':'/',
              'divided by':'/'
              }

spoken_txt=''


def replace_str_with_char(key_word,symbol,spoken_txt):
    if key_word in spoken_txt:
        spoken_txt = spoken_txt.split(key_word)
        for loop in range(0, len(spoken_txt), 1):
            spoken_txt[loop] = spoken_txt[loop].strip()
        spoken_txt = symbol.join(spoken_txt)
    return(spoken_txt)


def audioTranscript():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio_data = r.listen(source)
    try:
        text = r.recognize_google(audio_data)
        return(text)
    except Exception as e:
        return('could not recognize audio')

@app.route('/', methods=['GET','POST'])
def index():
    spoken_txt=""
    return render_template('test.html', spoken_txt=spoken_txt)

@app.route("/audioprocessing", methods=['GET','POST'])
def audioprocessing():
    if request.method=='GET':

        spoken_txt=audioTranscript()
        spoken_txt=spoken_txt.lower()
        for loop in symbols_text:
                if loop in spoken_txt:
                    spoken_txt=replace_str_with_char(loop,symbols_text[loop],spoken_txt)
        return render_template('test.html', spoken_txt=spoken_txt)
    else:
        code_fragment=request.form["code"]
        output = subprocess.check_output(["python","-c",code_fragment])
        output = output.decode()
        output = output.strip()
        return render_template('output.html', output=output, code_fragment=code_fragment)

if __name__=="__main__":
    app.run()
