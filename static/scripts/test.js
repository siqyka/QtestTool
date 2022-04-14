// var positions = [[120.211598, 30.244463], [120.210792, 30.246026]];
var hmmarkers = [];

var hmIcon = new AMap.Icon({
    // 图标尺寸
    size: new AMap.Size(300, 100),
    // 图标的取图地址
    image: 'C:/Users/PREDATOR/Desktop/hm.png',
    // 图标所用图片大小
    imageSize: new AMap.Size(15, 15),
    // 图标取图偏移量
    // imageOffset: new AMap.Pixel(-9, -3)
});


function logMapinfo() {
    var zoom = map.getZoom(); //获取当前地图级别
    document.querySelector("#map-zoom").innerText = zoom;
    if (zoom < 13.7) {
        map.remove(hmmarkers);
        hmmarkers = []
    }
    //创建地铁站点
    else if (zoom > 13.7 && hmmarkers == false) {
        for (var i = 0, hmmarker; i < positions.length; i++) {

            hmmarker = new AMap.Marker({
                map: map,
                icon: hmIcon,
                position: positions[i]
            });

            hmmarkers.push(hmmarker);
        }
    }

};

//绑定地图移动与缩放事件
map.on('zoomend', logMapinfo);



