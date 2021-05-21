
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


async function makeRequest(url, method='GET', body) {
    let headers = {
        'X-CSRFToken':getCookie('csrftoken')
    }
    let response = await fetch(url, {method, headers:headers, body:body});
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
    let result = document.getElementById('result')
    let a = document.getElementById('A').value
    let b = document.getElementById('B').value
    let data = {"A": a, "B": b}
    let url = event.target.dataset.url
    try{
        let res = await makeRequest(url, "POST", JSON.stringify(data))
        result.innerHTML = `Результат: ${res.answer}`
    }
    catch(e){
        let r = await e.response.json()
        result.innerText= r.answer
    }
}

async function tokenGet(){
    await makeRequest('http://localhost:8000/api_v1/get_token')
}
window.addEventListener('load', tokenGet)