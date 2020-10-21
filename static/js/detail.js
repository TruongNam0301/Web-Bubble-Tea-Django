$( document ).ready(function() {
     alertTopping();
});

function alertTopping() {
    $("input[name='topping']").on('change', function (e) {
        if ($('input[name=topping]:checked').length > 2) {
            $(this).prop('checked', false);
            alert("allowed only 3");
        }
    });
}

$('.btn-buy').click(function(){
    var id = $('.product-detail').attr('data-id');
    var size = $("input[name=size]:checked").val();
    var sugar = $("input[name=sugar]:checked").val();
    var quantity = $("input[name=quantity]").val()
    var toppings = [];
    $('input[name=topping]:checked').map(function() {
        toppings.push($(this).val());
    });
    console.log(quantity);
    $.ajax({
        type: "POST",
        url:'/products/addCart',
        data: {
                'toppings[]':toppings,
                'id':id,
                'quantity':quantity,
                'size':size,
                'sugar':sugar,
                },
        success: function(response){
            $('.total_quantity').html(response)
        }
    })
})