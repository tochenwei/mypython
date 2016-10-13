<?php
print_r($_REQUEST);
$username = $_REQUEST['username'];
$pwd = $_REQUEST['pwd'];
$act = $_REQUEST['act'];
session_start();
if($act == 'login'){
	if($username=='test' && $pwd=='123456'){
		$_SESSION['username']=$username;
	}else{
		$_SESSION['username']='';
	}
}
if($act == 'info'){
	echo $_SESSION['username'];
}
?>