import React from 'react';
import GetRequestParam from '../util/GetRequestParam';


export default class DefaultPage extends React.Component{
    render(){
        let params = GetRequestParam();
        return (
            <div className={'sub-page'}>
                <h2>{params.content?params.content:'本页正在建设中，尽请期待。'}</h2>
            </div>
        );
    }
}