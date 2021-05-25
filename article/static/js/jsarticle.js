
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
    let id = button.dataset.id
    let result = document.getElementById(id)
    let url = button.dataset.url
    try{
        let res = await makeRequest(url)

        button.setAttribute('data-url', url.replace("likearticle", "unlikearticle"))
        button.innerHTML = '<i class="fas fa-thumbs-down" style="font-size: 20px"></i>'
        button.onclick = onClickUnlice
        result.innerText= res

    }
    catch(e){
        let r = await e.response.json()
        result.innerText= r
    }
}
async function onClickUnlice(event) {
    event.preventDefault()
    let button = event.currentTarget
    let id = button.dataset.id
    let result = document.getElementById(id)
    let url = button.dataset.url
    try{
        let res = await makeRequest(url)
        button.setAttribute('data-url', url.replace("unlikearticle", "likearticle"))
        button.innerHTML = '<i class="fas fa-thumbs-up" style="font-size: 20px"></i>'
        button.onclick = onClick
        result.innerText= res
    }
    catch(e){
        let r = await e.response.json()
        result.innerText= r
    }
}


async function onClickComment(event) {
    event.preventDefault()
    let button = event.currentTarget
    let id = button.dataset.id
    let result = document.getElementById(id)
    let url = button.dataset.url
    try{
        let res = await makeRequest(url)

        button.setAttribute('data-url', url.replace("likecomment", "unlikecomment"))
        button.innerHTML = '<i class="fas fa-thumbs-down" style="font-size: 20px"></i>'
        button.onclick = unClickComment
        result.innerText= res

    }
    catch(e){
        let r = await e.response.json()
        result.innerText= r
    }
}
async function unClickComment(event) {
    event.preventDefault()
    let button = event.currentTarget
    let id = button.dataset.id
    let result = document.getElementById(id)
    let url = button.dataset.url
    try{
        let res = await makeRequest(url)
        button.setAttribute('data-url', url.replace("unlikecomment", "likecomment"))
        button.innerHTML = '<i class="fas fa-thumbs-up" style="font-size: 20px"></i>'
        button.onclick = onClickComment
        result.innerText= res
    }
    catch(e){
        let r = await e.response.json()
        result.innerText= r
    }
}

