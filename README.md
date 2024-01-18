# boggle-game
The goal of the game is to get the highest point total. To gain points, players create words from a random assortment of letters in a 5x5 grid.

## **Set Up **

```bash
$python3 -m venv venv
```
Activate virtual env
```bash
$source venv/bin/activate
(env) $

```
Install all necessary dependencies
```bash
(env) $pip3 install -r requirements.txt
...

```

Run flask app
```
(env) flask run
```

### **Usage Instructions **
- User can find words by chaining words in the horizontal, vertical, or diagonal axis.
- Entering a valid word will award a score proportional to the length of the word
- Selecting a timed game will set a 60 second timer
- Scores are saved server side using session
- Timed Games will be saved in both localStorage and server side sessions

**Technologies Used:** sessionStorage, Jquery, Flask, Axios, Unittest

## TODO 
Implement gameboard cursor interactivity and addtional unittesting
