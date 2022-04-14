var file = document.getElementById("file")
var fileName = document.getElementById("fileName")
function getname() {

    fileName.innerHTML = file.files[0].name
}

function afterClick(){
    if(file.files[0]!=undefined){
        let formData=new FormData();
        let ajaxHttp=new XMLHttpRequest();
        ajaxHttp.open("POST","http://127.0.0.1:5000/uploader",true);
        // ajaxHttp.setRequestHeader()
        formData.append("file",file.files[0]);
        ajaxHttp.send(formData);
        ajaxHttp.onreadystatechange=function(){
            if(ajaxHttp.responseText=="True" && ajaxHttp.readyState==4){
                alert("文件转换成功！")
                // location.reload();
            };
            if(ajaxHttp.responseText=="False" && ajaxHttp.readyState==4){
                alert("请重新上传文件！");
            };
        }

    }
    else{
        alert("?")
    }
}

