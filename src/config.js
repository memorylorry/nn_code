let config = {
    profile:'prod3', // 设置运行模式: prod:test:local（缺省）
    version:new Date().getTime()
};

let prod_url = {
    root:'/py-demo',
    url_prefix:'/py-demo/dist/data'
};
let local_url = {
    root:'/',
    url_prefix:'/dist/data'
};



if(config.profile == 'prod'){
    config.resources = prod_url;
}else{
    config.resources = local_url;
}

export default config;