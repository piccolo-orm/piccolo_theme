window.onload = function() {
    console.log("custom theme loaded")

    const paramElements = document.getElementsByClassName('sig-param')

    Array(...paramElements).forEach((element) => {
        console.log('adding element ...')
        let brElement = document.createElement('br');
        element.parentNode.insertBefore(brElement, element)
    })

    const lastParamElements = document.querySelectorAll('em.sig-param:last-of-type')

    Array(...lastParamElements).forEach((element) => {
        console.log('adding end element ...')
        let brElement = document.createElement('br');
        element.after(brElement)
    })
}
