function animate(obj,target,callback){
    clearInterval(obj.timer);
    obj.timer =setInterval(function(){
        // var step = (target - obj.offsetLeft) / 10;
        var step = (target - obj.offsetLeft);
        step = step > 0 ? Math.ceil(step): Math.floor(step);
        if(obj.offsetLeft = target) {
            clearInterval(obj.timer);
            // if(callback) {
            //     callback();
            // }
            callback && callback();
        }
        // 把每次加1这个步长改为一个慢慢变成小的值
        obj.style.left = obj.offsetLeft + step + 'px';

    },15);
}