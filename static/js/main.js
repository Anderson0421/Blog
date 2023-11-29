// Nuevo Post - Modal

const NewPost = document.getElementById('NewPost');
const ModalNew = document.getElementById('ModalNew');
const CloseModal = document.getElementById('CloseModal');

NewPost.addEventListener('click',()=>{
    ModalNew.classList.remove('hidden')
})

CloseModal.addEventListener('click',()=>{
    ModalNew.classList.add('hidden')
})


