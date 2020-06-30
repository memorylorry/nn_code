import React from 'react';
import ReactDOM from 'react-dom';

// Tag数组
var tags = ['#iconad', '#iconbell', '#iconbackpack', '#iconbadge', '#iconatom', '#iconanchor', '#iconbatteries', '#iconbridge', '#iconbill', '#iconbowling', '#iconbutton', '#iconbuzzer', '#iconbrush', '#iconcalculator', '#iconchair', '#iconcandy', '#iconcolumn', '#iconcastle', '#iconcocktail', '#iconconfig', '#iconconverse', '#icondemoltion', '#iconcrown', '#iconchip', '#icondelivery', '#iconfilm', '#icondonut', '#icondynamite', '#iconflasher', '#iconfolder', '#iconflashlight', '#icongas', '#iconflower', '#iconengine', '#icongraph', '#iconhelmet', '#iconguitar', '#iconhat', '#iconhammer', '#iconhospital', '#iconhotdog', '#iconlamp', '#iconmagnet', '#iconluggage', '#iconmegaphone', '#iconmedal', '#iconmailbox', '#iconmirror', '#iconmonitor', '#iconnote', '#iconpassport', '#iconpicture', '#iconpills', '#iconpen', '#iconplay', '#iconrecycle', '#iconresponsive', '#iconpointer', '#iconplayer', '#iconring', '#iconroad', '#iconrun', '#iconpool', '#iconscan', '#iconsatellite', '#iconserver', '#iconshirt', '#iconship', '#iconspray', '#iconskate', '#iconstar', '#iconthermometer', '#icontower', '#iconswitcher', '#iconstadium', '#icontheatre', '#iconumbrella', '#iconstage', '#iconusb', '#iconvault', '#iconvespa', '#iconvinyl', '#iconwacom', '#iconwallet', '#iconwebcam', '#iconwrench', '#iconwatch', '#iconworkspace'];

// 根据Tag名获取
function getByTag(tag) {
    return (
        <svg className="icon" aria-hidden="true" width="60" height="60">
            <use xlinkHref={tag}></use>
        </svg>
    )
}

// 获取一个图标
function get(data) {
    return (
        <svg className="icon" aria-hidden="true" width="60" height="60">
            <use xlinkHref={data.tag}></use>
        </svg>
    )
}

// 随机获取一个图标
function getRandom(data) {
    let rnd = Math.random() * (tags.length - 1);
    rnd = Math.round(rnd);
    return (
        <svg className="icon" aria-hidden="true" width="60" height="60">
            <use xlinkHref={tags[rnd]}></use>
        </svg>
    )
}

var IconFont = {
    tags:tags,
    getByTag:getByTag,
    get:get,
    getRandom:getRandom
};

export default IconFont;