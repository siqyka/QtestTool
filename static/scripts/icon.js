var Positions = [...line3,...line4,...line5,...line7,...line8]

// icon样式
var icon = {
    // 图标类型，现阶段只支持 image 类型
    type: 'image',
    // 图片 url
    image: '../static/makes/hm.png',
    // 图片尺寸
    size: [17, 17],
    // 图片相对 position 的锚点，默认为 bottom-center
    anchor: 'center',
};

// 文字样式
var textStyle = {
    fontSize: 13,
    fontWeight: 'normal',
    // fillColor: '#22886f',
    fillColor: '#757575',
    
    strokeColor: '#fff',
    strokeWidth: 2,
    fold: true,
    padding: '2, 5',
};
var markers = [];
var positions = Positions.slice(0, 3E4);
// var positions=[[120.211598, 30.244463],[120.210792, 30.246026]]
var LabelsData = [
    {
        name: '自提点1',
        position: [120.211598, 30.244463],
        zooms: [13.7, 20],
        opacity: 1,
        zIndex: 120,
        fold: true,
        icon,
        text: {
            content: '中邮速递易',
            direction: 'right',
            offset: [-4, -2],
            style: textStyle
        }
        // text: {
        //     // 要展示的文字内容
        //     content: '中邮速递易',
        //     // 文字方向，有 icon 时为围绕文字的方向，没有 icon 时，则为相对 position 的位置
        //     direction: 'right',
        //     // 在 direction 基础上的偏移量
        //     offset: [-20, -5],
        //     // 文字样式
        //     style: {
        //         // 字体大小
        //         fontSize: 12,
        //         // 字体颜色
        //         fillColor: '#22886f',
        //         //
        //         strokeColor: '#fff',
        //         strokeWidth: 2,
        //         fold: true,
        //         padding: '2, 5',
        //     }
        // }
    }]


// var allowCollision = false;
var layer = new AMap.LabelsLayer({
    zooms: [13.7, 20],
    zIndex: 120,
    // collision: false,
    // 设置 allowCollision：true，可以让标注避让用户的标注
    // allowCollision,
});
layer.add(markers);
// 图层添加到地图
map.add(layer);

// 初始化 labelMarker
var pot={
    name: '自提点1',
    position: [120.211598, 30.244463],
    zooms: [13.7, 20],
    opacity: 1,
    zIndex: 120,
    fold: true,
    icon,
    text: {
        content: '中邮速递易',
        direction: 'right',
        offset: [-4, -2],
        style: textStyle
    }
}
// for (var i = 0; i < LabelsData.length; i++) {
//     var curData = LabelsData[i];
//     curData.extData = {
//         index: i
//     };

//     var labelMarker = new AMap.LabelMarker(curData);

//     markers.push(labelMarker);

// }
for (var i = 0; i < positions.length; i++) {
    msg=positions[i]
    text=pot['text']
    text['content']=msg['name']
    pot['position']=msg['position'];
    var curData = pot
    curData.extData = {
        index: i
    };

    var labelMarker = new AMap.LabelMarker(curData);

    markers.push(labelMarker);

}

// 将 marker 添加到图层
layer.add(markers);

