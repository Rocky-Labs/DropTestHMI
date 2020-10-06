$(function() {

  var $list;
  $list = $('ul'); 
  

    $('.drop_btn').click(function() {
       
      console.log('Drop btn click');

          
       // e.preventDefault();                         // Prevent form being submitted
      
        $.ajax({
          data: {
              di1: 1,
              di2: 0
  
          },
          type: 'POST',
          url: '/DropProcess'
  
      })
      .done(function(data){
          if(data.error){
              $('#errorAlert').text(data.error).show();
  
          }
          else
          {
            $('#errorAlert').text(data.error).show();    // Add item to end of the list
            
          }
         
      })
       
    });

      $('.close_btn').click(function() {
       
        console.log('close btn click');
        
        $.ajax({
          data: {
              di1: 1,
              di2: 0
  
          },
          type: 'POST',
          url: '/CloseProcess'
  
      })
      .done(function(data){
          if(data.error){
              $('#errorAlert').text(data.error).show();
  
          }
          else
          {
            $('#errorAlert').text(data.error).show();  
          }
         
      })

        });

});

