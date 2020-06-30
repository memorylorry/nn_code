import React from 'react';
var myMarked = require('marked');
import hljs  from 'highlight.js'

// Set options
// `highlight` example uses `highlight.js`
myMarked.setOptions({
    renderer: new myMarked.Renderer(),
    highlight: function (code) {
        return hljs.highlightAuto(code).value;
    },
    pedantic: false,
    gfm: true,
    tables: true,
    breaks: false,
    sanitize: false,
    smartLists: true,
    smartypants: false,
    xhtml: false
});

export default myMarked;