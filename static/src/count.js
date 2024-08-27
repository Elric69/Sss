function fetchData() {
    fetch("/api/data")
    .then(
        response => response.json()

    ).then(data => {
        const para = document.getElementById("solved-leetcode")
        para.innerHTML = `Total solved questions: ${data.total}<br>Easy: ${data.easy}<br>Medium: ${data.medium}<br>Hard: ${data.hard}`
    }
    ).catch(error => {
        
        console.error("error :", error);
        const para = document.getElementById("solved-leetcode")
        para.innerHTML = "Total solved questions: ??<br>Easy: ??<br>Medium: ??<br>Hard: ??"
    })
}
window.onload = fetchData;
