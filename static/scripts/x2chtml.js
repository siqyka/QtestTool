var file = document.getElementById("file")
var fileName = document.getElementById("fileName")
var button = document.getElementById("button")
var durl = ""

function getName() {

    fileName.innerHTML = file.files[0].name;
    button.innerHTML = "转换";
    button.name = "zh";
}

function afterClick() {
    let formData = new FormData();
    let ajaxHttp = new XMLHttpRequest();

    if (file.files[0] != undefined && button.name == "zh") {

        ajaxHttp.open("POST", "http://127.0.0.1:5000/x2c/uploader", true);
        // ajaxHttp.setRequestHeader()
        formData.append("file", file.files[0]);
        ajaxHttp.send(formData);
        ajaxHttp.onreadystatechange = function () {
            returnText = ajaxHttp.responseText;
            if (returnText == "Q101" && ajaxHttp.readyState == 4) {
                fileName.innerHTML=""
                alert("请上传xmind文件！");
                return
            }
            statusText = returnText.substring(0, returnText.lastIndexOf("+"));

            if (statusText == "True" && ajaxHttp.readyState == 4) {
                durl = returnText.substring(returnText.lastIndexOf("+") + 1);
                alert("文件转换成功！")
                button.innerHTML = "下载"
                button.name = "xz"
                // location.reload();
            };
            if (statusText == "False" && ajaxHttp.readyState == 4) {
                alert("请重新上传文件！");
            };
        }

    }
    else if (file.files[0] != undefined && button.name == "xz") {
        var index = durl.lastIndexOf("/");
        var download_file_name = durl.substring(index + 1)
        var url = "http://127.0.0.1:5000" + durl
        ajaxHttp.open("GET", url, true);
        ajaxHttp.responseType = 'blob'; // 返回类型blob
        ajaxHttp.onload = function (e) {
            if (this.status === 200) {
                const blob = this.response;
                const reader = new FileReader();
                reader.readAsDataURL(blob); // 转换为base64，可以直接放入a表情href
                reader.onload = function (e) {
                    const a = document.createElement('a');
                    a.download = download_file_name;
                    a.href = e.target.result;
                    document.documentElement.appendChild(a);
                    a.click();
                    a.remove(); // 等价于document.documentElement.removeChild(a);
                };
            }
        };
        ajaxHttp.send(); // 发送ajax请求
        button.name = "xz"
    }
    else {
        alert("请选择上传的文件！")
    }
}

