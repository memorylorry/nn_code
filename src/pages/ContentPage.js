import config from '../config';
import React from 'react';
import PropTypes from 'prop-types';
import { Menu, Icon, Button, NavBar, Grid, Row, Col } from 'antd';
import { Route, Link, BrowserRouter as Router } from 'react-router-dom';

import IconFont from '../component/GetIconFont.js';

import request from 'superagent'

import './ContentPage.less';

const propTypes = {
    url: PropTypes.string
};
const defaultProps = {
    url: config.resources.url_prefix+'main_page.json'
};
export default class ContentPage extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            main_title:'模范标题',
            menu:[]
        };
    }


    createDefault(e,idx,order){
        let name = order?order+'. '+e.name:e.name;
        let element = e.type == 'link'?
            <div className={e.type+'-row'}>
                {e.href && e.href!=''?
                    <a href={e.href} className={e.type} target='_blank'>{name}</a>:
                    <span className={e.type} target='_blank'>{name}</span>      
                }
                {e.sub_href && e.sub_href!=''?
                    <a href={e.sub_href} className={'sub-'+e.type} target='_blank'>{e.sub_name}</a>:
                    ''
                }
            </div>
            :<div className={e.type}>{name}</div>;
        return (
            <Row key={idx}>
                <Col span={24}>
                    {element}
                </Col>
            </Row>
        )
    }
    /**
     * 渲染目录
     */
    renderMenuContent(menu){
        let res = [];
        menu.map((e,idx)=>{
            let ans = this.createDefault(e,idx);
            res.push(ans);
            if(e.data && e.data.length>0){
                e.data.map((sub_e,sub_idx)=>{
                    let sub_ans = this.createDefault(sub_e,(idx+1)*10+sub_idx+1,sub_idx+1);
                    res.push(sub_ans);
                });
            }
        });
        return res;
    }

    render() {
        let menu = this.state.menu;
        let menu_element = this.renderMenuContent(menu);
        let main_title = this.state.main_title;

        return (
            <div className={'sub-page content-page'}>
                {
                    main_title && main_title!=''?
                    <Row key={'main_title'}>
                        <Col span={24}>
                            <span className={'main_title'}>{main_title}</span>
                            
                        </Col>
                    </Row>
                    :''
                }
                {menu_element}
            </div>
        );
    }

    componentDidMount(){
        let url = config.resources.url_prefix + '/main_page.json?version='+config.version;
        request
            .get(url)
            .end((err,resp)=>{
                if(!err){
                    var response = JSON.parse(resp.text)
                    if(response.code == 0){
                        this.setState({
                            main_title:response.title,
                            menu:response.data
                        });
                    }
                }
            });
    }
}
ContentPage.propTypes = propTypes;
ContentPage.defaultProps = defaultProps;