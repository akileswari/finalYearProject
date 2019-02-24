function exportdocx(){

  var sImageData = zingchart.exec('myChart', 'getimagedata', {
        format : 'png'
    });
    alert(sImageData);
//}
var can = document.getElementById('myChart-main-c');
var ctx = can.getContext('2d');

ctx.fillRect(50,50,50,50);
////
var img = new Image();
img.src = sImageData.toDataURL();
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
//////        window.open("/download");
//
}
