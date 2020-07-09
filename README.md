# Image-Augmentation-Bounding-Box-MultipleClasses

To prevent google collab from disconnecting:
function ConnectButton(){
    console.log("Connect pushed"); 
    document.querySelector("#top-toolbar > colab-connect-button").shadowRoot.querySelector("#connect").click() 
}
setInterval(ConnectButton,60000);
