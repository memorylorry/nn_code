import React from 'react';
import ReactDOM from 'react-dom';
import PropTypes from 'prop-types';

import { Link } from 'react-router-dom';

import { Menu, Icon, Button } from 'antd';
const SubMenu = Menu.SubMenu;

const propTypes = {
  collapsed:PropTypes.bool,
  onChange:PropTypes.func
};
const defaultProps = {
  collapsed:false,
  onChange:(collapsed)=>{}
};
export default class GuideMenu extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        let isShowLogTitle = this.props.collapsed?'none':'inline-block';
        return (
            <div className="leftPanel" style={{ maxWidth: 200 }}>
                <div className="logoArea">
                    <a className="logoHref" href="/">
                        <img src={"/png/logo.png"}></img>
                        <span className="title" style={{display:isShowLogTitle}}>follow ME</span>
                    </a>
                </div>
                <Menu
                    className="guideMenu"
                    defaultSelectedKeys={['1']}
                    defaultOpenKeys={['sub1']}
                    mode="inline"
                    theme="dark"
                    inlineCollapsed={this.props.collapsed}>
                    <Menu.Item key="m1">
                        <Link to="/AssetsAnalysis">
                            <Icon type="github" />
                            <span>资产分析</span>
                        </Link>
                    </Menu.Item>
                    <Menu.Item key="m2">
                        <Link to="/SummaryMethodPage">
                            <Icon type="github" />
                            <span>资产统计方案</span>
                        </Link>
                    </Menu.Item>
                    <Menu.Item key="m3">
                        <Link to="/MarkDownViewer?url=/stock/trader_6_mission.md">
                            <Icon type="github" />
                            <span>理财文章</span>
                        </Link>
                    </Menu.Item>
                    <Menu.Item key="m4">
                        <Link to="/CardList">
                            <Icon type="github" />
                            <span>卡片列表</span>
                        </Link>
                    </Menu.Item>
                </Menu>
            </div>
        );
    }
}
GuideMenu.propTypes = propTypes;
GuideMenu.defaultProps = defaultProps;