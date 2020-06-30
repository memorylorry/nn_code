let config = {
    profile:'' // 设置运行模式: prod:test:local（缺省）
};

let prod_url = {
    url_prefix:''
};
let local_url = {
    url_prefix:'/dist/data/'
};



if(config.profile == 'prod'){
    config.resources = prod_url;
}else{
    config.resources = local_url;
}

export default config;