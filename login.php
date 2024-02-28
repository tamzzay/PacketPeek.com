<?php
	// Retrieve the form data
	$username = $_POST['username'];
	$password = $_POST['password'];
	
	// Check if the username and password are valid
	if ($username == 'myusername' && $password == 'mypassword') {
		echo 'Login successful!';
	} else {
		echo 'Invalid credentials!';
	}
?>