const editButtons = document.getElementsByClassName("btn-edit");
const bookText = document.getElementById("id_body");
const bookForm = document.getElementById("bookForm");
const submitButton = document.getElementById("submitButton");

/**
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Fetches the content of the corresponding comment.
 * - Populates the `commentText` input/textarea with the comment's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
 */
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let bookId = e.target.getAttribute("book_id");
        let bookContent = document.getElementById(`book${bookId}`).innerText;
        bookText.value = bookContent;
        submitButton.innerText = "Update";
        bookForm.setAttribute("action", `edit_book/$bookId}`);
    });
}