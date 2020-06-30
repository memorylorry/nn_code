import config from '../config';
import React from 'react';
import PropTypes from 'prop-types';

import { List, InputItem, Toast,WhiteSpace } from 'antd-mobile';

const propTypes = {
    focusHandle: PropTypes.func
};
const defaultProps = {
    focusHandle: (data)=>{}
};
export default class Setting extends React.Component {

    constructor(props){
        super(props);
        this.state = {userInfo:{}}
        this.focusHandle = this.focusHandle.bind(this);
        this.blurHandle = this.blurHandle.bind(this);
    }

    focusHandle(){
        // this.props.focusHandle(true);
    }
    blurHandle(){
        // this.props.focusHandle(false);
    }

    handleClick(){
    }
    render() {
        let userInfo = this.state.userInfo;
        return (
            <div className={'sub-page'}>
                <List renderHeader={() => '基础信息'}>
                    <InputItem
                        clear
                        placeholder={"设置别名"}
                        value = {userInfo.name?userInfo.name:''}
                        onFocus={this.focusHandle}
                        onBlur={this.blurHandle}
                        editable={false}
                    >昵称</InputItem>
                    <InputItem
                        clear
                        placeholder="29403***9"
                        value = {userInfo.qq?userInfo.qq:''}
                        onFocus={this.focusHandle}
                        onBlur={this.blurHandle}
                        editable={false}
                    >QQ</InputItem>
                    <InputItem
                        clear
                        placeholder="wechatID"
                        value = {userInfo.wechatID?userInfo.wechatID:''}
                        onFocus={this.focusHandle}
                        onBlur={this.blurHandle}
                        editable={false}
                    >微信号</InputItem>
                    <InputItem
                        clear
                        placeholder="mail@qq.com"
                        value = {userInfo.mail?userInfo.mail:''}
                        onFocus={this.focusHandle}
                        onBlur={this.blurHandle}
                        editable={false}
                    >邮件</InputItem>
                    <InputItem
                        type="phone"
                        placeholder="186 1234 1234"
                        value = {userInfo.phone?userInfo.phone:''}
                        onFocus={this.focusHandle}
                        onBlur={this.blurHandle}
                        editable={false}
                    >手机号码</InputItem>
                </List>

                <List renderHeader={() => '安全'}>
                    <List.Item>
                        <div
                            style={{ width: '100%', color: '#108ee9', textAlign: 'center' }}
                            // onClick={this.handleClick}
                        >
                            修改密码
                        </div>
                    </List.Item>
                </List>
            </div>
        );
    }
    componentDidMount(){
        let url = config.resources.mainPage.UserInfo;
        $.ajax({
            url:url,
            async:false,
            dataType:'json',
            success:(data)=>{
                if(data.code == 0){
                    this.setState({userInfo:data.data})
                }else{
                    console.log('错误')
                }
            },
            error:(data)=>{
                console.log('错误')
            }
        });
    }
}
Setting.propTypes = propTypes;
Setting.defaultProps = defaultProps;