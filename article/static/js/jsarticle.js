
async function makeRequest(url, method='GET') {

    let response = await fetch(url, {method});
    if (response.ok) {  // нормальный ответ
        return await response.json();
    } else {            // ошибка
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

async function onClick(event) {
    event.preventDefault()
    let button = event.currentTarget
    let result = document.getElementById('result')
    let url = button.dataset.url
    console.log(url)
    try{
        let res = await makeRequest(url)
        result.innerHTML = `Результат: ${res.answer}`
        button.setAttribute('data-url', url.replace("likearticle", "unlikearticle"))
        button.innerHTML = '<i class="fas fa-thumbs-down" style="font-size: 20px"></i>'
        button.onclick = onClickDis
    }
    catch(e){
        let r = await e.response.json()
        // result.innerText= r.answer
    }
}
async function onClickDis(event) {

}


async function tokenGet(){
    await makeRequest('http://localhost:8000/api_v1/get_token')
}
window.addEventListener('load', tokenGet)