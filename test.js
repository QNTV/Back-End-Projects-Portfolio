var xhr = new XMLHttpRequest();
var url = 'https://home.sieukhung.org/2023/01/o-day-co-nhieu-gai-ngon/';
xhr.open('GET', url, true);
xhr.responseType = 'text';
xhr.onreadystatechange = function () {
  if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
    var parser = new DOMParser();
    var htmlDoc = parser.parseFromString(xhr.responseText, 'text/html');
    var images = htmlDoc.getElementsByTagName('img');
    for (var i = 0; i < images.length; i++) {
      var imgSrc = images[i].src;
      if (imgSrc.endsWith('.jpg') || imgSrc.endsWith('.png') || imgSrc.endsWith('.jpeg')) {
        var xhrImg = new XMLHttpRequest();
        xhrImg.open('GET', imgSrc, true);
        xhrImg.responseType = 'blob';
        xhrImg.onreadystatechange = function () {
          if (xhrImg.readyState === XMLHttpRequest.DONE && xhrImg.status === 200) {
            var blob = xhrImg.response;
            var link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);
            link.download = imgSrc.substring(imgSrc.lastIndexOf('/') + 1);
            link.click();
          }
        };
        xhrImg.send();
      }
    }
  }
};
xhr.send();
