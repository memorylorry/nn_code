import React from 'react'
// 引入编辑器组件
import BraftEditor from 'braft-editor'
// 引入编辑器样式
import 'braft-editor/dist/index.css'

export default class EditorPage extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            editorState: BraftEditor.createEditorState(null)
        }

        this.changeHandler = this.changeHandler.bind(this);
        this.submitContent = this.submitContent.bind(this);
    }

    changeHandler(editorState){
        this.setState({ editorState });
    }
    
    submitContent(){
        const htmlContent = this.state.editorState.toHTML();
        console.log(htmlContent);
    }
    
    render() {
        const {editorState} = this.state;

        let controls_str = [
            'undo', 'redo', 'separator',
            'font-size', 'line-height', 'letter-spacing', 'separator',
            'text-color', 'bold', 'italic', 'underline', 'strike-through', 'separator',
            'superscript', 'subscript', 'remove-styles', 'emoji',  'separator', 'text-indent', 'text-align', 'separator',
            'headings', 'list-ul', 'list-ol', 'blockquote', 'code', 'separator',
            'link', 'separator', 'hr', 'separator',
            'media', 'separator',
            'clear'
        ];

        const extendControls = [
            'separator',
            {
                key: 'save-button', // 控件唯一标识，必传
                type: 'button',
                title: '提交文档', // 指定鼠标悬停提示文案
                className: 'save-button', // 指定按钮的样式名
                html: null, // 指定在按钮中渲染的html字符串
                text: '提交', // 指定按钮文字，此处可传入jsx，若已指定html，则text不会显示
                onClick: () => {
                    this.submitContent();
                },
            }
        ]
        
        // 通过ref属性来将编辑器实例赋值给this.editorInstance
        return <BraftEditor value={editorState}
                    controls={controls_str}  
                    extendControls={extendControls}
                    onChange={this.changeHandler}
                    onSave={this.submitContent}
                    ref={instance => this.editorInstance = instance} />
    }

}