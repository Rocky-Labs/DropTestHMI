$(function() {

    // SETUP
    var $list, $newItemForm, $newItemButton;
    var item = '';                                // item is an empty string
    $list = $('ul');                               // Cache the unordered list
    $newItemForm = $('#newItemForm');              // Cache form to add new items
    $newItemButton = $('#newItemButton');          // Cache button to show form

   // var dt = new Date();

    //$('dateTime').html(dt.val());
  
    $('li').hide().each(function(index) {          // Hide list items
      $(this).delay(450 * index).fadeIn(1600);     // Then fade them in
    });
  
    // ITEM COUNTER
    function updateCount() {                       // Create function to update counter
      var items = $('li[class!=complete]').length; // Number of items in list
      $('#counter').text(items);                   // Added into counter circle
    }
    updateCount();                                 // Call the function
  
    // SETUP FORM FOR NEW ITEMS
    $newItemButton.show();                         // Show the button
    $newItemForm.hide();                           // Hide the form
    $('#showForm').on('click', function() {        // When click on add item button
      $newItemButton.hide();                       // Hide the button
      $newItemForm.show();                         // Show the form
    });
    console.log($('input[name=rdo]:checked').val());
    $('input[name=rdo]').click(function() {
      console.log(document.getElementById("yes").checked == true);
      console.log(document.getElementById("no").checked == true);
      console.log($('input[name=rdo]:checked').val());
    });

    // ADDING A NEW LIST ITEM
    $newItemForm.on('submit', function(e) {       // When a new item is submitted
      e.preventDefault();                         // Prevent form being submitted
    
      $.ajax({
        data: {
            item1: $('#itemDescription').val(),
            EmployeeName: $('#EmployeeName').val(),
            Test:  $('input[name=rdo]:checked').val()
        },
        type: 'POST',
        url: '/formProcess'

    })
    .done(function(data){
        if(data.error){
            $('#errorAlert').text(data.error).show();

        }
        else
        {
          $list.append('<li>' + "SAP #: " + data.item1 + " | "+ " Status: "+ data.Test + '</li>');      // Add item to end of the list
          
        }
       
    })


//      var text = $('#itemDescription').val();
//    var text2 =$('#itemDescription2').val();       // Get value of text input




      //$list.append('<li>' + text(data.item1) + '</li>');      // Add item to end of the list
     //$list.append('<li>' + data.item2 + '</li>');  
      //$(data.item1).val('');                    // Empty the text input
      //$(data.EmployeeName).val('');
      updateCount();   
      $('form')[0].reset();                            // Update the count
    });
  
    // CLICK HANDLING - USES DELEGATION ON <ul> ELEMENT
    $list.on('click', 'li', function() {
      var $this = $(this);               // Cache the element in a jQuery object
      var complete = $this.hasClass('complete');  // Is item complete
  
      if (complete === true) {           // Check if item is complete
        $this.animate({                  // If so, animate opacity + padding
          opacity: 0.0,
          paddingLeft: '+=180'
        }, 500, 'swing', function() {    // Use callback when animation completes
          $this.remove();                // Then completely remove this item
        });
      } else {                           // Otherwise indicate it is complete
        item = $this.text();             // Get the text from the list item
        $this.remove();                  // Remove the list item
        $list                            // Add back to end of list as complete
          .append('<li class=\"complete\">' + item + '</li>')
          .hide().fadeIn(300);           // Hide it so it can be faded in
        updateCount();                   // Update the counter
      }                                  // End of else option
    });                                  // End of event handler
  
  });