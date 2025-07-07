function getQuote(type) {
    let url = type === "fun" ? "/get-fun-quote" : "/get-normal-quote";

    fetch(url)
        .then(response => response.json())
        .then(data => {
            document.getElementById("quote-text").innerText = "❝ " + data.quote + " ❞";
            document.getElementById("author-name").style.display = "none";
        })
        .catch(error => console.error('Error fetching quote:', error));
}
