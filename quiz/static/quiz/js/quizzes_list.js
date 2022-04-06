const nav = document.querySelector('#navActive');
let navigation = nav.value;
console.log(navigation);

const all = document.querySelector('#all');
const following = document.querySelector('#following');
const my = document.querySelector('#my');
const quizTaken = document.querySelector('#quizTaken');

const topNavigation = document.querySelectorAll('.topNavigation');




if (navigation == 'quizzes'){
    all.classList.add('active')
    topNavigation[0].classList.add('active');
}else if (navigation == 'following-quizzes'){
    following.classList.add('active')
    topNavigation[0].classList.add('active');
}else if (navigation == 'my-quizzes'){
    my.classList.add('active')
    topNavigation[0].classList.add('active');
}else if (navigation == 'quizTaken'){
    quizTaken.classList.add('active')
    topNavigation[0].classList.add('active');
}




$('.likeForm').submit(function(e){
    e.preventDefault();
const serializeData = $(this).serialize()
const quiz_id = $(this).data('quiz')
// alert('Still working!')
// alert(serializeData)
$.ajax({
    type: 'POST',
    url : $(this).data('url'),
    data : serializeData,
    success : function(response){
        // alert('It works');
        // document.querySelector('#deleteButton').parentNode.parentNode.style.display = 'none';
        // console.log(id);
        // console.log(response)
        
        if (response == 'liked'){
            // console.log($(`#likeButton${id}`));
            $(`#likeButton${quiz_id}`).text('unlike');
        }else if (response == 'unliked'){
            // console.log($(`#unlikeButton${id}`));
            $(`#likeButton${quiz_id}`).text('like');
        }
        

    },
    error : function(){
        alert('It falis silently!')
    }

});
})
