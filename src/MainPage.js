import config from './config';
import React from 'react';
import ReactDOM from 'react-dom';

import { Menu } from 'antd';
const { SubMenu } = Menu;
import { Route, Switch, Link, BrowserRouter } from 'react-router-dom';

import NotLiveRoute from 'react-live-route'
import { withRouter } from 'react-router-dom'

const LiveRoute = withRouter(NotLiveRoute)

import IconFont from './component/GetIconFont';
import AppList from './pages/AppList';
import NoticeList from './pages/NoticeList';
import ContentPage from './pages/ContentPage';
import DefaultPage from './pages/DefaultPage';

import request from 'superagent'

import './MainPage.less';
import './Common.less';

export default class MainRoute extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            menu:[],
            current: "0"
        }
        this.handleClick = this.handleClick.bind(this);
    }

    componentDidMount(){
        let url = config.resources.url_prefix + '/menu.json';
        request
            .get(url)
            .end((err,resp)=>{
                if(!err){
                    var response = JSON.parse(resp.text)
                    this.setState({menu:response.data})
                }
            });
    }

    handleClick (e) {
        // console.log('click ', e);
        let type = e.item.props.type;
        if(type!='link'){
            this.setState({ current: e.key });
            window.scrollTo(0,0);
        }
    };

    
    createDefault(e,idx){
        if(e.type=='component'){
            return <Menu.Item key={idx} >
                    <Link to={e.href}>{e.name}</Link>
                </Menu.Item>;
        }
        if(e.type=='link'){
            return <Menu.Item key={idx} type='link'>
                    <a target='_blank' href={e.href}>{e.name}</a>
                </Menu.Item>;
        }
    }
    render() {
        const { current } = this.state;
        let menu = this.state.menu;
        let element = [];
        menu.map((e,idx)=>{
            if(e.skip)return;
            if(e.type=='component'||e.type=='link'){
                element.push(
                    this.createDefault(e,idx)
                );
            }
            if(e.type=='SubMenu'){
                element.push(
                    <SubMenu key={idx} title={e.name} type='SubMenu'>
                        {
                            e.data.map((sub_e,sub_idx)=>{
                                return this.createDefault(sub_e,"setting:"+((idx+1)*10+sub_idx));
                            })
                        }
                    </SubMenu>
                );
            }
        });

        return (
            <BrowserRouter>
                <div className='common-page'>
                    <Menu onClick={this.handleClick} selectedKeys={[current]} mode="horizontal">
                        <Menu.Item key="logo" style={{fontSize:0,background:'#f9a623'}} >
                            <a href={config.resources.root}>
                                <img src='./dist/png/logo.png' />.
                            </a>
                        </Menu.Item>
                        {element}
                    </Menu>
                    <Route exact path="/" component={ContentPage} />
                    <Route exact path="/py-demo" component={ContentPage} />
                    <Route path="/DefaultPage" component={DefaultPage} />
                </div>
            </BrowserRouter>
        )
    }
}


ReactDOM.render(
    <MainRoute />,
    document.getElementById('root')
);