async function uploadFile() {
    const filePath = document.getElementById("fileInput").files[0].path;
    const url = document.getElementById("urlInput").value;

    if (url !== "") {
        filePath = url;
        alert("Uploading file from URL...");
    }

    const status = document.getElementById("status");
    status.innerHTML = "Uploading file...";

    const response = await fetch("/upload", {
        method: "POST",
        body: JSON.stringify({
            "filepath": filePath
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    });

    if (response["error"]) {
        alert(response["error"]);
        return;
    }

    const answer = await response.json();
    status.innerHTML = answer.message;
}

async function query() {
    const query = document.getElementById("queryInput").value;
    const response = await fetch("/query", {
        method: "POST",
        body: JSON.stringify({
            "query": query
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    });

    if (response["error"]) {
        alert(response["error"]);
        return;
    }

    const answer = await response.json();

    const outputContainer = document.getElementById("outputContainer");
    outputContainer.innerHTML = answer.answer;
}