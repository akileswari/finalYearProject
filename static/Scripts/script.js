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

function exportdocx(){

  var sImageData = zingchart.exec('myChart', 'getimagedata', {
        format : 'png'
    });
    alert(sImageData);
var block = sImageData.split(";");
var contentType = block[0].split(":")[1];// In this case "image/gif"
var realData = block[1].split(",")[1];// In this case "R0lGODlhPQBEAPeoAJosM...."
var blob = b64toBlob(realData, contentType);
console.log(blob);
saveData(blob, "a.png");
var can = document.getElementById('myChart-main-c');
var ctx = can.getContext('2d');

ctx.fillRect(50,50,50,50);
////
var img = new Image();
img.src = sImageData;
document.body.appendChild(img);
//var canvas = document.createElement('canvas');
//var ctx = canvas.getContext('2d');
////var data=$('#myChart');
//var img=  new Image();
//var DOMURL = window.URL || window.webkitURL || window;
////var svg=new Blob([data],{
////type:'image/svg+xml:charset=utf-8'});
////
//img.onload=function(){
////
//ctx.drawImage(img, 0, 0, 500, 700);
//}
////var url = DOMURL.createObjectURL(sImageData);
//img.src=sImageData;
////        // $.get("http://localhost:4545/download")
       window.open("/download");
//
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
            }

            var byteArray = new Uint8Array(byteNumbers);

            byteArrays.push(byteArray);
        }

      var blob = new Blob(byteArrays, {type: contentType});
      return blob;
}

