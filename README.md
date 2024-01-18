# boggle-game
The goal of the game is to get the highest point total. To gain points, players create words from a random assortment of letters in a 5x5 grid.

## **Set Up **

```bash
$python3 -m venv venv
```

```bash
$source venv/bin/activate
(env) $

```

```bash
(env) $pip3 install flask
...

```

Make a “requirements.txt” file in this directory with a listing of all the software needed for this project:
```
(env) $pip3 freeze > requirements.txt
```

### **Usage Instructions **
- User can find words by chaining words in the horizontal, vertical, or diagonal axis.
- Entering a valid word will award a score proportional to the length of the word
- Selecting a timed game will set a 60 second timer
- Scores are saved server side using session
- Timed Games will be saved in both localStorage and server side sessions

**Technologies Used:** HTML, CSS, JavaScript, Flask, Axios, Python, Unittest

## TODO 
Implement timer