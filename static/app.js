
async function performPost() {
  try {
    const formData = new FormData();
    formData.append('color', $('input[name="color"]').val());

    await axios.post("/submit-form", formData)
      .then(response => {
        console.log(response)
    })
  } catch (error) {
    console.log(error);
  }
}
