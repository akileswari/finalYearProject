
saveData = (function () {

    var a = document.createElement("a");
    a.style = "display: none";
    return function (blob, fileName) {
        var url = blob;
        a.href = url;
        a.download = fileName;
        a.click();
        window.URL.revokeObjectURL(url);
    };
}());


function exportdocx() {
    console.log("hello1");
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
    var imagename=selectedChart+".png"
    var form = new FormData();
    form.append('file', blob, imagename);
    console.log("befor ajax call");
    $.ajax({
      type: 'POST',
      url: '/download',
      data: form,
      cache: false,
      processData: false,
      contentType: false
    }).done(function(data) {
      console.log(data);
      window.open("/downloadpdf?fn="+selectedChart+".png","clearcache=yes");
    });


    form=undefined;

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
//function deletedocx()
//{
//var s=window.open("/delete");
//}

