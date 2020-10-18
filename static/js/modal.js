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
    setDataModal(item);
    makeInputRadio();
})

function setDataModal(item){
    var image = item.find('img').attr('src');
    var name = item.find('.name-product').text();
    var price = item.find('.price-new').text();
    $('.modal-body').find('img').attr('src',image);
    $('.modal-body').find('h3').html(name);
    $('.modal-body').find('h4').html(price);
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
    var size = $("input[name=size]:checked").val();
    var sugar = $("input[name=sugar]:checked").val();
    var checkboxValues = [];
    $('input[name=topping]:checked').map(function() {
        checkboxValues.push($(this).val());
    });
    console.log(checkboxValues);
})

function alertTopping() {
    $("input[name='topping']").on('change', function (e) {
        if ($('input[name=topping]:checked').length > 2) {
            $(this).prop('checked', false);
            alert("allowed only 3");
        }
    });
}

           