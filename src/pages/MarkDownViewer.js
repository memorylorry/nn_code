import React from 'react';

import { Button } from 'antd';

import marked from 'marked';
import hljs from 'highlight.js';

import GetRequestParam from '../util/GetRequestParam';

export default class MarkDownViewer extends React.Component {
    fetchData(url){
        let res = '';
        $.ajax({
            url: url,
            async:false,
            success:(data)=>{
                res = data;
            }
        });
        return res;
    }
    constructor(props){
        super(props);
    }
    render() {
        let params = GetRequestParam();
        let url = '/articles/' + params.url;
        console.log(params);
        let res = this.fetchData(url);
        return (
            <div className="sub-page markdown-html"
                dangerouslySetInnerHTML={{
                    __html: marked(res)
                }}
            >
            </div>
        )
    }
    componentDidMount(){
        // marked相关配置
        marked.setOptions({
            renderer: new marked.Renderer(),
            gfm: true,
            tables: true,
            breaks: true,
            pedantic: false,
            sanitize: true,
            smartLists: true,
            smartypants: false,
            highlight: function(code) {
                return hljs.highlightAuto(code).value;
            },
        });
        hljs.initHighlightingOnLoad();
    }
    componentDidUpdate(){
        // marked相关配置
        marked.setOptions({
            renderer: new marked.Renderer(),
            gfm: true,
            tables: true,
            breaks: true,
            pedantic: false,
            sanitize: true,
            smartLists: true,
            smartypants: false,
            highlight: function(code) {
                return hljs.highlightAuto(code).value;
            },
        });
        hljs.initHighlightingOnLoad();
    }
}