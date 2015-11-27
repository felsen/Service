function call_fun()
{
	 var stage_name=document.getElementById('stage_name').value;
	 var course_name=document.getElementById('stageCategory').value;
	 
		 $.ajax({
			type:"POST",
			url:"check.php",
			data:{
			 stage_name:stage_name,
			 course_name:course_name
		 },
			 success:function(result){
     // $("#result").html(result);
    }
		 });
	
}

function subcategory_enter()
{
	 var sel_stage_name=document.getElementById('sel_stage_name').value;
	 var stageCategory_sub=document.getElementById('stageCategory_sub').value;
	  var stageCategory_sub_name=document.getElementById('stageCategory_sub_name').value;
	 
		 $.ajax({
			 type:"POST",
			 url:"sub_cat.php",
			 data:{
			 sel_stage_name:sel_stage_name,
			 stageCategory_sub:stageCategory_sub,
			 stageCategory_sub_name:stageCategory_sub_name,
		 },
			 success:function(result){
     // $("#result").html(result);
    }
		 });
}

function Client_entry()
{
	 var Client_name=document.getElementById('Client_name').value;
	 var Priority=document.getElementById('Priority').value;
	 // var stageCategory_sub_name=document.getElementById('stageCategory_sub_name').value;
	 
		 $.ajax({
			 type:"POST",
			 url:"client.php",
			 data:{
			 Client_name:Client_name,
			 Priority:Priority
			
		 },
			 success:function(result){
     // $("#result").html(result);
    }
		 });
}

function upload_img()
{
	 var upload_btb=document.getElementById('upload_btb').value;
	
	 // var stageCategory_sub_name=document.getElementById('stageCategory_sub_name').value;
	 
		 $.ajax({
			 type:"POST",
			 url:"upload.php",
			 data:{
			 upload_btb:upload_btb
			
			
		 },
		 success:function(result){
     // $("#result").html(result);
    }
		 });
}
	 
	
		
