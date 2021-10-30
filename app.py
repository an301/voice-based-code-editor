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
              'closer parentheses':')',
              'prince':'print',
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
              'multiplied by':'*',
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


#route
@app.route('/', methods=['GET','POST'])
def index():
    spoken_txt=""
    return redirect('/audio_test')


@app.route("/audio_test", methods=["GET","POST"])
def audio_test():
    if request.method=="GET":
        return render_template('audio_test.html')
    else:
        audio_data = request.files['audio_data']
        r = sr.Recognizer()
        uploaded_audio = sr.AudioFile(audio_data)
        with uploaded_audio as source:
            r.adjust_for_ambient_noise(source)
            audio_info = r.record(source)
        try:
            text = r.recognize_google(audio_info)
            text = text.lower()
            for loop in symbols_text:
                if loop in text:
                    text = replace_str_with_char(loop, symbols_text[loop], text)
            print(text)
            output = subprocess.check_output(["python", "-c", text])
            output = output.decode()
            return render_template('output.html',output=output,code_fragment=text)
        except Exception as e:
            return render_template('output.html',code_fragment='could not recognize audio',output='')


if __name__=="__main__":
    app.run()
