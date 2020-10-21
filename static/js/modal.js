$( document ).ready(function() {
    $(window).scroll(function(){
        if(window.pageYOffset>280){
            $('.menu').addClass('menu-scroll')
        }
        else{
            $('.menu').removeClass('menu-scroll')
        }
    })
     alertTopping();
});

$('.btn-buy').click(function(){
    var item = $(this).parent().parent().parent();
    $('input[type=checkbox]').prop('checked',false); 
    $('input[name=quantity]').prop('value',1);
    setDataModal(item);
    makeInputRadio();
})

function setDataModal(item){
    var image = item.find('img').attr('src');
    var name = item.find('.name-product').text();
    var price = item.find('.price-new').text();
    var id = item.data('id');
    $('.modal-body').find('img').attr('src',image);
    $('.modal-body').find('h3').html(name);
    $('.modal-body').find('h4').html(price);
    $('.modal-content').attr('data-id',id);
}

function makeInputRadio(){
    let size = "<h4>Choose Size:</h4><input type='radio' id='sizeM' name='size' value='M' checked='checked'><label for='sizeM'>M</label><input type='radio' id='sizeL' name='size' value='L'><label for='sizeL'>L</label>"
    $('.size').html(size);
    let sugar = "<h4>Choose Sugar:</h4><input type='radio' name='sugar' value='100' checked='checked'><label>100% sugar</label>"
    +"<input type='radio' name='sugar' value='75'><label>75% sugar</label>"
    +"<input type='radio' name='sugar' value='50'><label>50% sugar</label>"
    +"<input type='radio' name='sugar' value='30'><label>30% sugar</label>";
    $('.sugar').html(sugar);
}

$('.save-modal').click(function(){
    var id = $('.modal-content').attr('data-id');
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

function alertTopping() {
    $("input[name='topping']").on('change', function (e) {
        if ($('input[name=topping]:checked').length > 2) {
            $(this).prop('checked', false);
            alert("allowed only 3");
        }
    });
}

           