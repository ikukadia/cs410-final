window.addEventListener("load", onLoad);

function onLoad() {
    document.getElementById('input-file').addEventListener('change', getFile)

    function getFile(event) {
        const input = event.target
        if ('files' in input && input.files.length > 0) {
            placeFileContent(document.getElementById('content-target'), input.files[0])
        }
    }
    
    function placeFileContent(target, file) {
        readFileContent(file).then(content => {
              target.value = content
        }).catch(error => console.log(error))
    }
    
    function readFileContent(file) {
        const reader = new FileReader()
        return new Promise((resolve, reject) => {
            reader.onload = event => resolve(event.target.result)
            reader.onerror = error => reject(error)
            reader.readAsText(file)
        })
    }
}

function toggleDiv(){
    var div = document.getElementById("tab-id")
    div.style.display = div.style.display == "none" ? "block" : "none"
}