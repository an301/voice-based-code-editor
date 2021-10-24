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


# def audioTranscript():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source)
#         audio_data = r.listen(source)
#     try:
#         text = r.recognize_google(audio_data)
#         return(text)
#     except Exception as e:
#         return('could not recognize audio')

@app.route('/', methods=['GET','POST'])
def index():
    spoken_txt=""
    return render_template('test.html', spoken_txt=spoken_txt)

# @app.route("/audioprocessing", methods=['GET','POST'])
# def audioprocessing():
#     if request.method=='GET':
#
#         spoken_txt=audioTranscript()
#         spoken_txt=spoken_txt.lower()
#         for loop in symbols_text:
#                 if loop in spoken_txt:
#                     spoken_txt=replace_str_with_char(loop,symbols_text[loop],spoken_txt)
#         return render_template('test.html', spoken_txt=spoken_txt)
#     else:
#         code_fragment=request.form["code"]
#         output = subprocess.check_output(["python","-c",code_fragment])
#         output = output.decode()
#         output = output.strip()
#         return render_template('output.html', output=output, code_fragment=code_fragment)

# @app.route("/test_upload_audio", methods=["GET","POST"])
# def test_upload_audio():
#     if request.method=="GET":
#         return render_template('upload_audio_recording.html')
#     else:
#         audio_file=request.files['uploaded_file']
#         # audio_file.save('audio.wav')
#         r = sr.Recognizer()
#         uploaded_audio=sr.AudioFile(audio_file)
#         print(uploaded_audio)
#         with uploaded_audio as source:
#             r.adjust_for_ambient_noise(source)
#             audio_data = r.record(source)
#         try:
#             text = r.recognize_google(audio_data)
#             print(text)
#             text = text.lower()
#             for loop in symbols_text:
#                 if loop in text:
#                     text = replace_str_with_char(loop, symbols_text[loop], text)
#             print(text)
#         except Exception as e:
#             print('could not recognize audio')
#         print(request.form)
#         print(request.files)
#         return request.form

@app.route("/test_javascript_audio_upload", methods=["GET","POST"])
def java_script_audio():
    if request.method=="GET":
        return render_template('index.html')
    else:
        audio_data=request.files['audio_data']
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
            output = subprocess.check_output(["python", "-c",text])
            output = output.decode()
            print(output)
        except Exception as e:
            print('could not recognize audio')
        # audio_data.save('audio.wav')
        print('file uploaded')
        return redirect('/')

if __name__=="__main__":
    app.run()
