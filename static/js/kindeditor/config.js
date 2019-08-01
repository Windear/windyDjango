KindEditor.ready(function (K) {
    K.create('textarea[name=content]', {
        width: 800,
        height: 600,
        uploadJson: '/admin/upload/kindeditor',
        allowImageUpload: true,//允许上传图片
        urlType:'domain',//带域名的绝对路径
        formatUploadUrl:false,//是否格式化上传后的URL
    });
});








