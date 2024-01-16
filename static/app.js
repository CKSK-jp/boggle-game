const $guess = $('input[name="guess"]');
const $wordList = $('#found-words-list');
const $feedbackDiv = $('.feedback');
const $scorebox = $('#user-score');

async function submitGuess() {
  try {
    let guess = $guess.val();
    $guess.val('');

    const response = await axios.post("/submit-guess", {
      guess: guess
    });
    if (response.status === 200) {
      console.log(response);
      updateFoundWords(response.data.foundWords)
      updateMessage(response.data.feedback)
      updateScore(response.data.score)
    }
  } catch (error) {
    console.log(error);
  }
}

function updateFoundWords(foundWords) {
  $wordList.empty();
  foundWords.forEach(word => {
    const foundWordItem = $('<li>').text(word);
    $wordList.append(foundWordItem);
  })
}

function updateMessage(msg) {
  $feedbackDiv.text(msg);
}

function updateScore(score) {
  $scorebox.text() + score;
}