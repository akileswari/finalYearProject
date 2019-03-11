function exportdocx() {
    var selectedChart = document.getElementById("SelectedChart").value;
    var form = new FormData();
    if (selectedChart == "All charts") {
        var chartid = ["myChart", "myChart_a", "myChart_c", "myChart_i", "myChart_n"];
        for (var i = 0; i < chartid.length; i++) {
            var sImageData = zingchart.exec(chartid[i], 'getimagedata', {
                format: 'png'
            });
            var block = sImageData.split(";");
            var contentType = block[0].split(":")[1]; // In this case "image/gif"
            var realData = block[1].split(",")[1]; // In this case "R0lGODlhPQBEAPeoAJosM...."
            var blob = b64toBlob(realData, contentType);
            var imagename = chartid[i] + ".png"
            form.append('file'+i, blob, imagename);
            }
    }
    else {
        var sImageData = zingchart.exec(selectedChart, 'getimagedata', {
            format: 'png'
        });
        var block = sImageData.split(";");
        var contentType = block[0].split(":")[1]; // In this case "image/gif"
        var realData = block[1].split(",")[1]; // In this case "R0lGODlhPQBEAPeoAJosM...."
        var blob = b64toBlob(realData, contentType);
        var imagename = selectedChart + ".png"
        form.append('file', blob, imagename);
    }
    $.ajax({
        type: 'POST',
        url: '/download',
        data: form,
        cache: false,
        processData: false,
        contentType: false
    }).done(function (data) {
        window.open("/downloadpdf?fn=" + selectedChart + ".png", "clearcache=yes");
    });
    form = undefined;

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

