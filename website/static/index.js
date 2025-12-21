function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ noteId })
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      window.location.href = "/";
    } else {
      alert("Failed to delete note: " + (data.error || "Unknown error"));
    }
  })
  .catch(error => {
    console.error("Error:", error);
    alert("An error occurred while deleting the note.");
  });
}
