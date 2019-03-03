
saveData = (function () {

    var a = document.createElement("a");
    a.style = "display: none";
    return function (blob, fileName) {
        var url = window.URL.createObjectURL(blob);
        a.href = url;
        a.download = fileName;
        a.click();
        window.URL.revokeObjectURL(url);
    };
}());


function exportdocx() {
    var selectedChart=document.getElementById("SelectedChart").value;
    console.log(selectedChart);
    var sImageData = zingchart.exec(selectedChart, 'getimagedata', {
        format: 'png'
    });
    var block = sImageData.split(";");
    var contentType = block[0].split(":")[1];// In this case "image/gif"
    var realData = block[1].split(",")[1];// In this case "R0lGODlhPQBEAPeoAJosM...."
    var blob = b64toBlob(realData, contentType);
    console.log(blob);
    //saveData(blob, "a.png");
//    var url = window.URL.createObjectURL(blob);
//    url.download="asd.png";
//    console.log(url);
//    var file = new File([new Blob()], "image1.png", {type:"image/png"});
//    console.log(file);
    var form = new FormData();
    form.append('file', blob, "fomd.png");
    // var can = document.getElementById('myChart-main-c');
    // var ctx = can.getContext('2d');

    // ctx.fillRect(50,50,50,50);

    // var img = new Image();
    // img.src = sImageData;
    // document.body.appendChild(img);

    $.ajax({
      type: 'POST',
      url: '/download',
      data: form,
      cache: false,
      processData: false,
      contentType: false
    }).done(function(data) {
      console.log(data);
      window.open("/downloadpdf");
    });


}
function b64toBlob(b64Data, contentType, sliceSize) {
    contentType = contentType || '';
    sliceSize = sliceSize || 512;

    var byteCharacters = atob(b64Data);
    var byteArrays = [];

    for (var offset = 0; offset < byteCharacters.length; offset += sliceSize) {
        var slice = byteCharacters.slice(offset, offset + sliceSize);

        var byteNumbers = new Array(slice.length);
        for (var i = 0; i < slice.length; i++) {
            byteNumbers[i] = slice.charCodeAt(i);
        }1

        var byteArray = new Uint8Array(byteNumbers);

        byteArrays.push(byteArray);
    }

    var blob = new Blob(byteArrays, { type: contentType });
    return blob;
}

