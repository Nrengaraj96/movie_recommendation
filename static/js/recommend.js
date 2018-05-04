$(function(){
        $('#recommendbutton').click(function(){
                 
		 $.ajax({
                        url: '/recommend',
                        data: $('form').serialize(),
                        type: 'POST',
                        success: function(response){
                                console.log(response);
                        },
                        error: function(error){
                                console.log(error);
                        }
                });
        });
});
