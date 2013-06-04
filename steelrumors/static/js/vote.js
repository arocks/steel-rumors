jQuery(document).ready(function($) 
    {
	$(".vote_form").submit(function(e) 
		{
		    e.preventDefault(); 
		    var btn = $("button", this);
		    var l_id = $(".hidden_id", this).val();
		    btn.attr('disabled', true);
		    $.post("/vote/", $(this).serializeArray(),
			  function(data) {
			      if(data["voteobj"]) {
				  btn.text("-");
			      }
			      else {
				  btn.text("+");
			      }
			  });
		    btn.attr('disabled', false);
		});
    });