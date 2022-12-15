// // facebook url 
// let shareOnFacebook = ()=>{
//     const navUrl = 'https://www.facebook.com/sharer/sharer.php?u=' + 'https://www.jumia.com.ng/generic-lebaiqi-over-ear-powerful-bass-stereo-bluetooth-4.0-headphone-handsfree-wireless-headset-with-microphone-fm-radio-micro-sd-card-slot-19145560.html';
//     window.open(navUrl , '_blank');
//   }

//   // share via facebook
// shares.forEach(share => {
//     share.addEventListener('click', () => {
//         shareOnFacebook()
//     })
// })

// posting comments
// let commentBody = document.querySelectorAll(".user-comment ul")
// let comment = document.querySelector("#comment")
// let commentButton = document.querySelector([data-comment])

// commentButton.addEventListener('click', () =>{
//     commentBody.appendchild() = comment.value
// })



const target = document.getElementById('my_message').innerHTML;
        if (target == "comments cannot be empty" || "comments successfully added"){
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
let shareOnFacebook = ()=>{
    const navUrl = 'https://www.facebook.com/sharer/sharer.php?u=' + 'https://www.jumia.com.ng/generic-lebaiqi-over-ear-powerful-bass-stereo-bluetooth-4.0-headphone-handsfree-wireless-headset-with-microphone-fm-radio-micro-sd-card-slot-19145560.html';
    window.open(navUrl , '_blank');
}


// posting comments

const commentButton = document.querySelector("[data-comment]")
commentButton.addEventListener('click', () =>{
let textInput = document.getElementById("comment");
if(textInput.value !==""){
    let node = document.createElement("LI");  
    node.innerHTML = textInput.value;
    textInput.value="";
    document.getElementById("list").appendChild(node);
  }else {
    alert("Comment box is empty, kindly use the textarea provided below")
  
}
})


// share "select" option

let media = document.querySelector("#shareMedia")
const share = document.querySelector("[data-share]")
const grab = document.URL

share.addEventListener('click', () => {
    if (media.value === "fbk"){
        shareOnFacebook()
    } 
    else
    if (media.value === "wthp"){       
        
        window.open("whatsapp://send?text=" + grab,'_blank' )
        
    }
        
    else if (media.value === "email") {
        document.getElementById('mailSh').click()
        
    }
})



