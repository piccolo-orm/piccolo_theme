
/**
 * We add extra br tags to the autodoc output, so each parameter is shown on
 * its own line.
 */
function setupAutodoc() {
    const paramElements = document.getElementsByClassName('sig-param')

    Array(...paramElements).forEach((element) => {
        console.log('adding element ...')
        let brElement = document.createElement('br')
        element.parentNode.insertBefore(brElement, element)
    })

    const lastParamElements = document.querySelectorAll('em.sig-param:last-of-type')

    Array(...lastParamElements).forEach((element) => {
        console.log('adding end element ...')
        let brElement = document.createElement('br')
        element.after(brElement)
    })
}

function setupSearchSidebar() {
    document.querySelector('form.search input[type=text]').placeholder = 'Search...'

    document.querySelector('form.search input[type=submit]').value = 'Search'
}

window.onload = function() {
    console.log("custom theme loaded")

    setupAutodoc()
    setupSearchSidebar()
}
