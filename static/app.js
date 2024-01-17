const $guess = $('input[name="guess"]');
const $wordList = $('#found-words-list');
const $feedbackDiv = $('.feedback');
const $scorebox = $('#user-score');
const $timerBtn = $('.timer-btn');
const $timerBox = $('#timer').parent();
let countdownInterval;

init();

function init() {
  if (sessionStorage.getItem('timedGame') === 'true') {
    activateTimer();
  } else {
    deactivateTimer();
  }

  $timerBtn.on('click', toggleTimer);
}

function activateTimer() {
  $timerBtn.addClass('active');
  $timerBox.addClass('timer-styles');
  countdownInterval = setInterval(startTimer, 1000);
}

function deactivateTimer() {
  $timerBtn.removeClass('active');
  $timerBox.removeClass('timer-styles');
  clearInterval(countdownInterval);
  $timerBox.children().text('');
}

function toggleTimer() {
  if ($timerBtn.hasClass('active')) {
    deactivateTimer();
    sessionStorage.setItem('timedGame', false);
    stopTimer();
  } else {
    activateTimer();
    sessionStorage.setItem('timedGame', true);
  }
}

function startTimer() {
  try {
    fetch('/start_timer')
      .then(response => response.json())
      .then(data => {
        let seconds = Math.round(data.duration)
        $timerBox.children().text(seconds);
        console.log(seconds);

        if (seconds <= 0) {
          deactivateTimer();
          sessionStorage.setItem('timedGame', false);
          gameOver();
        }
      });
  } catch (error) {
    console.log(error);
  }
}

function stopTimer() {
  axios.post('/stop_timer')
    .then(() => console.log('Timer stopped'))
    .catch(error => console.error(error));
}

function gameOver() {
  $('#user-input :input').prop('disabled', true);
  $timerBtn.addClass('disabled');
  $('.feedback').text('GAME OVER, press reset to try again');
}

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