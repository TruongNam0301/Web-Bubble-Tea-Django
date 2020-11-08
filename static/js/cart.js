$('.delete').click(function(){
    stt=$(this).attr('data-stt');
    price = $('.price-item').html();
    $.ajax({
        type: "POST",
        url:'/cart/delete',
        data: {
                'stt':stt,
                'price':price
                },
        success: function(response){
            location.reload();
            
        }
    })
})