let updateBtns = document.getElementsByClassName('update-cart')
for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        let itemId = this.dataset.product
        let action = this.dataset.action

        if (user === 'AnonymousUser') {
            addCookieItem(itemId, action)

        } else {
            updateUserOrder(itemId, action)
        }
    })
}

function addCookieItem(itemId, action) {
    if (action === 'add') {
        if (cart[itemId] === undefined) {
            cart[itemId] = {'quantity': 1};
        } else {
            cart[itemId]['quantity'] += 1
        }
    }
    if (action === 'remove') {
        cart[itemId]['quantity'] -= 1
        if (cart[itemId]['quantity'] <= 0) {
            delete cart[itemId]
        }
    }
}

function updateUserOrder(itemId, action) {
    let url = '/update_item/'
    fetch(url, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'itemId': itemId, 'action': action})
    })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            location.reload()
        })
}