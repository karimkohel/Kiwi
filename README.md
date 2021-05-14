# Poppy 
Project poppy is a custom made virtual assistant project.


### What's happening 

##### neuralintents file
the generic class that holds all code responsible for the nueral netowrk

##### poppy
the main file that is self explanatory

##### fx 
the file responsible for all functions and logic to be run upon a certain request

##### speech
some custom made functions that haandles text to speach and speach recognition for the assistant

### Features 

 - [X] greet and bye
 - [X] tell time
 - [X] tell weather
 - [X] tell jokes
 - [X] search online
 - [X] write down notes
 - [ ] play music
 - [ ] manage calendar/classes
 - [ ] change vioce settings
 - [ ] give you attitude if you ask too much
 - [ ] maybe have a GUI


#### links:
this is to remind me what the hell was i doing when i get back to the project on a later date.

 - [Neuralnine tutorial](https://www.youtube.com/watch?v=1lwddP0KUEg&t=130s)
 - [Tim tutorial](https://youtube.com/playlist?list=PLzMcBGfZo4-ndH9FoC4YWHGXG5RZekt-Q)
 - [random](https://www.youtube.com/watch?v=9KZwRBg4-P0)
 - [random](https://www.youtube.com/watch?v=RpWeNzfSUHw)


#### Freezing
Pyinstaller command 

```bash
pyinstaller --noconfirm --onedir --windowed --icon "K:/Projects/python/poppy/icon.ico" --debug "all" --noupx --add-data "K:/Projects/python/poppy/model.h5;." --add-data "K:/Projects/python/poppy/model_classes.pkl;." --add-data "K:/Projects/python/poppy/model_words.pkl;." --add-data "K:/Projects/python/poppy/notes.txt;." --paths "K:/Projects/python/poppy" --additional-hooks-dir "K:/Projects/python/poppy/hooks" --hidden-import "tensorflow" --hidden-import "tensorflow.lite.python.lite" --hidden-import "urllib3" --hidden-import "urllib" --hidden-import "numpy" --hidden-import "pkg_resources.py2_warn" --hidden-import "pkg_resources.markers" --add-data "K:/Projects/python/poppy/intents.json;." --add-data "K:/Projects/python/poppy/icon.ico;." --add-data "K:/Projects/python/poppy/kiwi.jpg;."  "K:/Projects/python/poppy/kiwi.py"
```