const init = () => {
    const inputArea = document.querySelector('#js-userinput');
    const button = document.querySelector('#js-go');

    let keyword;
    inputArea.addEventListener('keydown', e => {
        if (e.key === 'Enter') {
            searchAndPush(inputArea.value);
        }
    });
    button.addEventListener('click', e => {
        searchAndPush(inputArea.value);
    });
};


const searchAndPush = keyword => {
    const API_KEY = 'PdBtKCXj8CkSQCOSxL6SN6BZ2aQsvtlI';
    const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${API_KEY}`;
    /*
    AJAX 요청
    1. 어떤 이벤트가 발생한다.
    2. 요청을 전송하고, 응답이 도착할 때까지 기다린다. 화면 전환은 없다.
    3. 응답이 오면, 지금 문서에서 응답 내용을 추가로 render 한다.
     */
    const AJAXCall = new XMLHttpRequest();
    AJAXCall.open('GET', URL);
    AJAXCall.send();
    AJAXCall.addEventListener('load', e => {
        const JSONData = JSON.parse(e.target.response);
        pushToDom(JSONData);
    });

    const pushToDom = dataset => {
        const resultArea = document.querySelector('#result-area');
        resultArea.innerHTML = null;
        const dataArray = dataset.data;
        let imageURL;
        let element;
        for (let imgData of dataArray) {
            imageURL = imgData.images.fixed_height.url;
            element = document.createElement('img');
            element.className = 'container-image';
            element.src = imageURL;
            element.alt = imgData.title;
            resultArea.appendChild(element);
        }
    };
};

init();