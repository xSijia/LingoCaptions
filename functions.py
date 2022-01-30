import csv
from tkinter import *
from threading import *
import json
import time
import tkinter.font as tkFont
import tkinter as tk
from pypinyin import pinyin
import pykakasi
kks = pykakasi.kakasi()

try:
    import azure.cognitiveservices.speech as speechsdk
except ImportError:
    print("""
    Importing the Speech SDK for Python failed.
    Refer to
    https://docs.microsoft.com/azure/cognitive-services/speech-service/quickstart-python for
    installation instructions.
    """)
    import sys
    sys.exit(1)

speech_key, service_region = "0f1dd8e11efb4c87b72f72506dabdec2", "eastus"
langCodes = {}
langCodesSource = {}
caption_windows = {}
resJSON = ""
roman = None
listening = None


def setResJson(resJSON):
    for translations in resJSON['Translation']['Translations']:
        if translations['Language'] in caption_windows:
            text = translations['Text']
            if translations['Language'] == 'zh-Hans' and roman.get() == 1:
                text = ' '.join([p[0] for p in pinyin(text)]) + '\n' + text
            if translations['Language'] == 'ja' and roman.get() == 1:
                text = ' '.join([p['hepburn'] for p in kks.convert(text)]) + '\n' + text
            caption_windows[translations['Language']].label.delete(1.0, "end")
            caption_windows[translations['Language']].label.insert(1.0, text)
            caption_windows[translations['Language']].label.tag_add('ok', 1.0, "end")
        print(translations['Language'] + ":     " + translations['Text'])
        # Label(newWindow,
        #       text=translations['Language'] + ":     " + translations['Text']).pack()


def increase(window):
    window.fontsize = window.fontsize + 1
    window.label.config(font=('Arial', window.fontsize))


def decrease(window):
    window.fontsize = window.fontsize - 1
    window.label.config(font=('Arial', window.fontsize))


def on_closing(window, output):
    if langCodes[output.get()] in caption_windows:
        del caption_windows[langCodes[output.get()]]
    window.destroy()

def openNewCapWindow(outputs, master):
    for output in outputs:
        if langCodes[output.get()] not in caption_windows:
            #print(output.get())
            # Toplevel object which will
            # be treated as a new window
            newWindow = Toplevel(master)
            newWindow.attributes('-alpha', 0.85)

            # sets the title of the
            # Toplevel widget
            newWindow.title(output.get())

            # sets the geometry of toplevel
            newWindow.geometry("600x70")
            fontFrame = Frame(newWindow)
            fontFrame.pack()


            newWindow.label = Text(newWindow)
            newWindow.label.tag_config("ok",justify='center')
            #newWindow.label.configure(state="disabled")
            #newWindow.label.insert(1.0, 'ergvfdsvvgfcdgtf')

            newWindow.fontsize = 14

            newWindow.label.configure(bg=newWindow.cget('bg'), relief="flat", font=('Arial', newWindow.fontsize))
            increaseTxtSizeBtn = Button(fontFrame,
                                text="+",
                                command=lambda w=newWindow: increase(w))
            increaseTxtSizeBtn.pack(side=LEFT)
            decreaseTxtSizeBtn = Button(fontFrame,
                                text="-",
                                command=lambda w=newWindow: decrease(w))
            decreaseTxtSizeBtn.pack(side=LEFT)


            caption_windows[langCodes[output.get()]] = newWindow

            #newWindow.var = StringVar()
            #newWindow.label = Label(newWindow,
            #                       textvariable=newWindow.var)

            newWindow.label.pack()

            newWindow.protocol("WM_DELETE_WINDOW", lambda w=newWindow, o=output: on_closing(w, o))

            # A Label widget to show in toplevel


def loadlangcode():
    reader = csv.reader(open('languagecodes.csv'))
    global langCodes
    langCodes = {}
    for row in reader:  # skip first row
        key = row[0]
        if key in langCodes:
            # implement your duplicate row handling here
            pass
        langCodes[key] = row[1]
    reader = csv.reader(open('srclanguagecodes.csv'))
    global langCodesSource
    langCodesSource = {}
    for row in reader:  # skip first row
        key = row[0]
        if key in langCodesSource:
            # implement your duplicate row handling here
            pass
        langCodesSource[key] = row[1]
    return langCodes, langCodesSource


def loadRomanCheckbox(master):
    global roman
    roman = IntVar()
    romanbtn = Checkbutton(master, text="Romantization On\n(Chinese & Japanese Only)", variable=roman,
                           onvalue=1,
                           offvalue=0)
    romanbtn.pack(pady=5)

