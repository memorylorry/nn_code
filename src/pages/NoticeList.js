import config from '../config';
import React from 'react'

import { Card } from 'antd-mobile';
import { List, Avatar, Button, Skeleton } from 'antd-mobile';

const Item = List.Item;
const Brief = Item.Brief;
const { Meta } = Card;

import './NoticeList.less'

export default class NoticeList extends React.Component {

    constructor(props) {
        super(props);
    }


    render() {
        let data = [{

        }];
        return (
            <List className='sub-page'>
                <List.Item
                    arrow="horizontal"
                    onClick={() => { }}
                >
                    Title <Brief>subtitle</Brief>
                </List.Item>
            </List>
        );
    }

}