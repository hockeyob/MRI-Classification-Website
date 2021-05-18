<?php 
$command = escapeshellcmd('python /var/www/html/python_scripts/diagnose.py');
$output = shell_exec($command);
echo $output;
?>