def loadListenCheckbox(master, callback):
    global listening
    listening = IntVar()
    listenbox = Checkbutton(master, text="Listener\n(Retoggle when Necessary)", variable=listening,
                            command=callback,
                            onvalue=1,
                            offvalue=0)
    listenbox.pack(pady=5)

"""def NativeCapCheckbox(master):
    roman = IntVar()
    romanbtn = Checkbutton(master, text="Romantization On\n(Chinese & Japanese Only)", variable=roman,
                           onvalue=1,
                           offvalue=0)
    romanbtn.pack(pady=5)"""


def loadSourceDropDown(master):
    # Dropdown menu options
    _, source = loadlangcode()
    # datatype of menu text
    sourcecli = StringVar()

    # initial menu text
    sourcecli.set("English (United States)")

    # Create Dropdown menu
    dropsource = OptionMenu(master, sourcecli,  *source)
    dropsource.pack()

    return sourcecli


def loadOutDropDown(master):
    # Dropdown menu options
    output, _ = loadlangcode()

    # datatype of menu text
    outclicked = StringVar()
    outclicked.set("Source")

    dropoutput = OptionMenu(master, outclicked, *output)
    dropoutput.pack()

    return outclicked

def loadOutDropDownEng(master):
    # Dropdown menu options
    output, _ = loadlangcode()

    # datatype of menu text
    outclicked = StringVar()
    outclicked.set("English")

    dropoutput = OptionMenu(master, outclicked, *output)
    dropoutput.pack()

    return outclicked


def sourceshow(label, sourcecli):
    label.config(text=sourcecli.get())


def outshow(label, outclicked):
    label.config(text=outclicked.get())


def threading(source, outputs):
    if listening.get() == 1:
        i = langCodesSource[source.get()]
        j = [langCodes[output.get()] for output in outputs]
        print(i, j)
        # Call work function
        t1 = Thread(target=lambda: translation_continuous_from_mic(i, j))
        t1.start()

"""
# work function
def translate():
    pass
    #resJSON = json.loads(evt.result.json)
    #print(resJSON['Text'])

    #for translations in resJSON['Translation']['Translations']:
    #    print(translations['Language'] + ":     " + translations['Text'])


def threadWin(master):
    threading()
    openNewCapWindow(master)"""

def translation_continuous_from_mic(source, outputs):
    """performs continuous speech translation from input from an audio file"""
    # <TranslationContinuous>
    # set up translation parameters: source language and target languages
    translation_config = speechsdk.translation.SpeechTranslationConfig(
        subscription=speech_key, region=service_region,
        speech_recognition_language=source,
        target_languages=outputs, voice_name="de-DE-Hedda")

    # audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    audio_config = speechsdk.audio.AudioConfig(device_name='BlackHole2ch_UID')

    # Creates a translation recognizer using and audio file as input.
    recognizer = speechsdk.translation.TranslationRecognizer(
        translation_config=translation_config, audio_config=audio_config)

    def result_callback(event_type, evt):
        resJSON = json.loads(evt.result.json)
        setResJson(resJSON)
        # for translations in resJSON['Translation']['Translations']:
        #     print(translations['Language'] + ":     " + translations['Text'])
        """callback to display a translation result"""
        #print("{}: {}\n\tTranslations: {}\n\tResult Json: {}".format(
        #    event_type, evt, evt.result.translations.items(), evt.result.json))

    def stop_cb(evt):
        """callback that signals to stop continuous recognition upon receiving an event `evt`"""
        print('CLOSING on {}'.format(evt))
        listening.set(0)

    # connect callback functions to the events fired by the recognizer
    recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    # event for intermediate results
    recognizer.recognizing.connect(lambda evt: result_callback('RECOGNIZING', evt))
    # event for final result
    recognizer.recognized.connect(lambda evt: result_callback('RECOGNIZED', evt))
    # cancellation event
    recognizer.canceled.connect(lambda evt: print('CANCELED: {} ({})'.format(evt, evt.reason)))

    # stop continuous recognition on either session stopped or canceled events
    recognizer.session_stopped.connect(stop_cb)
    recognizer.canceled.connect(stop_cb)

    def synthesis_callback(evt):
        """
        callback for the synthesis event
        """
        #print('SYNTHESIZING {}\n\treceived {} bytes of audio. Reason: {}'.format(
        #    evt, len(evt.result.audio), evt.result.reason))
        pass

    # connect callback to the synthesis event
    recognizer.synthesizing.connect(synthesis_callback)

    # start translation
    recognizer.start_continuous_recognition()
    while listening.get() == 1:
        time.sleep(.5)

    print('stopping')
    recognizer.stop_continuous_recognition()
    global caption_windows
    for window in caption_windows.values():
        window.destroy()
    caption_windows = {}
    # </TranslationContinuous>
