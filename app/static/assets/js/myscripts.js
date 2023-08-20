var $ = jQuery;
$(document).ready(function(){

$(".cart-plus").on('click',function(e){
   e.preventDefault()
   pid = $(this).attr('pid').toString()
   console.log("pid ",pid);

   $.ajax({
      type:'GET',
      url:'/pluscart',
      data:{
         prod_id:pid
      },
      success:function(data){
         console.log("data =", data)
         //eml.innerText=data.quantity
         document.getElementById("amount").innerText=data.amount
         document.getElementById("totalamount").innerText=data.totalamount
         $('#'+pid).val(data.quantity)
      }
   })
})

$(".cart-minus").on('click',function(e){
      e.preventDefault()
      pid = $(this).attr('pid').toString()
      //console.log("pid ",pid);
      eml=this;

      $.ajax({
         type:'GET',
         url:'/minuscart',
         data:{
            prod_id:pid
         },
         success:function(data){
            console.log("data =", data)
            //eml.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
            $('#'+pid).val(data.quantity)
            //eml.parentNode.parentNode.parentNode.parentNode.remove()
         }
      })
})

$(".removecart").on('click',function(e){
   e.preventDefault()
   pid = $(this).attr('pid').toString()
   //console.log("pid ",pid);
   eml=this;

   $.ajax({
      type:'GET',
      url:'/removecart',
      data:{
         prod_id:pid
      },
      success:function(data){
         console.log("data =", data)
         //eml.innerText=data.quantity
         document.getElementById("amount").innerText=data.amount
         document.getElementById("totalamount").innerText=data.totalamount
         $('#'+pid).val(data.quantity)
         //eml.parentNode.parentNode.parentNode.parentNode.remove()
         $(".table").load(window.location.href + " .table" );

      }
   })
 })
});