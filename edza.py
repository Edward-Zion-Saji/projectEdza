import datetime
import pyttsx3
import random
import speech_recognition as sr
import webbrowser
import wikipedia
import winsound
from time import strftime

import wolframalpha
import wx
import wx.html
import wx.html2


class MyBrowser(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle('Edza-Web')
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        # Element Variables
        self.browser = wx.html2.WebView.New(self)
        self.address = wx.TextCtrl(self, value="", size=(500, 26))
        self.go = wx.Button(self, label="Go", id=wx.ID_OK)
        self.back = wx.Button(self, label="Back")
        self.forward = wx.Button(self, label="Forward")
        self.reload = wx.Button(self, label="Refresh")
        self.result = None
        self.Maximize(True)
        # Nav area
        addressarea = wx.BoxSizer()
        addressarea.Add(self.address, proportion=1, border=0)
        addressarea.Add(self.go, proportion=0, border=0)
        addressarea.Add(self.back, proportion=0, border=0)
        addressarea.Add(self.forward, proportion=0, border=0)
        addressarea.Add(self.reload, proportion=0, border=0)
        # adding elements
        sizer.Add(addressarea, proportion=0, flag=wx.EXPAND, border=0)
        sizer.Add(self.browser, 1, wx.EXPAND, 10)
        # button binding
        self.Bind(wx.EVT_BUTTON, self.OnGo, id=wx.ID_OK)
        self.Bind(wx.EVT_BUTTON, self.OnBack, self.back)
        self.Bind(wx.EVT_BUTTON, self.OnForward, self.forward)
        self.Bind(wx.EVT_BUTTON, self.OnReload, self.reload)

        # File Menu
        self.fileMenu = wx.Menu()
        self.New = self.fileMenu.Append(wx.ID_ANY, 'New Window')
        self.Exit = self.fileMenu.Append(wx.ID_ANY, 'Exit')
        self.Bind(wx.EVT_MENU, self.OnNew, self.New)
        self.Bind(wx.EVT_MENU, self.OnCloseWindow, self.Exit)
        # Help Menu
        self.helpMenu = wx.Menu()
        self.Help = self.helpMenu.Append(wx.ID_ANY, 'Help')
        self.About = self.helpMenu.Append(wx.ID_ANY, 'About Edza-Web')
        self.Bind(wx.EVT_MENU, self.OnHelp, self.Help)
        self.Bind(wx.EVT_MENU, self.OnAbout, self.About)
        # Adding the actual Menu Bar
        self.menuBar = wx.MenuBar()
        self.menuBar.Append(self.fileMenu, 'File')
        self.menuBar.Append(self.helpMenu, 'Help')
        self.SetMenuBar(self.menuBar)

        self.SetSizer(sizer)
        self.SetSize((1000, 700))

    def OnBack(self, event):
        self.browser.GoBack()

    def OnForward(self, event):
        self.browser.GoForward()

    def OnGo(self, event):
        self.result = self.address.GetValue()
        self.browser.LoadURL(self.result)

    def OnReload(self, event):
        self.browser.Reload()

    def OnNew(self, event):
        if __name__ == '__main__':
            app = wx.App()
            dialog = MyBrowser(None, -1)
            dialog.browser.LoadURL("http://www.google.com")
            dialog.Show()
            app.MainLoop()

    @staticmethod
    def OnHelp(event):
        helpDlg = HelpDlg(None)
        helpDlg.Show()

    def OnAbout(self, event):
        aboutDlg = AboutDlg(None)
        aboutDlg.Show()

    def OnCloseWindow(self, event):
        self.Destroy()


# About Menu Dialog HTMl Style
class AboutDlg(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, wx.ID_ANY, title="About", size=(400, 400))

        html = wxHTML(self)

        html.SetPage(

            "<h2>Edza-Web</h2>"

            "<p>Thanks for trying out this web browser, It's nothing big yet, but we can dream right? </p>"

            "<p><b>Python, Browser, and WxPython</b></p>"

            '<p>WxPython is the GUI back end that runs this program</p>'

            '<p>Python is the programing language of this program and browser is the functions of this program.</p>'

            '<p>This Sotware is completely licenced under Apache 2.0 and the source code is available on GitHub</p>'

        )


class HelpDlg(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, wx.ID_ANY, title="About", size=(400, 400))

        html = wxHTML(self)

        html.SetPage(
            ''

            "<h2>Edza-Web Help</h2>"

            "<p>Thanks for trying out this web browser, It's nothing big yet, but we can dream right?"

            "<p>Not much to be said about usage as it pretty self explanatory if you ever use a computer.</p>"

            "<p>Go to any site by typing in the address and pressing go.</p>"



            '<p>Thank\'s again for this software!</p>'
        )


class wxHTML(wx.html.HtmlWindow):
    def OnLinkClicked(self, link):
        webbrowser.open(link.GetHref())


class AboutDlgMain(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, wx.ID_ANY, title="About", size=(400, 400))

        html = wxHTML(self)

        html.SetPage(

            "<h2>Edza-Personal Digital Assistant</h2>"

            "<p>Ai Assistant and Q/A </p>"

            "<p>Created by <b>Edward Zion Saji.</b></p>"

            '<p>Licenced under Apache 2.0</p>'
            
            '<p>WxPython is the GUI back end that runs this program</p>'

            '<p>Python is the programing language of this program.</p>'

            '<p>Version: v2.12</b></p>'
        
            '<p> This software is free to use and redistribute and is an open source project. Source code available at GitHub.</p>')


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
                          pos=wx.DefaultPosition, size=wx.Size(1200, 627),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
                          wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                          title="Edza-Personal Assistant")
        panel = wx.Panel(self)
        image_file = 'ai3.png'
        bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap1 = wx.StaticBitmap(self, -1, bmp1, (0, 0))
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(self.bitmap1,
                            label="Hello I am Edza, Your Personal Digital Assistant. How can I help you?", pos=(280, 10))
        lbl.SetForegroundColour('pink')
        lbl.SetBackgroundColour('black')
        my_sizer.Add(lbl, 0, wx.ALL, 40)
        font1 = wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'arial')
        lbl.SetFont(font1)
        self.txt = wx.TextCtrl(self.bitmap1, style=wx.TE_PROCESS_ENTER, size=(700, 30), pos=(250, 545))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        font2 = wx.Font(14, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'arial')
        self.txt.SetFont(font2)
        panel.SetSizer(my_sizer)
        bmp = wx.Bitmap("mic3.jpg", wx.BITMAP_TYPE_ANY)
        self.button = wx.BitmapButton(self.bitmap1, id=wx.ID_ANY, bitmap=bmp,
                                      size=(bmp.GetWidth() + 10, bmp.GetHeight() + 10), pos=(960, 540))
        self.button.Bind(wx.EVT_BUTTON, self.onButton)
        bmp2 = wx.Bitmap("abcd.jpg", wx.BITMAP_TYPE_ANY)
        self.button2 = wx.BitmapButton(self.bitmap1, id=wx.ID_ANY, bitmap=bmp2,
                                      size=(bmp2.GetWidth() + 10, bmp2.GetHeight() + 10), pos=(1100, 5))
        self.button2.Bind(wx.EVT_BUTTON, self.onAbout)
        bmp3 = wx.Bitmap("aaa.jpg", wx.BITMAP_TYPE_ANY)
        self.button2 = wx.BitmapButton(self.bitmap1, id=wx.ID_ANY, bitmap=bmp3,
                                       size=(bmp3.GetWidth() + 10, bmp3.GetHeight() + 10), pos=(5, 5))
        self.button2.Bind(wx.EVT_BUTTON, self.onWeb)
        self.Show()

    @staticmethod
    def onAbout(event):
        aboutDlg1 = AboutDlgMain(None)
        aboutDlg1.Show()

    @staticmethod
    def onWeb(event):
         if __name__ == '__main__':
             app = wx.App()
             dialog = MyBrowser(None, -1)
             dialog.browser.LoadURL("http://www.google.com")
             dialog.Show()
             app.MainLoop()

    @staticmethod
    def onButton(event):
        now = datetime.datetime.now()
        frequency = 900
        duration = 500
        winsound.Beep(frequency, duration)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Tell me something:")
            audio = r.listen(source)
            try:
                print("You said:- " + r.recognize_google(audio))
            except sr.UnknownValueError:
                print("Could not understand audio")
        greetings = ['hey there', 'hello', 'hi', 'Hi', 'hey!', 'hey']
        question = ['how are you', 'how are you doing']
        responses = ['Okay', "I'm fine"]
        var1 = ['who made you', 'who created you']
        var2 = ['I_was_created_by_Edward_right_in_his_computer.', 'Edward', 'Some_guy_whom_i_never_got_to_know.']
        var3 = ['what time is it', 'what is the time', 'time']
        var4 = ['who are you', 'what is your name']
        cmd1 = ['open browser', 'open google', 'open the browser', 'open Google']
        cmd2 = ['play music', 'play songs', 'play a song', 'open music player']
        cmd3 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
        jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.',
                 'My dog used to chase people on a bike a lot.'
                 ' It got so bad, finally I had to take his bike away.',
                 'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']
        cmd4 = ['open youtube', 'i want to watch a video', 'open YouTube']
        cmd5 = ['tell me the weather', 'what is the weather', 'weather', 'what about the weather', 'how is the day',
                'how is the day today']
        cmd6 = ['exit', 'close', 'goodbye', 'nothing']
        cmd7 = ['what is your color', 'what is your colour', 'your color', 'your color?']
        colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']
        cmd8 = ['what is your favourite colour', 'what is your favourite color']
        cmd9 = ['thank you']
        repfr9 = ['your welcome', 'glad i could help you']
        abc = ('what can you do', 'do something')
        abcrep = 'I can tell the time, answer questions, tell the weather and much more. Just ask me'
        youcall = ['YouTube', 'youtube', 'YOUTUBE']
        data = ""
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        volume = engine.getProperty('volume')
        engine.setProperty('volume', 10.0)
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 50)

        def a():
            random_greeting = random.choice(greetings)
            print(random_greeting)
            engine.say(random_greeting)
            engine.runAndWait()

        def b():
            print(abcrep)
            engine.say(abcrep)
            engine.runAndWait()

        def c():
            engine.say('I am fine')
            engine.runAndWait()
            print('I am fine')

        def d():
            engine.say('I was made by edward')
            engine.runAndWait()
            reply = random.choice(var2)
            print(reply)

        def e():
            print(random.choice(repfr9))
            engine.say(random.choice(repfr9))
            engine.runAndWait()

        def f():
            print(random.choice(colrep))
            engine.say(random.choice(colrep))
            engine.runAndWait()
            print('It keeps changing every micro second')
            engine.say('It keeps changing every micro second')
            engine.runAndWait()

        def g():
            engine.say('I am edza your personal AI assistant')
            engine.runAndWait()

        def h():
            if __name__ == '__main__':
                app = wx.App()
                dialog = MyBrowser(None, -1)
                dialog.browser.LoadURL('www.youtube.com')
                dialog.Show()
                app.MainLoop()

        def i():
            print('see you later')
            engine.say('see you later')
            engine.runAndWait()
            exit()

        def j():
            print("Current time : ")
            print(strftime("The time is %H:%M"))
            engine.say(strftime("The time is %H:%M"))
            engine.runAndWait()

        def k():
            if __name__ == '__main__':
                app = wx.App()
                dialog = MyBrowser(None, -1)
                dialog.browser.LoadURL("http://www.google.com")
                dialog.Show()
                app.MainLoop()

        def l():
            data = r.recognize_google(audio)
            data = data.split()
            data = data[1:]
            L = ' '.join(data)
            if __name__ == '__main__':
                app = wx.App()
                dialog = MyBrowser(None, -1)
                dialog.browser.LoadURL('http://www.google.com/search?hl=en&q=' + L)
                dialog.Show()
                app.MainLoop()

        def m():
            data = r.recognize_google(audio)
            data = data.split()
            data = data[1:]
            L = ' '.join(data)
            if __name__ == '__main__':
                app = wx.App()
                dialog = MyBrowser(None, -1)
                dialog.browser.LoadURL('http://www.youtube.com/search?hl=en&q=' + L)
                dialog.Show()
                app.MainLoop()

        if r.recognize_google(audio) in greetings:
            a()
        elif r.recognize_google(audio) in abc:
            b()
        elif r.recognize_google(audio) in question:
            c()
        elif r.recognize_google(audio) in var1:
            d()
        elif r.recognize_google(audio) in cmd9:
            e()
        elif r.recognize_google(audio) in cmd7:
            f()
        elif r.recognize_google(audio) in cmd8:
            f()
        elif r.recognize_google(audio) in var4:
            g()
        elif r.recognize_google(audio) in cmd4:
            h()
        elif r.recognize_google(audio) in cmd6:
            i()
        elif r.recognize_google(audio) in var3:
            j()
        elif r.recognize_google(audio) in cmd1:
            k()
        elif 'Google' in r.recognize_google(audio):
            l()
        elif 'YouTube' in r.recognize_google(audio):
            m()

        else:
            try:
                app_id = "GJRQVK-GY36XW7K8H"
                client = wolframalpha.Client(app_id)
                res = client.query(r.recognize_google(audio))
                answer = next(res.results).text
                print(answer)
                engine.say(answer)
                engine.runAndWait()
            except:
                print(wikipedia.summary(r.recognize_google(audio)))
                engine.say(wikipedia.summary(r.recognize_google(audio)))
                engine.runAndWait()

    def OnEnter(self, event):
        user_input = self.txt.GetValue()

        # Variables and replies
        greetings = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey']
        question = ['how are you', 'how are you doing']
        responses = ['Okay', "I'm fine"]
        var1 = ['who made you', 'who created you']
        var2 = ['I_was_created_by_Edward_right_in_his_computer.', 'Edward', 'Some_guy_whom_i_never_got_to_know.']
        var3 = ['what time is it', 'what is the time', 'time']
        var4 = ['who are you', 'what is your name']
        cmd1 = ['open browser', 'open google', 'open the browser', 'open Google']
        cmd2 = ['play music', 'play songs', 'play a song', 'open music player']
        cmd4 = ['open youtube', 'i want to watch a video', 'open YouTube']
        cmd6 = ['exit', 'close', 'goodbye', 'nothing']
        cmd7 = ['what is your color', 'what is your colour', 'your color', 'your color?']
        colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']
        cmd8 = ['what is your favourite colour', 'what is your favourite color']
        cmd9 = ['thank you']
        repfr9 = ['your welcome', 'glad i could help you']
        abc = ('what can you do', 'do something')
        abcrep = 'I can tell the time, answer questions, tell the weather and much more. Just ask me'
        youcall = ['YouTube', 'youtube', 'YOUTUBE']
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        volume = engine.getProperty('volume')
        engine.setProperty('volume', 10.0)
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 50)
        data = ''

        def a():
            random_greeting = random.choice(greetings)
            print(random_greeting)
            engine.say(random_greeting)
            engine.runAndWait()

        def b():
            print(abcrep)
            engine.say(abcrep)
            engine.runAndWait()

        def c():
            engine.say('I am fine')
            engine.runAndWait()
            print('I am fine')

        def d():
            engine.say('I was made by edward')
            engine.runAndWait()
            reply = random.choice(var2)
            print(reply)

        def e():
            print(random.choice(repfr9))
            engine.say(random.choice(repfr9))
            engine.runAndWait()

        def f():
            print(random.choice(colrep))
            engine.say(random.choice(colrep))
            engine.runAndWait()
            print('It keeps changing every micro second')
            engine.say('It keeps changing every micro second')
            engine.runAndWait()

        def g():
            engine.say('I am edza your personal AI assistant')
            engine.runAndWait()

        def h():
            if __name__ == '__main__':
                app = wx.App()
                dialog = MyBrowser(None, -1)
                dialog.browser.LoadURL('www.youtube.com')
                dialog.Show()
                app.MainLoop()

        def i():
            print('see you later')
            engine.say('see you later')
            engine.runAndWait()

        def j():
            print("Current time : ")
            print(strftime("The time is %H:%M"))
            engine.say(strftime("The time is %H:%M"))
            engine.runAndWait()

        def k():
            if __name__ == '__main__':
                app = wx.App()
                dialog = MyBrowser(None, -1)
                dialog.browser.LoadURL('http://www.google.com')
                dialog.Show()
                app.MainLoop()

        def l():
            data = user_input
            data = data.split()
            data = data[1:]
            L = ' '.join(data)
            if __name__ == '__main__':
                app = wx.App()
                dialog = MyBrowser(None, -1)
                dialog.browser.LoadURL('http://www.google.com/search?hl=en&q=' + L)
                dialog.Show()
                app.MainLoop()

        def m():
            data = user_input
            data = data.split()
            data = data[1:]
            L = ' '.join(data)
            if __name__ == '__main__':
                app = wx.App()
                dialog = MyBrowser(None, -1)
                dialog.browser.LoadURL('http://www.youtube.com/search?hl=en&q=' + L)
                dialog.Show()
                app.MainLoop()

        if user_input in greetings:
            a()
        elif user_input in abc:
            b()
        elif user_input in question:
            c()
        elif user_input in var1:
            d()
        elif user_input in cmd9:
            e()
        elif user_input in cmd7:
            f()
        elif user_input in cmd8:
            f()
        elif user_input in var4:
            g()
        elif user_input in cmd4:
            h()
        elif user_input in cmd6:
            i()
        elif user_input in var3:
            j()
        elif user_input in cmd1:
            k()
        elif 'Google' in user_input:
            l()
        elif user_input[:7] in youcall:
            m()
        else:
            try:
                app_id = "GJRQVK-GY36XW7K8H"
                client = wolframalpha.Client(app_id)
                res = client.query(user_input)
                answer = next(res.results).text
                print(answer)
                engine.say(answer)
                engine.runAndWait()
            except:
                print(wikipedia.summary(user_input))
                engine.say(wikipedia.summary(user_input))
                engine.runAndWait()


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
