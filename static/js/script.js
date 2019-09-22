/**
==================================

 copy tokken 

==================================
**/
function copyToken() {
  const el = document.createElement('textarea');
  el.value = "%%%%%%%%";
  document.body.appendChild(el);
  el.select();
  document.execCommand('copy');
  document.body.removeChild(el);
  $.notify("Token copied", "success");
}
$( "#copyToken" ).mouseover(function() {
  $("#copyToken").html("############################")
});
$( "#copyToken" ).mouseout(function() {
  $("#copyToken").html("Get token")
});




/**
==================================

 input range helper func  

==================================
**/
function updateTextInput(val) {
          document.getElementById('textInput').innerHTML=val; 
}

function updateTextInput2(val) {
          document.getElementById('textInput2').innerHTML=val; 
}



/**
==================================

 submit animation  

==================================
**/


$('#voice_form').submit(function(){
  $('.cssload-bell').css('visibility', 'visible');
  return true;
});
/**
==================================

 file helper functions 

==================================
**/
'use strict';

;( function( $, window, document, undefined )
{
	$( '.inputfile' ).each( function()
	{
		var $input	 = $( this ),
			$label	 = $input.next( 'label' ),
			labelVal = $label.html();

		$input.on( 'change', function( e )
		{
			var fileName = '';

			if( this.files && this.files.length > 1 )
				fileName = ( this.getAttribute( 'data-multiple-caption' ) || '' ).replace( '{count}', this.files.length );
			else if( e.target.value )
				fileName = e.target.value.split( '\\' ).pop();

			if( fileName )
				$label.find( 'span' ).html( fileName );
			else
				$label.html( labelVal );
		});

		// Firefox bug fix
		$input
		.on( 'focus', function(){ $input.addClass( 'has-focus' ); })
		.on( 'blur', function(){ $input.removeClass( 'has-focus' ); });
	});
})( jQuery, window, document );


$('.tog').click(function() {  
	$('.audio-player').toggle()

});


/**
==================================

 link click conformation 

==================================
**/
$('.link_del_track').click(function(){
    return confirm("Are you sure you want to delete track?");
})