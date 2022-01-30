# LingoCaptions

![image](https://user-images.githubusercontent.com/87694809/151697297-b9ee70c6-06e8-478a-be07-746d1415dc38.png)

A captioning application that facilitiates language learning by overcoming communication barriers through the use of real-time translator of internal computer audio.

![image](https://user-images.githubusercontent.com/87694809/151697598-cc43e635-fdd2-4500-959a-3fe4349654ec.png)

Functionality: 

The application currently works on MacOs. 

By clicking on the drop down menu directly undernearth "Select Langauge", the user is able to choose the langauge they want captions for.
Note: If you add too many outputs, you must extend the size of the application in order to view all of the contents appropiately. 

Clicking on "Add Output" allows the creation of mutiple caption window if more langauge needs to be translated. 

Checking the "romanization" checkbox allows the display of the orginal and romanization translation of the langauge. (Currently only Chinese-Pinyin and Japanese-Romaji). If it's not checked, only the original translation will display. The checkbox can be toggled at anytime.

Checking the "listening" checkbox must be checked in order to generate captions. Unchecking the box while the caption windows are open will close those windows. 
Note: that there is a delay when unchecking the box.

In order generate caption windows, click on "Generate Captions" after setting up the source and output langauges.  

The user is able to adjust the font size through the use of the "plus/minus" signs displayed at the top of their caption window. The plus sign increases size, while the minus sign decreases size.

The user is able to copy characters from the caption window and paste it elsewhere.

Note: If the user wants to add a langauge while the listening checkbox is fufilled, it will not work. The user must turn off and on the listening checkbox in order for the added langaages to populate and to reset the listener.

Installment: 
Install Blackhole (https://github.com/ExistentialAudio/BlackHole)
Go into Audio MIDI setup, create multi-ouput aggregate device with the outputs being Blackhole and the Macphone speakers. This is done by checking the two "Use" boxes next to Blackhole and the user's speakers.

![image](https://user-images.githubusercontent.com/87694809/151698155-df91d4c8-d782-4ed9-a326-1acc968aba4a.png)

The sound must be set to the multi-output aggregate device in order to run.

![image](https://user-images.githubusercontent.com/87694809/151698091-a3dd05d1-dd6a-4551-96f8-7fc56f1d61f1.png)

Note: the user is unable to change the volume of the video. They must go back to "Macphone Speakers" (where the volume would originally be outputted) within the their sound setting and change the volume.


API: Azure Translator
Note: Azure API key must be replaced in code in order for it to work.

Implementation: 
Desktop Application using Python and Tkinter(GUI). 
Compatible with Python 3.9. Higher versions might not be compatible.


https://youtu.be/vVFATnt2V_w
