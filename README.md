# Web-views-tracking
I don't know how to say it... Use to  track your web views by adding a simple HTML code\
Programming languages: Python, HTML (wait this not a programming language)\
[The website](https://Web-views-tracking.lukenk.repl.co)

## How to use
Simply put the HTML code that the app give you to your HTML `<head>` section. To view the view count, simply replace the view counter link to `/views/<your_ID>` instead of `/count/<you_ID>`

## How it work
After you connect to [/h](https://Web-views-tracking.lukenk.repl.co/h), it will create a `.txt` file in `file` folder with a 10 digits name that contain view number in it (start at 0)\
The HTML <link> tag will make the browser connect to the website, which then make the python server increase the view number by 1.

## CLI
You can just use any programming language and send a HTTP post requests to https://Web-views-tracking.lukenk.repl.co/cli

### Post data
Send the post request with the following data:  
`respond : <your_option>`  
Options:
- `link` Respond the entire link (include the app link) to put in HTML tag
- `code` Respond only 10 characters for the tracking code
- `html` Respond the HTML tag
- `count` Respon the link to the counter\
To get the respond with the view count, send post request:  
`respond : check, code: <your_code>`  
`<your_code>` is the 10 characters for the tracking code  

### Examples
#### Python
```py
import requests
link = 'https://Web-views-tracking.lukenk.repl.co/cli'
r = requests.post(link, data = {'respond' : 'html'}) 
html_tag = r.text #get the entire HTML tag for use
```
## Versions
### 1.0 
- First release to Gig Hub

### 1.1 (not yet release)
- Add interface to the counter view page
- CLI command for view the views number

### Some far day
- Add IFrame for view counter
- Options for the HTML code


## Branches
So I'll note some branches
1. `main` the default, and fully able to run.
2. `unstable-relpit` branch that connect to [repl.it](https://repl.it/@LukeNK/Web-views-tracking) so I can edit. As the name, this branch will be unstable and have a lot of bug, but will be the branch that have the latest features.