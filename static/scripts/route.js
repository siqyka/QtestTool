


var path = [//每个弧线段有两种描述方式
    [120.211598,30.244463],//起点
    [//弧线段有两种描述方式2
      [120.211598,30.244463],//控制点
      [120.207006,30.23955],//控制点
      [120.207006,30.23955]//途经点
    ]


];

var bezierCurve = new AMap.BezierCurve({
    path: path,
    isOutline: true,
    outlineColor: '#ffeeff',
    borderWeight: 3,
    strokeColor: "#3366FF", 
    strokeOpacity: 1,
    strokeWeight: 3,
    // 线样式还支持 'dashed'
    strokeStyle: "solid",
    // strokeStyle是dashed时有效
    strokeDasharray: [10, 10],
    lineJoin: 'round',
    lineCap: 'round',
    zIndex: 50,
})

map.add(bezierCurve);
// 缩放地图到合适的视野级别
// map.setFitView([ bezierCurve ])

// var bezierCurveEditor = new AMap.BezierCurveEditor(map, bezierCurve)
