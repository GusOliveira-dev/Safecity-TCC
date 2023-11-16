function showFrame(frameNumber) {
    var iframes = document.querySelectorAll('.iframe-container iframe');
    for (var i = 0; i < iframes.length; i++) {
        iframes[i].style.display = 'none';
    }
    document.getElementById('iframe-' + frameNumber).style.display = 'block';
}



function getNews() {
    fetch('https://cors-anywhere.herokuapp.com/http://newsapi.org/v2/everything?q=furto AND roubo +São Paulo&apikey=134a6d5a441c4203892bf4cc970cc8ff',{headers: new Headers({"X-RequestedWith":"wkgfjkhdgfhkusvsbvkhbhsb" })})
        .then(response => response.json())
        .then(response => {
            for (var i = 0; i < 10; i++) {
                document.getElementById("output").innerHTML +=
                "<div class='news-card'>" +
                "<img class='news-image' src=" + response.articles[i].urlToImage + ">" +
                "<div class='news-content'>" +
                "<h3>" + response.articles[i].title + "</h3>" +
                response.articles[i].source.name + "<br><br>" +
                response.articles[i].description +
                "<a href=" + response.articles[i].url + " target='_blank'>Leia Mais</a>" +
                "</div>" +
                "</div>";
                }
            })}  