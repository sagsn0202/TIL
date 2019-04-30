const DOMAIN = 'https://jsonplaceholder.typicode.com/';
const RESOURCE = 'posts/';
const QUERY_STRING = '';
const URL = DOMAIN + RESOURCE + QUERY_STRING;

const XHR = new XMLHttpRequest();
// 요청을 만들고, 정보를 담고, 보내고, 기다린다.
XHR.open('POST', URL);
XHR.setRequestHeader(
    'Content-Type',
    'application/json;charset=UTF-8'
);
XHR.send(
    JSON.stringify({"title": "NewPOST", "body": "This is New Post", "userId": 1})
);
XHR.addEventListener('load', e => {
    const parseData = JSON.parse(e.target.response);
    console.log(parseData);
});