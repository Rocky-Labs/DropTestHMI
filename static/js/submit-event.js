(function () {
    var form = document.getElementById('login'); // get from element
    
   // var displaySetting = rowf.style.display; 

    addEvent(form, 'submit', function(e) { //when user submit form 
                 e.preventDefault();  //stop being sent
                 var elements = this.elements;  //get all forms elements
                 var username = elements.username.value;
                 var msg = ' Welcome ' + username;
                 document.getElementById('main').textContent = msg;
                 
                 });
  
 }()); 