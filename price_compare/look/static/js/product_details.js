


const target = document.getElementById('my_message').innerHTML;
            if (target == ""){
                document.getElementById('my_message').innerHTML=""
            }
        else if (target == "comments cannot be empty" || "comments successfully added"){
            setTimeout(

         myGreeting=() =>{
            document.getElementById('my_message').innerHTML=""
        }
            
            ,5000)}  


// Added code for facebook share, whatsapp share, email share and comments post
// facebook url 
// Emmanuel please note you have to change the URL to share to reflect the "Application URL"
// I also used variable grab to get the current window url but i think this is supposed to be "Application URL" too
// The comment aspect is also for rendering, the comment disappear when page is reloaded
//  I believe you have a way of inserting the name and date as per user data stored in database
const shareOnFacebook = ()=>{
    let navUrl = 'https://www.facebook.com/sharer/sharer.php?u=' + document.URL
    window.open(navUrl , '_blank');
}

// share "select" option

const media = document.getElementById("shareMedia")
const share = document.getElementById("share-btn")
const grab = document.URL

share.addEventListener('click', () => {
    if (media.value == "fbk"){
        shareOnFacebook()
    } 
    else if (media.value == "wthp"){       
        
        window.open("whatsapp://send?text=" + grab,'_blank' )
        
    }
        
    else if (media.value == "email") {
        document.getElementById('mailSh').click()
        
    }
})





