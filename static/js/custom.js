$(document).ready(function (){
    
    
    $('.increment-btn').click(function (e) {
        e.preventDefault();

        var inc_value = $(this).closest('.productoData').find('.cantidadInput').val();
        var value = parseInt(inc_value,10);
        value = isNaN(value) ? 0 : value;
        if(value < 10)
        {
            value++;
            $(this).closest('.productoData').find('.cantidadInput').val(value);
        }
    });


    
$('.decrement-btn').click(function (e) {
    e.preventDefault();

    var dec_value = $(this).closest('.productoData').find('.cantidadInput').val();
    var value = parseInt(dec_value,10);
    value = isNaN(value) ? 0 : value;
    if(value > 1)
    {
        value--;
         $(this).closest('.productoData').find('.cantidadInput').val(value);
    }
});

$('.agregarAlCarroBtn').click(function (e){
    e.preventDefault();

    var idProducto = $(this.closest('.productoData')).find('.productoId').val();
    var productoCantidad= $(this).closest('.productoData').find('.cantidadInput').val();
    var token = $('input[name=csfmiddlewaretoken]').val();
    $.ajax({
        method: "POST",
        url: "/agregarAlCarro",
        data: {
            'idProducto': idProducto,
            'productoCantidad': productoCantidad,
            csfmiddlewaretoken: token
        },
        dataType: "dataType",
        success: function(response){
            console.log(response);
        }
    });
});

});