const $wordList = $('#found-words-list');
const $feedbackDiv = $('.feedback')

async function submitGuess() {
  try {
    let guess = $('input[name="guess"]').val();

    const response = await axios.post("/submit-guess", {
      guess: guess
    });
    console.log(response.status)
    if (response.status === 200) {
      updateFoundWords(response.data.foundWords)
      updateMessage(response.data.feedback)
    }
  } catch (error) {
    console.log(error);
  }
}

function updateFoundWords(foundWords) {
  $wordList.empty()
  foundWords.forEach(word => {
    console.log(word)
    const foundWordItem = $('<li>').text(word)
    $wordList.append(foundWordItem)
  })
}

function updateMessage(msg) {
  console.log(msg);
  $feedbackDiv.text(msg)
}