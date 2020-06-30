import config from '../config';
import React from 'react';
import { Menu, Icon, Button, NavBar, Grid } from 'antd-mobile';
import { Route, Link, BrowserRouter as Router } from 'react-router-dom';

import IconFont from '../component/GetIconFont.js';

import './AppList.less';

export default class AppList extends React.Component {
    constructor(props){
        super(props);
        this.state = {appList:[]};
    }
    render() {
        let appList = this.state.appList;
        const rows = appList.map((row,index) => {
            const data = row.apps.map((_val, i) => ({
                icon: <Link className="itema" to={`/item/${_val.id}`}>
                            {IconFont.getByTag(_val.logo)}
                       </Link>,
                text: `${_val.name}`,
            }));
            return (
                <div key={index}>
                    <div className="sub-title bright-color">{row.name}</div>
                    <Grid data={data} activeStyle={false} onClick={(d)=>{console.log(d);}} />
                </div>
            );
        });

        return (
            <div className={'sub-page app-list'}>
                {rows}
            </div>
        );
    }

    componentDidMount(){
        let url = config.resources.mainPage.AppList;
        $.ajax({
            url:url,
            async:false,
            dataType:'json',
            success:(data)=>{
                if(data.code == 0){
                    this.setState({appList:data.data})
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