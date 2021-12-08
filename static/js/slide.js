window.addEventListener('load',function(){
    // 获取元素
    var arrow_l = document.querySelector('.arrow-l');
    var arrow_r = document.querySelector('.arrow-r');
    var focus = document.querySelector('.focus');
    var focusWidth = focus.offsetWidth;
    // 鼠标经过，就显示隐藏
    focus.addEventListener('mouseenter',function(){
        arrow_l.style.display = 'block';
        arrow_r.style.display = 'block';
        clearInterval(timer);
        timer = null; //清除定时器变量

    });
    // 鼠标离开
    focus.addEventListener('mouseleave',function(){
        arrow_l.style.display = 'none';
        arrow_r.style.display = 'none';
        timer = setInterval(function(){
            arrow_r.click();
        },2000);

    });
    // 动态生成小圆圈
    var ul = focus.querySelector('ul');
    var ol = focus.querySelector('.circle');
    for(var i= 0; i < ul.children.length; i++) {
        var li = document.createElement('li');
        // 记录当前小圆圈的索引号，通过自定义属性来做
        li.setAttribute('index',i);
        // 把小li插入到ol里面,
        ol.appendChild(li);
        // 小圆圈的排他思想，我们可以直接在生成小圆圈的同时，直接绑定点击事件
        li.addEventListener('click',function(){
            for(var i = 0; i < ol.children.length; i++) {
                ol.children[i].className = '';
            }
            // 留下自己，当前的li设置current 类名
            this.className = 'current';
            // 点击小圆圈，移动图片，当前移动的是ul
            // ul的移动距离 小圆圈的索引号乘以图片的宽度，注意是负值
            // 当前惦记了某个小li或拿到当前小li的索引号
            var index = this.getAttribute('index');
            // 当点击了某个小li或拿到当前小li的索引号给num
            num = index;
              // 当点击了某个小li或拿到当前小li的索引号给circle

            circle = index;
            // var focusWidth = focus.offsetWidth;
            console.log(focusWidth);
            console.log(index);
            animate(ul,-index * focusWidth);
        });
    }
    // 把ol里面的第一个小li设置为current
    ol.children[0].className = 'current';
    // 克隆第一张图(li)放到ul最后面
    var first = ul.children[0].cloneNode(true);
    ul.appendChild(first);
    // 点击右侧按钮，图片滚动一张
    var num = 0;
    // circle 控制小圆圈的播放
    var circle = 0;
    // flag节流阀
    var flag = true;

    arrow_r.addEventListener('click',function(){
        if (flag) {
            flag = false; //关闭节流阀
            // 如果走到了最后一张图片，此时，我们的ul要快速复原left改为0
        if(num == ul.children.length - 1) {
            ul.style.left = 0;
            num = 0;
        }
        num++;
        animate(ul, -num * focusWidth, function(){
            flag = true; //打开节流阀
        });
        // 点击右侧按钮，小圆圈跟随一起变化,可以再申明一个变量控制小圈的播放
        circle++;
        if(circle == ol.children.length) {
            circle = 0;
        }
        circleChange();
        }
        // 先清楚其余小圆圈的current类名
        // for(var i = 0; i < ol.children.length; i++) {
        //     ol.children[i].className = '';
        // }
        // // 留下当前的小圆圈的current类名
        // ol.children[circle].className = 'current';
    });
    // 9.左侧按钮
    arrow_l.addEventListener('click',function(){
        if (flag) {
            flag = false;
            // 如果走到了最后一张图片，此时，我们的ul要快速复原left改为0
        if(num == 0){
            num = ul.children.length - 1;
            ul.style.left = -num * focusWidth + 'px'
        }

        num--;
        animate(ul, -num * focusWidth,function(){
            flag = true;
        });
        // 点击右侧按钮，小圆圈跟随一起变化,可以再申明一个变量控制小圈的播放
        circle--;
        // if(circle == ol.children.length) {
        //     circle = 0;
        // }
        circle = circle < 0 ? ol.children.length - 1 : circle;

        // 调用函数
        circleChange()
        }
    });
    function circleChange(){
        // 先清楚其余小圆圈的current类名
        for(var i = 0; i < ol.children.length; i++) {
            ol.children[i].className = '';
        }
            // 留下当前的小圆圈的current类名
        ol.children[circle].className = 'current';

    }
    // 自动播放轮播图
    var timer = setInterval(function(){
        // 手动调用点击函数
        arrow_r.click();
    },2000);


});