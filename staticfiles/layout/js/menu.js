// menu load
$(document).ready(function () {
    $(".nav-item a").click(function (){
        var contentLink = $(this).attr('id');
        // console.log(contentLink);
        // $("#bodyContent").remove();
        $(".container-fluid").load(contentLink);
    });
    $(". a").click(function (){
        var contentLink = $(this).attr('id');
        // console.log(contentLink);
        // $("#bodyContent").remove();
        $(".container-fluid").load(contentLink);
    });
})
