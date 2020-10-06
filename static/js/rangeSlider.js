var rangeSlider = function(){
    var slider = $('.range-slider'),
        range =  $('.range-slider__range'),
        arrowUp= $('.arrow_Up'),
        arrowDown= $('.arrow_Down'),
        default_button= $('.default_btn'),
        value = $('.range-slider__value');

    
    slider.each(function() {
        // sees the attribute on Html and displays it
        value.each(function() {
           var value = $(this).prev().attr('value');
           $(this).html(value);
           
            
        });
        //Slider function
        range.on('change', function(){
            $(this).next(value).html(this.value);

            var temp = value.val();
            //Adds one value when is click
          temp = range.val(parseInt(range.val()) );

          //Displays values into span
        $('.range-slider__value').html(temp.val());
         //shows it on the log
        console.log(parseInt(temp.val()));

        $.ajax({
          data: {
              btn_range: temp.val() 
  
          },
          type: 'POST',
          url: '/SliderProcess'
  
      })
      .done(function(data){
          if(data.error){
              $('#errorAlert').text(data.error).show();
  
          }
          else
          {
            $list.append('<li>' + data.item1 + '</li>');      // Add item to end of the list
            $list.append('<li>' + data.item2 + '</li>');  
          }
         
      })



        });
     // arrow up function that counts everytime is click
        arrowUp.click(function() {
          var temp = value.val();
            //Adds one value when is click
          temp = range.val(parseInt(range.val()) + 500 );

          //Displays values into span
        $('.range-slider__value').html(temp.val());
         //shows it on the log
        console.log(parseInt(temp.val()));

        $.ajax({
          data: {
              btn_up: temp.val() 
  
          },
          type: 'POST',
          url: '/btnUpProcess'
  
      })
      .done(function(data){
          if(data.error){
              $('#errorAlert').text(data.error).show();
  
          }
          else
          {
            $list.append('<li>' + data.item1 + '</li>');      // Add item to end of the list
            $list.append('<li>' + data.item2 + '</li>');  
          }
         
      })

        });

  // arrow down function that counts everytime is click
        arrowDown.click(function() {
            var temp = value.val();
            //subtract one value when is click
            temp = range.val(parseInt(range.val()) - 500 );
           //Displays values into span
           $('.range-slider__value').html(temp.val());
           //Shows it on the log
           console.log(parseInt(temp.val() ));


           $.ajax({
            data: {
                btn_down: temp.val()
    
            },
            type: 'POST',
            url: '/btnDownProcess'
    
        })
        .done(function(data){
            if(data.error){
                $('#errorAlert').text(data.error).show();
    
            }
            else
            {
              $list.append('<li>' + data.item1 + '</li>');      // Add item to end of the list
              $list.append('<li>' + data.item2 + '</li>');  
            }
           
        })


          });

          default_button.click(function() {
            var temp = 200;
            //subtract one value when is click
            range.val(parseInt(temp));
           //Displays values into span
           $('.range-slider__value').html(temp);
           //Shows it on the log
           console.log(parseInt(temp ));


           $.ajax({
            data: {
                btn_default: 200
    
            },
            type: 'POST',
            url: '/btnDefaultProcess'
    
        })
        .done(function(data){
            if(data.error){
                $('#errorAlert').text(data.error).show();
    
            }
            else
            {
              $list.append('<li>' + data.item1 + '</li>');      // Add item to end of the list
              $list.append('<li>' + data.item2 + '</li>');  
            }
           
        })

          });

    });
};

rangeSlider();